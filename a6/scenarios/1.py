import lib.util as util


command = "ifdown {iface}"
routing_entries = util.get_default_routing_information()
default_entry = next(
    (e for e in routing_entries if util.is_default_gateway(e)),
    None
)

util.run(command.format(iface=default_entry.iface))
