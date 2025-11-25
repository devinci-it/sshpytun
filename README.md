.----------------------------------------------------.
|  ░▄█▄█▄░█░░░█▀▀░█▀▀░█░█░█▀█░█░█░▀█▀░█░█░█▀█░░░▀▄░  |
|  ░▄█▄█▄░▀░░░▀▀█░▀▀█░█▀█░█▀▀░░█░░░█░░█░█░█░█░░░░▄▀  |
|  ░░▀░▀░░▀░░░▀▀▀░▀▀▀░▀░▀░▀░░░░▀░░░▀░░▀▀▀░▀░▀░░░▀░░  |
'----------------------------------------------------'

---

# sshpytun

**sshpytun** is a flexible, Python-based SSH tunnel utility with support for Dynamic (SOCKS), Local, and Remote tunnels.  
It provides a clean, fluent interface for building SSH commands with optional support for SSH identity files, custom ports, and bind addresses.

---

## Features

- Create **dynamic SOCKS** tunnels (`-D` flag) for proxying.
- Create **local port forwarding** tunnels (`-L` flag).
- Create **remote port forwarding** tunnels (`-R` flag).
- Fluent Python API design for easy extension.
- CLI with subcommands for each tunnel type.
- Supports specifying SSH user, host, port, identity file, and bind address.
- Simple and minimal dependencies.

---

## Installation

### Prerequisites

- Python 3.7+
- SSH client installed on your system (`ssh` command)
- `git` (optional, for cloning)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/devinci-it/sshpytun.git
   cd sshpytun
   ```

2.	(Optional) Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate


	3.	Upgrade pip and build tools:

python3 -m pip install --upgrade pip setuptools wheel


	4.	Install the package in editable mode with development dependencies:

pip install -e .
pipenv install --dev



⸻

Usage

The main CLI entrypoint is sshpytun with three subcommands:
	•	dyn — Dynamic SOCKS tunnel
	•	loc — Local port forwarding tunnel
	•	rem — Remote port forwarding tunnel

Run:
```
sshpytun --help
```
to see general help.

⸻

Examples

Dynamic Tunnel (SOCKS proxy)
```
sshpytun dyn <user> <host> --local-port 1080
```
Equivalent to:
```
ssh -fN -F ~/.ssh/config -p 22 <user>@<host> -D localhost:1080
```
You can specify:
	•	-p or --port for SSH server port
	•	-i or --identity for SSH private key
	•	-b or --bind-address for local bind address (default: localhost)

⸻

Local Tunnel (Local port forwarding)
```
sshpytun loc <user> <host> --local-port 8080 --remote-host remote.example.com --remote-port 80
```
Equivalent to:
```
ssh -fN -F ~/.ssh/config -p 22 <user>@<host> -L localhost:8080:remote.example.com:80
```

⸻

Remote Tunnel (Remote port forwarding)
```
sshpytun rem <user> <host> --remote-port 9090 --local-host 127.0.0.1 --local-port 3000
```
Equivalent to:
```
ssh -fN -F ~/.ssh/config -p 22 <user>@<host> -R 9090:127.0.0.1:3000

```
⸻

Python API (Fluent Interface)

You can also use the Python classes directly:
```
from sshpytun.dynamic import DynamicTunnel

tunnel = DynamicTunnel()\
    .user("alice")\
    .host("ssh.example.com")\
    .local_port(1080)

print(tunnel.build())
# Outputs: ssh -fN -F ~/.ssh/config -p 22 alice@ssh.example.com -D localhost:1080
```
Similar APIs exist for LocalTunnel and RemoteTunnel.

⸻

Development
	•	The source code is under the sshpytun/ directory.
	•	Main CLI logic is in app.py.
	•	Use pipenv for managing virtual environments and dependencies.
	•	To run tests or extend functionality, add scripts under scripts/ or extend the modules.

⸻

Packaging and Installation

The project uses setup.py with entry points for console scripts:
	•	sshpytun - main CLI with subcommands
	•	sshpytun-dyn - dynamic tunnel CLI wrapper
	•	sshpytun-loc - local tunnel CLI wrapper
	•	sshpytun-rem - remote tunnel CLI wrapper

You can install the package locally in editable mode with:
	
	```
	pip install -e .

	```
⸻

License

MIT License © devinci-it

⸻

Contact

For questions or contributions, please open issues or pull requests on GitHub.

⸻


