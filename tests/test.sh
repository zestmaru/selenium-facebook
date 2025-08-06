#!/bin/bash

GROUPS_FILE="groups.txt"
OUTPUT_FILE="output.txt"

debug=""

if [[ $1 == "true" ]]; then
    debug=-d True
fi

# Clear the output file
> "$OUTPUT_FILE"

while IFS= read -r group; do
    echo "### group=$group ###" | tee -a "$OUTPUT_FILE"
    ../src/facebook-parse.py -u "$group" $debug | tee -a "$OUTPUT_FILE"
    echo "###END###" | tee -a "$OUTPUT_FILE"
    echo "" | tee -a "$OUTPUT_FILE"
done < "$GROUPS_FILE"
