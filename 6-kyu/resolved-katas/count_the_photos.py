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

return the total number of photos.
it should return an integer
"""

# FUNCTION WORKS, BUT INEFFICIENT
# O(N^2) complexity, did not pass the kata quick enough
# Function using nested loops to iterate over string many times, would be very slow with large string arguments

# def count_photos(road):
#     tally = 0                                           # tally to be returned
#     i = 0                                               # i to increment each iteration
#     limit = len(road) - 1                               # limit to end loop set to length - 1

#     while i <= limit:
#         if road[i] == ">":                              # if char at index i is ">"
#             tally += road.count(".", i)                 # increase the tally by the number of "." found between index i and end of string (end arg not manditory, assumed by count() function to be end of string)

#         if road[i] == "<":                              # if char at index i is "<"
#             tally += road.count(".", 0,  i)             # increase the tally by the number of "." between start of string and road[i]
          
#         i += 1                                          # increment i and loop again

#     return tally


# FUNCTION WORKS EFFICIENTLY
# O(n) complexity
# This function only needs to iterate through string once

def count_photos(road):
    total_cameras = road.count('.')                        # Determine how many cameras string has
    cameras_seen = 0                                       # Var will increment as we iterate through the string character by character
    photos_taken = 0                                       # Return value

    for char in road:                                      # Start first and only interation through string
        if char == '>':                                    # If char is car going right: 
            photos_taken += total_cameras - cameras_seen        # Add to photos_taken the number of total camera minus the cameras already seen/passed
        elif char == '.':                                  # If char is a camera:
            cameras_seen += 1                                   # Increment cameras_seen
        elif char == '<':                                  # If char is a camera going left:
            photos_taken += cameras_seen                        # Add to photos_taken the number of cameras seen/passed thus far.

    return photos_taken

print(count_photos(".><.>>.<<"))
print(count_photos(">.<."))
print(count_photos(".>>"))
print(count_photos(">>."))