import lib.util as util


INTERFACES_FILE = "/etc/network/interfaces"

routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface = default_entry.iface

command = "sed -i 's/dhcp/manual/g' {iface_file}".format(iface_file=INTERFACES_FILE)
util.run(command)

command = "ip addr flush {iface}".format(iface=default_iface)
util.run(command)
