import socket, struct, fcntl
from collections import namedtuple
import subprocess
from shlex import split
from codecs import decode as decipher

ROUTE = "/proc/net/route"

RoutingEntry = namedtuple(
    'RoutingEntry', 
    ['iface', 'gateway', 'mask', 'dst', 'flags']
)

def is_default_gateway(routing_entry):
    return routing_entry.dst  == '00000000' and int(routing_entry.flags, 16) & 2

def get_default_routing_information():
    routing_entries = []
    with open(ROUTE) as route_file:
        for line in route_file:
            fields = line.strip().split()
            try:
                routing_entries.append(RoutingEntry(
                    iface=fields[0],
                    gateway=hex2address(fields[2]),
                    mask=hex2address(fields[7]),
                    dst=fields[1],
                    flags=fields[3]
                ))
            except ValueError:
                continue
    return routing_entries

def get_iface_ip_address(iface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(iface[:15], 'utf-8'))
    )[20:24])

def hex2address(val):
    return socket.inet_ntoa(struct.pack("<L", int(val, 16)))

def run(command):
    args = split(command)
    return subprocess.run(
        args,
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.STDOUT
    )

def decode(cipher):
    return decipher(cipher, "rot-13")

