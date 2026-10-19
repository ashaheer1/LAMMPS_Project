#!/bin/bash

mkdir -p processed

declare -A filemap=(
	["log.27Nov18.indent.g++.1"]="indent.log" 
	["log.8Apr21.melt.g++.1"]="melt.log"
	["log.27Nov18.min.box.g++.1"]="min_box.log"
	["log.27Nov18.indent.min.g++.1"]="indent_min.log"
)

for raw_name in "${!filemap[@]}"; do
	clean_name="${filemap[$raw_name]}"
	src="raw/$raw_name"
	dest="processed/$clean_name"

	if [ -f "$src" ]; then
	  cp "$src" "$dest"
	  echo "Copied $raw_name -> $clean_name"
  	else
	  echo "WARNING: $src not found, skipping"
	fi
done
