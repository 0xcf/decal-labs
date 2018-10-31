#!/bin/bash
set -euo pipefail

if [ $EUID -ne 0 ]; then
    echo "Please run this with sudo."
    exit 1
fi

GPGDIR=/tmp/lab8
PRIVKEY="$PWD/lab8privkey"

mkdir -p $GPGDIR

gpg --homedir "$GPGDIR" --import "$PRIVKEY"

decrypt() { gpg --homedir "$GPGDIR" -d --output "$1"; }

cat <<EOF | decrypt file3.txt && chmod 404 file3.txt && chown nobody file3.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQf/aDZDUjqaKzrE+AWN8tsIuON5QieEAYrPsJthHjOQffPy
tYZtt1Yu6RDteFq/KdRwYe/Lp30AoUqJX1JwNUNBRLbjQpNIPA9eE2w42lFgwBUd
vEBCYRl75Wb8kyixwxYPqt0xggi1CbWbzJTQhnhfzWF8216UjvZEo/BJJEzjfc/K
tm1rBf0vwgOsw4NNFbmCmDTX6qntAqrlHC+IgOkCjj+qmTPV/Q4TIj9Sjy9AiOB7
NIYZqUv8fufZ3gA81nlPgo7K7Wt/TQRthaUbM2kmlwrpHPn4cdQIIcCQsE7GOQ90
dSMWnitQXEDZp2xhJ8TmKE+5xefAr7A7iebSgUIr8tJMAUQ7NVR9yS1Bg5DEEYp2
nfxGMF4VgY7Rhmmhim/cOFAt0PZxfZhQ0D8Lh4NLLPt+UX1IkYGrajuGqnO+OmDP
+3DWs5sxgXSbOXk+kQ==
=uKIk
-----END PGP MESSAGE-----
EOF

cat <<EOF | decrypt file4.txt && chmod 644 file4.txt && chown nobody file4.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQf/RVxPPgoUtb28zqGN8DRzbTWHbFlCMdEQWv2XvyPuPCHb
PGwlV3ILOvQpH+D0kWA+20YFNr+uZ+tFX3LbmkOhgrAZy1bb32y7T632kURxq/5P
KM7upMADImiffI3jUJheqsOLF7urhcrd/mn5I748tqoFCnVLUMR0LAe2MFlfNdS8
MOdukWEGIW0LeQKpxAOMQTQf2Eb2Tko9F3OLVCdPFJcmC+u5p16IHLrMJED259hI
f1aP3unvkCobRTUEyupanDAtIo2afp+ygeRsC3Iftv0MX2s2DiuIfwZcxImBfvSp
ILoHvGB1qOJ2owYxcWTvepnG4uMIMnn8SMZTAuM8odJKASLx38pa2CNupYepVzjn
zRJ/NOQFVjM5wgW1+Fac4oBJQh2CzL4SN611jlt0Lk6q2AGQJrjzE5YBuqsKdXP+
/uTVUapNKPQx0GQ=
=ui/g
-----END PGP MESSAGE-----
EOF

cat <<EOF | decrypt file6.txt && chmod 400 file6.txt && chown nobody file6.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQgAyg67Yc+u6Yo4vFUZUTbTVfrVKoVZmtzy4yM6KxN1D7QQ
g90lvyqV/2VViYN4ynyg1uU1Ru1lLqvxYs+COPr1ij5zfzJvp9fQnUgLkvgejvEG
Sj4ENU6XRWmKco/H7dl4cp4btzykvlYCO7fKax1DmnuBrK9/QjHQhKsj3K2HmkBm
JXzfmsy4+/6Vnw+yueTikEOyyprn6QV8KfVNx9IOX14gitlGLYpN75vH/RHb4vh3
LObWsvODl8y5O8RyJb5nVRaUS0v50MBxAYwcNZI62AO6PmwT0cf6phGKipSGh2Zv
Yxj/6YDpuMcW36Wt1EzJxIWhnkvRfDN4xbghXTnGA9JQAUDBxCHiB/MM/UEQk3sa
sf1J1osXRsNxp8nN63Dby7FHhv/r80QM2bD8SfB0JZkEwnIozkVRU1gm5/l7Vzwm
m2eGxZIUX5H1/WtZkA3wa2Q=
=Nxi7
-----END PGP MESSAGE-----
EOF

