.PHONY: dev

dev-services:
	nx serve sso & \
	nx serve study-mode-api & \
	nx serve token-metering-api & \
	nx serve progress-api & \
	wait

dev-book:
	nx serve learn-app & \
	wait

dev-progress-api:
	cd apps/progress-api && docker compose up -d && \
	cd apps/progress-api && uv run uvicorn progress_api.main:app --reload --port 8002