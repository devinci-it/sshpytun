import argparse
from sshpytun.dynamic import DynamicTunnel
from sshpytun.local import LocalTunnel
from sshpytun.remote import RemoteTunnel

def common_user_host_args(parser):
    """Add common user/host/identity args to a parser."""
    parser.add_argument("user", help="SSH username")
    parser.add_argument("host", help="SSH server hostname or IP")
    parser.add_argument("-p", "--port", type=int, default=22, help="SSH server port (default: 22)")
    parser.add_argument("-i", "--identity", help="Path to SSH identity file")
    parser.add_argument("-b", "--bind-address", default="localhost", help="Local bind address (default: localhost)")

def handle_tunnel(args, TunnelClass, **extra_setters):
    """
    Instantiate the given TunnelClass and set properties based on args.

    extra_setters: dict mapping TunnelClass setter method name -> argparse arg name
    """
    tunnel = TunnelClass()\
        .user(args.user)\
        .host(args.host)\
        .port(args.port)\
        .identity(args.identity)\
        .bind_address(args.bind_address)

    for setter_name, arg_name in extra_setters.items():
        setter = getattr(tunnel, setter_name, None)
        if not setter:
            raise AttributeError(f"Tunnel class '{TunnelClass.__name__}' has no setter '{setter_name}'")
        setter(getattr(args, arg_name))

    print(tunnel.build())

def main():
    parser = argparse.ArgumentParser(prog="sshpytun")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Dynamic tunnel parser
    p = subparsers.add_parser("dyn", help="Create a dynamic SOCKS tunnel")
    common_user_host_args(p)
    p.add_argument("-lp", "--local-port", type=int, required=True, help="Local port for SOCKS proxy")
    p.set_defaults(func=lambda args: handle_tunnel(args, DynamicTunnel, local_port="local_port"))

    # Local tunnel parser
    p = subparsers.add_parser("loc", help="Create a local tunnel")
    common_user_host_args(p)
    p.add_argument("-lp", "--local-port", type=int, required=True, help="Local port to bind")
    p.add_argument("-rh", "--remote-host", required=True, help="Remote host to forward to")
    p.add_argument("-rp", "--remote-port", type=int, required=True, help="Remote port to forward to")
    p.set_defaults(func=lambda args: handle_tunnel(
        args,
        LocalTunnel,
        local_port="local_port",
        remote_host="remote_host",
        remote_port="remote_port"
    ))

    # Remote tunnel parser
    p = subparsers.add_parser("rem", help="Create a remote tunnel")
    common_user_host_args(p)
    p.add_argument("-rp", "--remote-port", type=int, required=True, help="Remote port to bind")
    p.add_argument("-lh", "--local-host", required=True, help="Local host to forward from")
    p.add_argument("-lp", "--local-port", type=int, required=True, help="Local port to forward from")
    p.set_defaults(func=lambda args: handle_tunnel(
        args,
        RemoteTunnel,
        remote_port="remote_port",
        local_host="local_host",
        local_port="local_port"
    ))

    args = parser.parse_args()
    args.func(args)

# Wrapper functions for separate console scripts (if desired)
import sys

def main_dyn():
    sys.argv.insert(1, "dyn")
    main()

def main_loc():
    sys.argv.insert(1, "loc")
    main()

def main_rem():
    sys.argv.insert(1, "rem")
    main()

if __name__ == "__main__":
    main()
