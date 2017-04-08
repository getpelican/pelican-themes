#!/bin/bash
#for i in GPL LGPL by-nc-nd by-nc-sa by-nc by-nd-nc by-nd by-sa;  do
for i in by-nc-nd by-nc-sa by-nc by-nd-nc by-nd by-sa;  do
    mkdir -p $i/4.0
    wget https://licensebuttons.net/l/$i/4.0/80x15.png -O $i/4.0/80x15.png
    wget https://licensebuttons.net/l/$i/4.0/88x31.png -O $i/4.0/88x31.png
done
