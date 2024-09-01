=begin

CODE WARS -> Remove duplicates from list
https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

VERY IMPORTANT:  The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
=end



=begin

# Out of the box solution -> return uniq method

def distinct(seq)
    seq.uniq
end

=end 



# My solution -> Iterate through array items, if item doesn't exist as key in hash then add the item also to the result array

def distinct(seq)
    seen = {}
    result = []
  
    seq.each do |item| # Iterate argument array
      unless seen[item]  # If item DOESN'T exist as key in our hash
        seen[item] = true   # Add the item as a key, value = true
        result << item      # Add it to the result array
      end
    end
  
    result
end