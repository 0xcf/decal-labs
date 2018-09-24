import lib.util as util


RESOLV_FILE = "/etc/resolv.conf"

lines = []
with open(RESOLV_FILE, "r+") as resolv_file:
    for line in resolv_file:
        lines.append("#" + line)
    resolv_file.seek(0, 0)
    resolv_file.write(''.join(lines))
