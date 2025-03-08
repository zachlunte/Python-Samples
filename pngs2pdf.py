#!/usr/bin/env python3

import os, img2pdf

# Create the PDF file name
pdf_title = "result.pdf"

# Determine the front of the string
front = "page"

# Get the contents of the current directory and sort them
contents = os.listdir(os.getcwd())

pngcontents = []
for c in contents:
    if c.endswith('.png'):
        pngcontents.append(c.strip(front).strip(".png"))
pngcontents.sort(key=int)

finalcontents = []
for c in pngcontents:
    content = front + c + ".png"
    finalcontents.append(content)

# Write the image files to a PDF
with open(pdf_title, "wb") as f:
    f.write(img2pdf.convert([c for c in finalcontents]))
