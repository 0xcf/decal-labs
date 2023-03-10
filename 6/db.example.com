;
; BIND data file example.com
;
$TTL	604800
@	IN	SOA	ns.example.com. root.example.com. (
				1		      ; Serial
				604800		; Refresh
				86400		  ; Retry
				2419200		; Expire
				604800 )	; Negative Cache TTL
;
        IN	NS	ns.example.com.

ns  IN  A   127.0.0.1                ; IP for name server (random ip)
@	IN	A	1.2.3.4                  ; A record for example.com (random ip)
; Add more records (Ex. CNAME, AAAA, MX, subdomains...)