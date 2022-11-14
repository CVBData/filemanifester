#!/usr/bin/env python

import sys, os
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H_%M_%S")
current_date = str(now.date())
time_date = [current_time, current_date]
pre_outfile_name = '_'.join(time_date)
outfile_name = "file_manifest_"+pre_outfile_name+".tsv"
print(outfile_name)

root = input("Please type in directory path to directory containing files to list, followed by the enter key:")
output_location = input("Please type the path to the directory where you want the output to be stored, \
followed by the enter key:")
output_final_location = os.path.join(output_location, outfile_name)

with open(output_final_location, 'a') as f:
    print("fullPath\tfileOriginalName\tfileNewName", file=f)

for path, subdirs, files in os.walk(root):
    for name in files:
        line = os.path.join(path, name)
        out_string = [line, name]
        out = '\t'.join(out_string)
        with open(output_final_location, 'a') as f:
            print(out, file=f)

print(output_final_location)
