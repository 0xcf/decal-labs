import lib.util as util


INTERFACES_FILE = "/etc/network/interfaces"

routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface = default_entry.iface

lines = []
with open(INTERFACES_FILE, "r+") as iface_file:
    for line in iface_file:
        if default_iface in line and "dhcp" in line:
            lines.append(line.replace("dhcp", "manual"))
        else:
            lines.append(line)
    iface_file.seek(0, 0)
    iface_file.write(''.join(lines))

command = "ip addr flush {iface}".format(iface=default_iface)
util.run(command)
