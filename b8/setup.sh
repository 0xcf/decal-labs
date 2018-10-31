#!/bin/bash
echo ocfdecal| gpg -o file3.txt --decrypt file3.txt.gpg
sudo chown nobody file3.txt
sudo chmod 404 file3.txt
echo ocfdecal| gpg -o file4.txt --decrypt file4.txt.gpg
sudo chown nobody file4.txt
sudo chmod 644 file4.txt
echo ocfdecal| gpg -o file5 --decrypt file5.gpg
sudo chown nobody file5
sudo chmod 000 file5
echo ocfdecal| gpg -o file6.txt --decrypt file6.txt.gpg
sudo chown nobody file6.txt
sudo chmod 400 file6.txt
echo ocfdecal| gpg -o file7.txt --decrypt file7.txt.gpg
sudo chown nobody file7.txt
sudo chmod 400 file7.txt
echo ocfdecal| gpg -o file8.txt --decrypt file8.txt.gpg
sudo chown nobody file8.txt
sudo chmod 777 file8.txt
echo ocfdecal| gpg -o file9.txt --decrypt file9.txt.gpg
sudo chown nobody file9.txt
sudo chmod 777 file9.txt
