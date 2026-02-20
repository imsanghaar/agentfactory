-- reserve.lua: Atomically create reservation using sorted set (v6)
-- KEYS[1] = metering:reservations:{user_id}
-- ARGV[1] = request_id (UUID format, no colons)
-- ARGV[2] = credits to reserve
-- ARGV[3] = current timestamp (unix epoch)
-- ARGV[4] = expiry timestamp (unix epoch, current + TTL)
--
-- Returns: {status, reserved_total, existing_tokens}
--   status = 0: new reservation created
--   status = 1: idempotent (same request_id, same tokens)
--   status = 2: conflict (same request_id, different tokens)

local key = KEYS[1]
local request_id = ARGV[1]
local tokens = tonumber(ARGV[2])
local now = tonumber(ARGV[3])
local expiry = tonumber(ARGV[4])

-- Step 1: Cleanup expired reservations (score < now) - FR-036
redis.call('ZREMRANGEBYSCORE', key, '-inf', now)

-- Step 2: Check if request_id already exists (idempotency) - FR-059, FR-060
local members = redis.call('ZRANGE', key, 0, -1)
for i, member in ipairs(members) do
    -- Member format: "request_id:tokens"
    -- Split on LAST colon to extract tokens (request_id is UUID, no colons)
    local sep = member:find(':[^:]*$')
    if sep then
        local existing_req_id = member:sub(1, sep - 1)
        local existing_tokens = tonumber(member:sub(sep + 1))

        if existing_req_id == request_id then
            if existing_tokens == tokens then
                -- Same request_id, same tokens: return existing (idempotent)
                local reserved_total = 0
                for j, m in ipairs(members) do
                    local s = m:find(':[^:]*$')
                    if s then
                        reserved_total = reserved_total + tonumber(m:sub(s + 1))
                    end
                end
                return {1, reserved_total, existing_tokens}
            else
                -- Same request_id, different tokens: conflict
                local reserved_total = 0
                for j, m in ipairs(members) do
                    local s = m:find(':[^:]*$')
                    if s then
                        reserved_total = reserved_total + tonumber(m:sub(s + 1))
                    end
                end
                return {2, reserved_total, existing_tokens}
            end
        end
    end
end

-- Step 3: Add new reservation - FR-036
local member = request_id .. ':' .. tokens
redis.call('ZADD', key, expiry, member)

-- Step 4: Set key expiry for automatic cleanup (2x reservation TTL = 600s)
-- This ensures keys for inactive users are automatically cleaned up
redis.call('EXPIRE', key, 600)

-- Step 5: Compute reserved_total from all members (including new one)
members = redis.call('ZRANGE', key, 0, -1)
local reserved_total = 0
for i, m in ipairs(members) do
    local s = m:find(':[^:]*$')
    if s then
        reserved_total = reserved_total + tonumber(m:sub(s + 1))
    end
end

return {0, reserved_total, tokens}
