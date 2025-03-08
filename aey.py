#! /usr/bin/env python3

import os
from time import sleep
from math import floor, ceil, sqrt
from random import randint

# Set the spiral size
spiral_size = 729

# Set the number of frames per color
color_frames = 2

# Set the wait time between each frame
wait_time = 0.01

# Create a list of letters to use
letter_list = ['a', 'e', 'y', 'A', 'E', 'Y']

# Get the dimensions of the terminal
terminal_dimensions = os.get_terminal_size()

# Get the total number of character spaces in the terminal
total_character_space = int(terminal_dimensions[0])*int(terminal_dimensions[1])

# Create a string of so many spaces to represent the character space
s = " "*int(total_character_space)

# Get the width of the terminal
w = int(terminal_dimensions[0])

# Get the height of the terminal
h = int(terminal_dimensions[1])

# Set the starting position of the spiral (should be the center)
position = ((((ceil(h/2))-1)*w)+(ceil(w/2)))

# Create the aey strings
aey1 = "     QQQQ      "+" "*(w-15)
aey2 = "    Q    Q     "+" "*(w-15)
aey3 = "    Q    Q     "+" "*(w-15)
aey4 = "     QQQQ Q    "+" "*(w-15)
aey5 = "               "+" "*(w-15)
aey6 = "     QQQQ      "+" "*(w-15)
aey7 = "    Q    Q     "+" "*(w-15)
aey8 = "    QQQQQQ     "+" "*(w-15)
aey9 = "    Q          "+" "*(w-15)
aey10 = "     QQQQ      "+" "*(w-15)
aey11 = "               "+" "*(w-15)
aey12 = "    Q    Q     "+" "*(w-15)
aey13 = "    Q    Q     "+" "*(w-15)
aey14 = "     QQQQ      "+" "*(w-15)
aey15 = "         Q     "+" "*(w-15)
aey16 = "     QQQQ      "

# Create the full aey string
aey = aey1+aey2+aey3+aey4+aey5+aey6+aey7+aey8+aey9+aey10+aey11+aey12+aey13+aey14+aey15+aey16

# Get the aey string position based on center position
aey_position = position-(floor(len(aey)/2))+(ceil(w/2))

# Insert the aey string into the center of the character space
aey_s = s[:aey_position] + aey + s[aey_position+len(aey):]

# Create list of possible color values
colors = [0, 1, 4, 7, 27, 22, 30, 31, 32, 33, 34, 35, 36, 37, 38, 48, 51, 52, 53, 54, 55]

# Generate a random starting color
random_color_index = randint(0, len(colors)-1)

# For the total size of the spiral
for n in range(spiral_size):

    # Generate a random new character from the letter list
    new_character = letter_list[randint(0,100)%6]

    # If printing the first frame
    if n == 0:

        # If current position is in aey space
        if aey_s[position] == 'Q':
   
            # Replace the current position with a space
            s = s[:position] + " " + s[position+1:]

        # Else if current position is not in aey space
        else:
            
            # Replace the current position with the new character
            s = s[:position] + new_character + s[position+1:] 

    # Else if printing any later frame
    else:
    
        # Calculate the add to give the current position based on previous position
        a = (-1)**(floor(sqrt(n-1))%2)
        b = floor((n-1)/(ceil(sqrt(n))))
        c = ceil(sqrt(n))
        d = (((((b+c)%2)+1)%2)*w)
        e = ((b+c)%2)+d
        add = a*e

        # Calculate the current position
        position = position + add

        # If current position is in aey space
        if aey_s[position] == 'Q':
   
            # Replace the current position with a space
            s = s[:position] + " " + s[position+1:]

        # Else if current position is not in aey space
        else:
            
            # Replace the current position with the new character
            s = s[:position] + new_character + s[position+1:]

    # If so many number of color frames have passed
    if n % color_frames == 0:
        
        # Update the color to a new random color 
        random_color_index = randint(0, len(colors)-1)

    # If this is the last frame
    if n == (spiral_size - 1):

        # Reset the color to the original terminal color
        random_color_index = 0

    # Print the current space with the current random color
    random_color_value = colors[random_color_index]
    random_color_string = "\033["+str(random_color_value)+"m" 
    print(random_color_string+s) 

    # Wait 0.1 seconds between each print cycle
    sleep(wait_time)

print("\033[0m")
