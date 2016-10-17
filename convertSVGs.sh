#!/bin/bash
mkdir -p img
for file in svg/*.svg
    do
        filename=$(basename $file)
        inkscape "$file" -d 1200 -A img/"${filename%.svg}.pdf"
    done