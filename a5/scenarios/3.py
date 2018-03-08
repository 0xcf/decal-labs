import lib.util as util

"""
Scenario Overview:
The /etc/hosts file will have an invalid entry for a website (google.com) which
points to a blackhole webserver.  Pinging this poisoned hostname will work but
any connections over TCP will fail, noticeably HTTP.

Triage:
The student should identify there is an issue when trying to connect to the 
domain over TCP, via a tool like "curl -L google.com" , "wget google.com", or
"telnet google.com 80".

Note that for this scenario ping will succeed, nefarious since the ip does not
correspond with the intended hostname.

Also note that using a lookup tool like dig or nslookup will return the valid
address for the hostname since it will not look into the /etc/hosts file and
will instead make a query to a nameserver. If the student discovered the
discrepancy between ip address returned via a lookup tool and the one used
when trying to connect via telenet, ping, or etc. then good on them!

Solution:
The solution here is simple, remove the invalid entry for the hostname from the /etc/hosts file.  In the future, resolving this hostname should either be done via DNS query or if the hostname in question has a static address, a valid entry can be added to the /etc/hosts file.
"""
HOSTS_FILE = "/etc/hosts"
ENTRY = "72.66.115.13 google.com\n"

# Edit their hosts file to contain a bad entry
with open(HOSTS_FILE, "a") as host_file:
    host_file.write(ENTRY)
