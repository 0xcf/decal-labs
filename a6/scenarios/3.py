import lib.util as util

HOSTS_FILE = "/etc/hosts"
ENTRY = "72.66.115.13 google.com\n"

with open(HOSTS_FILE, "a") as host_file:
    host_file.write(ENTRY)
