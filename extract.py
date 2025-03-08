#!/usr/bin/env python3

# File name: extract.py
# Author: Zachary Penn Lunte
# Function: Returns the average word length in a given text file

# Import sys 
import sys

# If incorrect number of arguments
if len(sys.argv) != 2:

    # Print a failure message
    print("FAILURE: langid.py must take one argument")

# Otherwise, if correct number of arguments
else:

    # Get the path of the file from arguments  
    path = sys.argv[1]

    # Open the text file 
    f = open(path, 'r')

    # Create an array to hold line averages
    lineavgs = []
  
    # Read each line in the file 
    while True: 
  
        # Get next line from file 
        line = f.readline() 
  
        # End loop after last line
        if not line: 
            break

        # Create an array to contain word letter counts
        counts = []

        # Create a counter to keep track of counted letters
        count = 0

        # For each letter in the line
        for letter in line: 

            # If the letter is not alphabetical
            if not letter.isalpha():

                # And if the count is greater than zero
                if count > 0:

                    # Add the current count to the counts list
                    counts.append(count)
 
                    # Reset the count to be zero
                    count = 0

            # Otherwise, if not a space
            else:

                # Add one to the count value
                count = count + 1

        # If the line had countable letters
        if len(counts) > 0:
    
            # Calculate the average of the counts
            lineavg = sum(counts) / len(counts)

            # Add the line average to the list of line averages
            lineavgs.append(lineavg)

    # If there were lines with countable letters
    if len(lineavgs) > 0:
    
        # Calculate the total average
        totalavg = sum(lineavgs) / len(lineavgs)

        # Print the total average
        print(totalavg)

    # Otherwise, if no lines with countable letters
    else:
    
        # No content
        print("No countable content")
  
f.close() 

