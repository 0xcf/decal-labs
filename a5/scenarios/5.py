import lib.util as util
from shutil import copyfile


"""
Scenario Overview:
We will be simulating spoofed DNS responses using dnsmasq, a tool that will
let us run a nameserver on our local machine.  Once the nameserver is up, we
will configure certain hostnames to point to a blackhole server.  Additionally,
we will edit /etc/resolv.conf to prioritize the local nameserver when it comes 
to resolving hostnames via lookup tools like dig.

Triage:
The student should use a lookup tool like dig to verify that they are receiving
DNS responses for their queries.  However, since these entries are spoofed the
bindings are bogus.  They should cross validate this result -- one good way to
do this is to have the lookup tool use an alternative nameserver to issue the
same query and notice that connections to this IP are valid.  Another option is
to perform a reverse DNS lookup via another DNS server.  The key here is that
you need to cross validate the IP in the DNS response in order to confirm that
it's invalid.

Solution:
Since the current DNS server has a malicious record there are multiple ways to
solve this issue.  One can place a static entry in /etc/hosts if the IP of the
destination in question doesn't change.  Additionally, you can modify the
default DNS server to be something more 'trustworthy', Google DNS at 8.8.8.8
for example.  This can be done by adding an entry in /etc/resolv.conf, mind the
order of the entry since this affects its priority.
"""
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

# Copy over dnsmasq conf and hosts file
copyfile(DNSMASQ_HOST_FILE_SRC, DNSMASQ_HOST_FILE_DST)
copyfile(DNSMASQ_CONFIG_FILE_SRC, DNSMASQ_CONFIG_FILE_DST)

# Add a line to resolv.conf to prioritize the local nameserver when executing DNS queries
with open(RESOLV_FILE, "r+") as resolv_file:
    original = resolv_file.read()
    resolv_file.seek(0, 0)
    resolv_file.write(ENTRY + original)

# Restart dnsmasq server
command = "killall -9 dnsmasq"
util.run(command)
command = "dnsmasq"
util.run(command)
