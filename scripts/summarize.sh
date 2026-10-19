#!/bin/bash

labels="extracted/block_labels.csv"

echo "=== Extraction Summary ==="
printf "%-25s %-8s %-6s %-45s %s\n" "File" "Rows" "Cols" "Description" "Columns"
echo "-------------------------------------------------------"

for csv in extracted/*.csv; do
	fname=$(basename "$csv" .csv)
	
	[ "$fname" = "block_labels" ] && continue

# split base block into separate base and block
	base=$(echo "$fname" | sed -E 's/_block[0-9]+$//')
	block=$(echo "$fname" | sed -E 's/.*_block([0-9]+)$/\1/')

	rows=$(( $( wc -l < "$csv") - 1 )) #removes the header row
	header=$(head -1 "$csv")
	ncols=$(echo "$header" | awk -F',' '{print NF}')

	desc=$(awk -F',' -v b="$base" -v n="$block" 'NR>1 && $1==b && $2==n {print $3}' "$labels")

	printf "%-25s %-8s %-6s %-45s %s\n" "$fname" "$rows" "$ncols" "$desc" "$header"
	
	done
