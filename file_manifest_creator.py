#!/usr/bin/env python

# import statements
import sys, os, time
from datetime import datetime

# set up date/time variables for output naming
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
current_date = str(now.date())
time_date = [current_time, current_date]
pre_outfile_name = '_'.join(time_date)

# name output file
outfile_name = "file_manifest_"+pre_outfile_name+".tsv"

# report output filename to user
print(outfile_name)


# prompts to user to extract relevant information for locating files to list and files to output
pre_root = input("Please type in directory path to directory containing files to list, followed by the enter key:")
pre_output_location = input("Please type the path to the directory where you want the output to be stored, \
followed by the enter key:")

# remove leading and trailing whitespaces
root = pre_root.strip()
output_location = pre_output_location.strip()
# set final location of output file to user-selected location
output_final_location = os.path.join(output_location, outfile_name)

# insert data-agnostic header
with open(output_final_location, 'a') as f:
    print("fullPath\tfileOriginalName\tfileNewName", file=f)

# for every file within the nominated path, walk through and add to manifest
for path, subdirs, files in os.walk(root):
    for name in files:
        # create joined path
        line = os.path.join(path, name)
        # create list for join iterator
        out_string = [line, name]
        # join fields with tabs to become a .tsv-formatted record
        out = '\t'.join(out_string)
        # append new record to output file
        with open(output_final_location, 'a') as f:
            print(out, file=f)

# report final location of output file to user
print(output_final_location)

# wait 5 seconds
time.sleep(5)

# exit
exit()
