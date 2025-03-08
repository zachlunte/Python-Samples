#!/usr/bin/env python3

# NOTE: This script should be launched from a directory containing
#       both the unsorted JPG files and associated export XML file 
#       from the Digital Bodleian.

# Import regular expressions and operating system
import re, os

# Set identifiers
start = "<Image>"
end = "</Image>"

# Create a tag
tag = "page"

# Create a counter
count = 1

# Open the file
f = open('iNQUIRE_export.xml', 'r')

# For each line
for line in f:

    # If line contains phrase "<Image>...</Image>"
    if start in line and ".jpg" in line:

        # Get the file name
        file_name = re.search('%s(.*)%s' % (start,end), line).group(1)

        os.rename(file_name, tag+str(count)+".jpg")

        # Increment the counter
        count += 1

# Close the file
f.closed
