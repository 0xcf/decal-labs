#!/bin/bash
echo ocfdecal| gpg -o file3.txt --decrypt file3.txt.gpg
chmod 404 file3.txt
sudo chown nobody file3.txt
rm file3.txt.gpg

echo ocfdecal| gpg -o file4.txt --decrypt file4.txt.gpg
chmod 644 file4.txt
sudo chown nobody file4.txt
rm file4.txt.gpg

echo ocfdecal| gpg -o file5 --decrypt file5.gpg
chmod 000 file5
sudo chown nobody file5 
rm file5.gpg

echo ocfdecal| gpg -o file6.txt --decrypt file6.txt.gpg
chmod 400 file6.txt
sudo chown nobody file6.txt
rm file6.txt.gpg

echo ocfdecal| gpg -o file7.txt --decrypt file7.txt.gpg
chmod 400 file7.txt
sudo chown nobody file7.txt
rm file7.txt.gpg

echo ocfdecal| gpg -o file8.txt --decrypt file8.txt.gpg
chmod 777 file8.txt
sudo chown nobody file8.txt
rm file8.txt.gpg

echo ocfdecal| gpg -o file9.txt --decrypt file9.txt.gpg
chmod 777 file9.txt
sudo chown nobody file9.txt
rm file9.txt.gpg
