from .base import SSHTunnel

class RemoteTunnel(SSHTunnel):
    def __init__(self):
        super().__init__()
        self._remote_port = None
        self._local_host = None
        self._local_port = None

    def remote_port(self, port):
        self._remote_port = int(port)
        return self

    def local_host(self, host):
        self._local_host = host
        return self

    def local_port(self, port):
        self._local_port = int(port)
        return self

    def build(self):
        if not (self._remote_port and self._local_host and self._local_port):
            raise ValueError("Remote port, local host, and local port are required for remote tunnel")
        cmd = self.base_command()
        cmd.append(f"-R {self._remote_port}:{self._local_host}:{self._local_port}")
        return " ".join(cmd)

    def __repr__(self):
        return (f"<RemoteTunnel user={self._user} host={self._host} port={self._port} "
                f"remote_port={self._remote_port} local_host={self._local_host} "
                f"local_port={self._local_port} bind_address={self._bind_address}>")
