=begin

CODE WARS -> Reversing Words in a String
https://www.codewars.com/kata/57a55c8b72292d057b000594/


You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"

=end


# My resolution -> split the string into an array, reverse the array, join the array back into a string

def reverse(string)
    result = string.split(" ")
    result.reverse!
    result.join(" ")
end


=begin

# Chain method resolution -> same process, but I believe harder to read

def reverse(string)
  string.split.reverse.join(" ")
end

=end