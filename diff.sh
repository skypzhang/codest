#!/bin/bash
cat file1.txt file2.txt | sort | uniq -d >temp.txt
cat file1.txt temp.txt | sort | uniq -u >file.txt
