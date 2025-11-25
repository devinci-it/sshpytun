from .base import SSHTunnel

class LocalTunnel(SSHTunnel):
    def __init__(self):
        super().__init__()
        self._local_port = None
        self._remote_host = None
        self._remote_port = None

    def local_port(self, port):
        self._local_port = int(port)
        return self

    def remote_host(self, host):
        self._remote_host = host
        return self

    def remote_port(self, port):
        self._remote_port = int(port)
        return self

    def build(self):
        if not (self._local_port and self._remote_host and self._remote_port):
            raise ValueError("Local port, remote host, and remote port are required for local tunnel")
        cmd = self.base_command()
        cmd.append(f"-L {self._bind_address}:{self._local_port}:{self._remote_host}:{self._remote_port}")
        return " ".join(cmd)

    def __repr__(self):
        return (f"<LocalTunnel user={self._user} host={self._host} port={self._port} "
                f"local_port={self._local_port} remote_host={self._remote_host} "
                f"remote_port={self._remote_port} bind_address={self._bind_address}>")
