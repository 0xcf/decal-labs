#!/bin/bash
sudo chown nobody file1.txt.gpg
sudo chmod 400 file1.txt.gpg
sudo chown nobody file2.txt.gpg
sudo chmod 400 file2.txt.gpg
sudo chown nobody file3.txt
sudo chmod 404 file3.txt
sudo chown nobody file4.txt
sudo chmod 644 file4.txt
sudo chown nobody file5
sudo chmod 000 file5
sudo chown nobody file6.txt
sudo chmod 400 file6.txt
sudo chown nobody file7.txt
sudo chmod 400 file7.txt
sudo chown nobody file8.txt
sudo chmod 777 file8.txt
sudo chown nobody file9.txt
sudo chmod 777 file9.txt
sudo chown nobody privkey
sudo chmod 400 privkey

sudo apt -qq install -y haveged
