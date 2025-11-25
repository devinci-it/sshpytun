from .base import SSHTunnel

class DynamicTunnel(SSHTunnel):
    def __init__(self):
        super().__init__()
        self._local_port = None

    def local_port(self, port):
        self._local_port = int(port)
        return self

    def build(self):
        if not self._local_port:
            raise ValueError("Local port required for dynamic tunnel")
        cmd = self.base_command()
        cmd.append(f"-D {self._bind_address}:{self._local_port}")
        return " ".join(cmd)

    def __repr__(self):
        return (f"<DynamicTunnel user={self._user} host={self._host} port={self._port} "
                f"local_port={self._local_port} bind_address={self._bind_address}>")
