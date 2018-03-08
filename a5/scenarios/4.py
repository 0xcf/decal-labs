import lib.util as util


"""
Scenario Overview:
Simulating being unable to perform DNS lookup at all.  This can be done by
simply pointing the default resolver to be some bogus address.

Triage:
The student should note that name translation fails.  This can be done by first
showing that running a tool with a domain name fails i.e. ping google.com.
Next they can find out that running that same tool with a static IP might work,
a good IP to use is one that is public and well known i.e. google DNS at 
8.8.8.8.  Additionally, they can try to use a lookup tool like dig or
nslookup and discover that they fail.

Solution:
This can be solved by setting resolv.conf to point at a valid nameserver.
"""

RESOLV_FILE = "/etc/resolv.conf"

lines = []
# comment out all lines in the resolv file
with open(RESOLV_FILE, "r+") as resolv_file:
    for line in resolv_file:
        lines.append("#" + line)
    resolv_file.seek(0, 0)
    resolv_file.write(''.join(lines))
