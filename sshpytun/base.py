import os
from pathlib import Path

class SSHTunnel:
    def __init__(self):
        self._user = None
        self._host = None
        self._port = 22
        self._identity = None
        self._config = str(Path.home() / ".ssh" / "config")
        self._bind_address = "localhost"
        self._flags = ["-fN"]

    # Fluent setters
    def user(self, user):
        self._user = user
        return self

    def host(self, host):
        self._host = host
        return self

    def port(self, port):
        self._port = int(port)
        return self

    def identity(self, path):
        self._identity = path
        return self

    def config(self, path):
        self._config = path
        return self

    def bind_address(self, addr):
        self._bind_address = addr
        return self

    def validate(self):
        if not self._user:
            raise ValueError("User is required")
        if not self._host:
            raise ValueError("Host is required")
        if self._identity and not os.path.isfile(os.path.expanduser(self._identity)):
            raise FileNotFoundError(f"Identity file not found: {self._identity}")
        if self._config and not os.path.isfile(os.path.expanduser(self._config)):
            raise FileNotFoundError(f"SSH config file not found: {self._config}")

    def base_command(self):
        self.validate()
        cmd = ["ssh"]
        cmd.extend(self._flags)
        cmd.extend(["-F", os.path.expanduser(self._config)])
        cmd.extend(["-p", str(self._port)])
        if self._identity:
            cmd.extend(["-i", os.path.expanduser(self._identity)])
        cmd.append(f"{self._user}@{self._host}")
        return cmd

    def build(self):
        raise NotImplementedError("Must be implemented by subclasses")

    def __str__(self):
        return self.build()

    def __repr__(self):
        return (f"<{self.__class__.__name__} user={self._user} host={self._host} "
                f"port={self._port} identity={self._identity} bind_address={self._bind_address}>")
