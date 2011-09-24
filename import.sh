#!/bin/bash

for version in 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20 21; do
    wget http://lacusveris.com/PythonTidy/PythonTidy-1.$version.python -O PythonTidy.py 
    git add PythonTidy.py
    git commit --author 'Chuck Rhode <CRhode@LacusVeris.com>' \
    	--date=$( stat  -f "%Sm" -t '%FT%T' PythonTidy.py ) \
	-m "Import version 1.$version"
    git tag 1.$version -m "Version 1.$version"
done

