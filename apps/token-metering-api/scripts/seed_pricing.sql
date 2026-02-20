-- Seed pricing data for token-metering-api
-- Tables are created by SQLModel metadata.create_all() on startup
-- Run this AFTER starting the service once to create tables

-- Clear existing pricing (for fresh setup)
DELETE FROM pricing;

-- DeepSeek Chat (study-mode-api ask agent) - $0.14/$0.28 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active, effective_date, created_at)
VALUES ('deepseek-chat', 0.00014, 0.00028, 64000, 'deepseek-v3.2', true, CURRENT_DATE, NOW());

-- GPT-5 Nano (study-mode-api triage agent) - $0.05/$0.40 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active, effective_date, created_at)
VALUES ('gpt-5-nano-2025-08-07', 0.00005, 0.00040, 128000, 'gpt5-nano-v1', true, CURRENT_DATE, NOW());

-- Claude Sonnet 4 - $3/$15 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active, effective_date, created_at)
VALUES ('claude-sonnet-4-20250514', 0.003, 0.015, 200000, 'claude-sonnet-4-v1', true, CURRENT_DATE, NOW());

-- Claude Opus 4 - $15/$75 per 1M tokens
INSERT INTO pricing (model, input_cost_per_1k, output_cost_per_1k, max_tokens, pricing_version, is_active, effective_date, created_at)
VALUES ('claude-opus-4-20250514', 0.015, 0.075, 200000, 'claude-opus-4-v1', true, CURRENT_DATE, NOW());

-- Verify
SELECT model, input_cost_per_1k as "$/1k in", output_cost_per_1k as "$/1k out", max_tokens, pricing_version
FROM pricing WHERE is_active = true ORDER BY model;
