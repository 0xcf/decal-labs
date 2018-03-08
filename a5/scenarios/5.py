import lib.util as util
from shutil import copyfile


RESOLV_FILE = "/etc/resolv.conf"
ENTRY = "nameserver {local_ns}\n"
DNSMASQ_HOST_FILE_SRC = "config/dnsmasq.hosts"
DNSMASQ_HOST_FILE_DST = "/etc/dnsmasq.hosts"
DNSMASQ_CONFIG_FILE_SRC = "config/dnsmasq.conf"
DNSMASQ_CONFIG_FILE_DST = "/etc/dnsmasq.conf"

routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface_entry = next(
    (e for e in routing_entries if not util.is_default_gateway(e) and e.iface == default_entry.iface),
    None
)

ENTRY = ENTRY.format(local_ns=util.get_iface_ip_address(default_iface_entry.iface))

copyfile(DNSMASQ_HOST_FILE_SRC, DNSMASQ_HOST_FILE_DST)
copyfile(DNSMASQ_CONFIG_FILE_SRC, DNSMASQ_CONFIG_FILE_DST)

with open(RESOLV_FILE, "r+") as resolv_file:
    original = resolv_file.read()
    resolv_file.seek(0, 0)
    resolv_file.write(ENTRY + original)

command = "killall -9 dnsmasq"
util.run(command)
command = "dnsmasq"
util.run(command)
