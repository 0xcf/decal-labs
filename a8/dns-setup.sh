#!/bin/bash
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
    echo "You need to run this as root."
    exit 1
fi

mkdir -p /etc/bind

cat > /etc/bind/named.conf.options <<EOF
// Berkeley IP ranges
acl "berkeley" {
	128.32/16;
	136.152/16;
	169.229/16;
	208.1.64/19;
	192.31.161/24;
	192.58.221/24;
	2607:f140::/32;
};

options {
	directory "/var/cache/bind";

	dnssec-validation auto;
	auth-nxdomain no;    # conform to RFC1035
	listen-on-v6 { any; };

	allow-query { any; };

	recursion yes;
	allow-recursion { localhost; "berkeley"; };
};
EOF

cat > /etc/bind/db.example.com <<EOF
;
; BIND data file example.com
;
\$TTL	604800
@	IN	SOA	ns.example.com. root.example.com. (
				1		; Serial
				604800		; Refresh
				86400		; Retry
				2419200		; Expire
				604800 )	; Negative Cache TTL
;
@	IN	NS	$(hostname -f).
@	IN	A	$(hostname -I | cut -d" " -f1)
test	IN	A	93.184.216.34
EOF
