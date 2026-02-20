-- finalize.lua: Remove reservation from sorted set on deduct (v6)
-- KEYS[1] = metering:reservations:{user_id}
-- ARGV[1] = request_id (UUID format, no colons)
-- ARGV[2] = current timestamp (unix epoch) for cleanup
--
-- Returns: {status, removed_tokens}
--   status = 1: reservation found and removed
--   status = 0: reservation not found (may have expired or already finalized)

local key = KEYS[1]
local request_id = ARGV[1]
local now = tonumber(ARGV[2])

-- Cleanup expired reservations first (opportunistic)
redis.call('ZREMRANGEBYSCORE', key, '-inf', now)

-- Find and remove the member with matching request_id - FR-037
local members = redis.call('ZRANGE', key, 0, -1)
for i, member in ipairs(members) do
    local sep = member:find(':[^:]*$')
    if sep then
        local existing_req_id = member:sub(1, sep - 1)
        local tokens = tonumber(member:sub(sep + 1))

        if existing_req_id == request_id then
            redis.call('ZREM', key, member)
            -- Refresh key expiry (2x reservation TTL = 600s) for active users
            redis.call('EXPIRE', key, 600)
            return {1, tokens}
        end
    end
end

-- Reservation not found
return {0, 0}
