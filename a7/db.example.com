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
@	IN	NS	yourvm.decal.xcf.sh.   ; Edit this!
@	IN	A	1.2.3.4                  ; Edit this!
test	IN	A	93.184.216.34
