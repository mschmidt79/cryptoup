#!/bin/bash
SHELL=/bin/sh PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
#####################################
#         cryptoup.sh               #
#      svedbox@gmail.com            #
#     An alternative variant        #
#      to run through the           #
#     terminal (without GUI)        #
#   --------------------------      # 
#   Before running you need         #
#    make the file executable       #
#  (sudo chmod +x .../cryptoup.sh)  #
#####################################
zenity --info --title="Wellcome to Cryptoup" --text="Please select crypto-container file"
FILE=`zenity --file-selection --title="Select crypto-container file"`
clear

sudo mkdir /media/cryptoup
sudo losetup /dev/loop1 $FILE 
sudo tcplay --map=secvol --device=/dev/loop1
sudo mount /dev/mapper/secvol /media/cryptoup/

read  -s -n1 -p "*** PRESS ANY KEY FOR DISMOUNT CRYPTO DISK ***" keypress

sudo umount -l /media/cryptoup/
sudo tcplay --unmap=secvol
sudo losetup -d /dev/loop1
sudo rmdir /media/cryptoup

echo; echo "OK"
exit 0
