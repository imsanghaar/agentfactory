### Core Concept
**The binding address, firewall rules, and SSH configuration determine whether your agent is reachable — security without connectivity is a locked room with no door.** When a deployed agent is unreachable, the cause is almost always one of three things: wrong binding address, a firewall blocking the port, or connecting to the wrong port entirely. This lesson gives you the diagnostic toolkit and secure remote access patterns to solve each.

### Key Mental Models
- **Ports as Numbered Doors**: A port identifies a specific service on a machine. Port 22 = SSH, port 8000 = your agent. Ports below 1024 require root; higher ports align with least privilege.
- **127.0.0.1 vs 0.0.0.0**: Binding to `127.0.0.1` means only the local machine can reach the service. Binding to `0.0.0.0` opens it to the network. This is the most common reason agents are unreachable.
- **Default-Deny Firewall**: Block everything, then explicitly allow only needed ports.
- **SSH Config as Address Book**: `~/.ssh/config` maps short aliases to full connection details, turning `ssh prod-server` into a complete connection.

### Critical Patterns
- **ss -tlnp to check listeners**: Shows which services are bound to which ports and addresses. If nothing appears for your agent's port, the process isn't running.
- **curl for HTTP testing**: `curl http://localhost:8000/health` tests local connectivity. Add `-v` for verbose output including headers and connection details.
- **SSH key-based authentication**: Generate keys with `ssh-keygen -t ed25519`, copy public key to server. Disable password authentication in `sshd_config` for security.
- **ufw for firewall management**: `sudo ufw allow 22/tcp` allows SSH; `sudo ufw allow 8000/tcp` allows your agent. Always allow SSH before enabling the firewall.

### Common Mistakes
- **Binding to 127.0.0.1 in production**: Your agent works locally but is invisible to the network. Production agents must bind to `0.0.0.0`.
- **Enabling ufw without allowing SSH**: Locking yourself out by enabling a firewall that blocks port 22. Always allow SSH first.
- **Diagnosing from the wrong layer**: Jumping to firewall debugging when the agent isn't running. Test local connectivity first.
