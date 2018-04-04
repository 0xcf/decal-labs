#!/bin/bash
sudo chown ocfdecal:ocfdecal file1.txt.gpg
sudo chmod 400 file1.txt.gpg
sudo chown ocfdecal:ocfdecal file2.txt.gpg
sudo chmod 400 file2.txt.gpg
sudo chown ocfdecal:ocfdecal file3.txt
sudo chmod 404 file3.txt
sudo chown ocfdecal:ocfdecal file4.txt
sudo chmod 644 file4.txt
sudo chown ocfdecal:ocfdecal file5
sudo chmod 000 file5
sudo chown ocfdecal:ocfdecal file6.txt
sudo chmod 400 file6.txt
sudo chown ocfdecal:ocfdecal file7.txt
sudo chmod 400 file7.txt
sudo chown ocfdecal:ocfdecal file8.txt
sudo chmod 777 file8.txt
sudo chown ocfdecal:ocfdecal file9.txt
sudo chmod 777 file9.txt
sudo chown ocfdecal:ocfdecal privkey
sudo chmod 400 privkey

sudo apt-get install haveged