cat <<EOF | decrypt file7.txt && chmod 400 file7.txt && chown nobody file7.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQgAqm2KqrXmMBdocdEfRGGzeIcp+LIv5LNx2JGgDFg/tjTc
oTcBcbz/waN4hl5FqaljVT8dj70/FpVNz7MLTWJa/cf+wf2Xd2us6kEfC+nARpqi
x62ilENBNZsnIhQG8oggvaCNqO0GsO4fwL75kyJ+w3B3sc/clIX7z3doLokJONLh
TADbk8GO/LwUlBtguubHiUu/H4wp9ED5M0XvzMpZlUApaxV3lc9pnUOXZSpk7dvM
LEKdAPu7X6xkWxx+Tl7f2mUI7EYzLyHKM40QHlq9eEarDz4YosercGIxmAfg1Z4a
U0LRAfEdF1GQ85n9KC8voRPSeCas0hi1BTxj0JOTnNJQAZYY409kcUTUytntwbBN
jyT3aprID7HGc2Kvl0TuxklD5Q64w8LcpGQRCbX5g4NCpybFo2wIODb6CP0dk8ex
sjw+rdPdv9T10xRoQwI5B3k=
=by0k
-----END PGP MESSAGE-----
EOF

cat <<EOF | decrypt file8.txt && chmod 777 file8.txt && chown nobody file8.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQgAmmxviNnMBnBWqoO9VVDKYtu3s3XCLtvQQ0NroHNOXY2G
5wD2cP8mNlLIuF9XKlaq9O3ivwRYDSwXPzWDt1lyBKrGcT9Jy9aLDt5QiG0ZEaZ2
LPotz3ZbnWVdplGYui+YrgvpHSwyHvj8srgqeLO3z4E9Z7rkYRVUtzo0HbYMICsu
tQ3xO6F9aL1Z5JrGGukgKl2WWqc5DqBxmzFbAqENf0yW5/BXG+qAxxGr0W8IiLuq
hfeoNA1rKBpRjKnrMth4fIzckJbqHqTl4FbcV2PuvEQ8CdFi/v41dEVp5nxklMMl
XRLYHGY/7uV2X/bj8qpGPQXghDvth0WQ3v3dr/ZoatJPAXMq9gOoYZpBJKdFq2iU
wk0jgsba1oyD1pahXQd2KvOgent//lyEb7bfxntp6lA1LhaR/9M/ER6iKXa3z5tV
hQzkVU7TNNDUm3uc1Mf9Ig==
=DrLZ
-----END PGP MESSAGE-----
EOF

cat <<EOF | decrypt file9.txt && chmod 777 file9.txt && chown nobody file9.txt
-----BEGIN PGP MESSAGE-----

hQEMA4OtrdUhwdONAQf/TFBgE43nYVP+bvzsVWLHk9ZR+GYjySQVKu9sQtHN/MbK
CVKd9NCDwASgjpNMaFt5z0BiUq0e9qsOJc1sxoamryb8FNjrldYiwDmgw7aaggFr
FBuQfOSoQeIzvC9AcOducSiALFD5DRPJVXn1f6g32UlAsrSmOGdXor+Jea9JVefi
8GlBHdrvOQG/zdEFt76bV4ZZE4r/vzsEYmddgWQNqt7VWoykfVkiGC451vlBWOYz
/dPhQmmU3bfcUs2Ibocqog7EhndYdHhu372ipWL+qi7gdfnWrM+2v7SQhBile6XO
2Iyicg6zlv+AgTCQ++kV/Sx0MXRmes6wuIoThd638dJOAehZdii5PGO46YoH9y76
VzaGujF8mcTfsbFdGpvNEOGENHwohoSgGNsoEyCJrTFEO+QcdvGPHDutwx3T+pwo
G3UULWemw6cKfk6Cv+Kw
=kUgM
-----END PGP MESSAGE-----
EOF
