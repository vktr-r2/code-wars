"""
DESCRIPTION:
In a string we describe a road. There are cars that move to the right and we denote
them with ">" and cars that move to the left and we denote them with "<". 
There are also cameras that are indicated by: " . ". A camera takes a photo of a car 
if it moves to the direction of the camera.

Task
Your task is to write a function such that, for the input string that represents a 
road as described, returns the total number of photos that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests.

Examples
For ">>." -> 2 photos were taken
For ".>>" -> 0 photos were taken
For ">.<." -> 3 photos were taken
For ".><.>>.<<" -> 11 photos were taken
"""

# return the total number of photos.
# it should return an integer

def count_photos(road):
    tally = 0                                           # tally to be returned
    i = 0                                               # i to increment each iteration
    limit = len(road) - 1                               # limit to end loop set to length - 1

    while i <= limit:
        if road[i] == ">":                              # if char at index i is ">"
            tally += road.count(".", i)                 # increase the tally by the number of "." found between index i and end of string (end arg not manditory, assumed by count() function to be end of string)

        if road[i] == "<":                              # if char at index i is "<"
            tally += road.count(".", 0,  i)             # increase the tally by the number of "." between start of string and road[i]
          
        i += 1                                          # increment i and loop again

    return tally

print(count_photos(".><.>>.<<"))
print(count_photos(">.<."))
print(count_photos(".>>"))
print(count_photos(">>."))