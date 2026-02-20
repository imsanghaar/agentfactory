.PHONY: dev

dev-services:
	nx serve sso & \
	nx serve study-mode-api & \
	nx serve token-metering-api & \
	wait

dev-book:
	nx serve learn-app & \
	wait