#!/usr/bin/env python3

import heapq

# FILE: magic.py
# DESCRIPTION: Takes some positive integer n and calculates the total number of possible n-order magic squares.
# AUTHOR: Zachary Penn Lunte

# Returns the magic number associated with n
def magicNum(n):
    return (n*((n*n)+1))//2

# Increments line of ints in desired fashion based on n
def incrementLine(l, n):
    result = l
    max = n*n
    while True:
        frontPart = list(result)
        backPart = []
        if frontPart[-1] != max:
            frontPart[-1] += 1
            result = frontPart
            if len(result) == len(set(result)):
                return result
        while frontPart[-1] == max:
            backPart.append(1)
            frontPart.pop(-1)
        frontPart[-1] += 1
        result = frontPart + backPart
        if len(result) == len(set(result)):
            return result

def getLines(n):
    result = []
    magNum = magicNum(n)
    curLine = []
    lastLine = []
    for i in range(n+1)[1:]:
        curLine.append(i)
    for i in range(n):
        lastLine.append((n*n)-i)
    while curLine != lastLine:
        curLine = incrementLine(curLine, n)
        if sum(curLine) == magNum:
            result.append(list(curLine))
    return result


# START: start placing numbers from available set down in order from smallest to largest until
# we reach a dead end.

# HITTING A DEAD END: if at any point there are x remaining spots to be filled, and the 
# sum of the currently placed numbers plus the x largest available numbers is less than the 
# magic number, we've reached a dead end. Once we hit a dead end, we need to increment.

# INCREMENTING: if we reach a dead end, we increment the end number until we are not at a dead end.
# To increment the end number, swap it with the smallest larger non-placed number. If there is no 
# larger non-placed number, add the number immediately to the left to the available set, then swap the 
# end number with the smallest number in the available set, and then repeat the process on the number 
# to the left. 

# ONE SLOT LEFT: if at any point, there is only one remaining place, do the following. 1) Caclulate 
# the sum of the currently placed nums. 2) Let x = magicNum - curSum. 3) If x is not a number in the 
# available set, we are at another dead end, and need to increment. 4) Otherwise, add the number x 
# into the last slot, store the line of ints as a success in the success collection, then increment.

# Returns the smallest element in the array a
def getSmallest(a):
    if len(a) == 0:
        return None
    else:
        return min(a)

# Returns the smallest element in the array a larger than x
def getSmallestLarger(x, a):
    if len(a) == 0:
        return None
    else:
        sl = max(a)
        if sl <= x:
            return None
        else:        
            for e in a:
                if e > x and e < sl:
                    sl = e
        return sl

# Returns True if at a dead end
def atDeadEnd(placed, available, n, magNum):
    numPlaced = len(placed)
    numRemaining = n - numPlaced
    curPlaSum = sum(placed)
    maxRemSum = sum(heapq.nlargest(numRemaining, available))
    return (curPlaSum + maxRemSum) < magNum

# Returns True if last remaining slot can be filled successfully
def canSucceed(placed, available, magNum):
    curPlaSum = sum(placed)
    remainder = magNum - curPlaSum
    return remainder in available

# Returns the succeeding final number
def getSucceeder(placed, available, magnum):
    curPlaSum = sum(placed)
    remainder = magNum - curPlaSum
    return remainder

def incrementPlacedSet(placed, available, n):
 
    if len(placed) < 1:
        return

    # Calculate max number for a slot
    maxVal = n*n

    # Pop last element
    last = placed.pop()

    # If there is a smallest element larger than last in available
    sl = getSmallestLarger(last, available)
    if sl != None:

        # Add it to placed, replacing last
        placed.append(sl)

        # Remove it from the available set
        available.remove(sl)

        # Then add replaced last into available set
        available.append(last)

    # If there is no element larger than last in available
    else:
         
        # Add last to available
        available.append(last)

        # Call increment on placed with last now removed
        incrementPlacedSet(placed, available, n)

    return

def buildLines(n):

    # Calculate magic number
    magNum = magicNum(n)

    # Storage space for successful lines
    successSet = []

    # Initialize currently placed set to be empty
    placedSet = []

    # Initialize available set to contain each number in range
    availableSet = []
    for i in range((n*n)+1)[1:]:
        availableSet.append(i)

    # Start by moving smallest value in available set to placed set 
    placedSet.append(min(availableSet))
    availableSet = availableSet[1:]

    # While num placed is greater than zero
    while len(placedSet) > 0:

        # Calculate number of slots remaining
        numRemaining = n - len(placedSet)
        
        # Check if at a dead end
        if atDeadEnd(placedSet, availableSet, n, magNum):

            # If so, increment last placed value
            incrementPlacedSet(placedSet, availableSet, n)

        # If not at dead end, and more than one space left
        elif numRemaining > 1:

            # Place at next space the smallest value in the available set
            placedSet.append(min(availableSet))

        # If not at dead end, and only one space left
        else:

            # Check if can succeed with last place
            if canSucceed(placedSet, availableSet, magNum):

                # If so, add success to the success set
                successSet.append(list(placedSet)+[getSucceeder(placedSet, availableSet, magNum)])

            # Increment the last placed value
            incrementPlacedSet(placedSet, availableSet, n)
   
    return successSet

# placed = [11,24,7,25]
# available = [1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23]
# n = 5
# print("Pre-increment: {}\t{}".format(placed, available))
# incrementPlacedSet(placed, available, n)
# print("Post-increment: {}\t{}".format(placed, available))

print("\n==== MAGIC SQUARES ENUMERATOR ====\n")
n = int(input(">>> Enter an order: "))

print("\nCalculating {}-order magic number...".format(n))
magNum = magicNum(n)

print("Calculating all possible {}-order lines...".format(n))
lines = getLines(n)

print("\nThe {}-order magic number is {}.".format(n, magNum))
print("There are {} possible {}-order lines.".format(len(lines), n))

print("\n**** PROGRAM TERMINATED ****\n")
