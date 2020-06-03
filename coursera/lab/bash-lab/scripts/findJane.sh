#!/bin/bash

files=""

> data/oldFiles.txt

#grep " jane " ~/data/list.txt | cut -d ' ' -f 3 >> ~/data/oldFiles.txt
files=$(grep " jane " data/list.txt | cut -d ' ' -f 3)

#echo $files 

for file in $files ; do
    echo $PWD$file;
    if test -e $PWD$file ; then 
        echo $PWD$file >> data/oldFiles.txt
    fi
done