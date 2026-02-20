### Core Concept
**systemd transforms your agent from a fragile manual process into an unkillable system service — it starts on boot, restarts after crashes, and runs under resource limits that prevent it from consuming your entire server.** A Digital FTE that requires manual restarts every time something goes wrong is not a production system; it's a babysitting obligation.

### Key Mental Models
- **Service File as Contract**: A `.service` file has three sections — `[Unit]` (identity and ordering), `[Service]` (how to run the process), and `[Install]` (boot integration). Each section controls a different aspect of the service's behavior.
- **Restart=on-failure, Not always**: `on-failure` restarts after crashes only. `always` restarts even after intentional stops. Use `on-failure` as the production default.
- **Start-Limit as Circuit Breaker**: `StartLimitBurst` and `StartLimitIntervalSec` prevent restart storms when a service crashes repeatedly.
- **Resource Limits as Safety Rails**: `MemoryMax` and `CPUQuota` cap consumption. A leak hits the limit instead of taking down the server.

### Critical Patterns
- **systemctl lifecycle commands**: `start` launches, `stop` halts, `enable` makes it start on boot, `disable` removes boot start, `status` shows current state. `daemon-reload` after editing service files.
- **journalctl for service logs**: `journalctl -u my-agent -f` follows live logs. Add `--since`, `--until`, and `-p err` to filter by time and severity.
- **systemctl show for verification**: `systemctl show my-agent --property=MemoryMax` confirms resource limits are applied as configured.
- **Health check scripting**: A script that curls the `/health` endpoint and checks the response validates that the service is not just running but actually functional.

### Common Mistakes
- **Using Restart=always**: Makes it impossible to intentionally stop your service without disabling it first. Use `Restart=on-failure` for production.
- **Forgetting daemon-reload**: After editing a service file, `systemctl daemon-reload` must be run before changes take effect. Without it, systemd uses the old configuration.
- **No resource limits**: A service without `MemoryMax` or `CPUQuota` can consume all server resources, affecting every other service on the machine.
