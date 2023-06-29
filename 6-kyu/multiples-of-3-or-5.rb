# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(num)
  #Declare array to store numbers to be summed
  multiples = []

  #Setup range from 1 to num-1 to be checked
  1.upto(num - 1) do |i|
    #Conditional to check if current number is multiple of 3 or 5
    if i % 3 == 0 || i % 5 == 0
      #If true, push number into multiples array
      multiples.push(i)
    end
  end
  #Return sum of multiples array using reduce
  multiples.reduce(0) { |sum, num| sum + num }
end

puts solution(10)