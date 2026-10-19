#!/bin/bash

mkdir -p extracted

for file in processed/*.log; do
	base=$(basename "$file" .log) 

	awk -v base="$base" '
	 /^Step / {
	   block++
	   outfile = sprintf("extracted/%s_block%d.csv", base, block)
	   hdr = ""
	   for (i=1; i<=NF; i++) hdr = hdr $i (i<NF ? "," : "")
	   print hdr > outfile
	   in_block = 1
	   next
	 }
 	 /^Loop time of/ {
	   in_block = 0
	   next
	 }
 	 in_block && NF > 0 {
	   row = ""
	   for (i=1; i<=NF; i++) row = row $i (i<NF ? "," : "")
	   print row > outfile
	 }

	' "$file"

	echo "Extracted blocks from $file"
done
