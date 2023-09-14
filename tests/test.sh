#!/bin/bash

groups=$(cat ./groups.txt)
echo "" > output.txt
for g in $groups;
do
    echo "### group="$g" ###" >> output.txt
    ../src/facebook-parse.py -u $g -d True >> output.txt
    echo "###END###" >> output.txt
    echo "" >> output.txt
done