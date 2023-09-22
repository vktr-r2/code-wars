/*

Write a function that given an array of numbers >= 0, 
will arrange them such that they form the biggest number.

For example:

[1, 2, 3] --> "321" (3-2-1)
[3, 30, 34, 5, 9] --> "9534330" (9-5-34-3-30)
The results will be large so make sure to return a string.

*/

/*
NOTES

- .every() method tests whether all elements in array pass the test implemented by provided callback
- .map(String) method converts all numbers to a string for lexigraphical comparison
- localeCompare() method of String values returns a number indicating whether this string comes before, or after, or is the same as the given string in sort order.

*/


// MY SOLUTION
function biggest(nums) {

  // If all numbers are zero, return '0'
  if (nums.every(num => num === 0)) {
    return '0';
  }

  // Convert numbers to strings for easy comparison
  const strNums = nums.map(String);
  
  // Custom sort the array
  strNums.sort((a, b) => {
    const ab = a + b;
    const ba = b + a;

    // localeCompare method compares strings lexicographically
    return ba.localeCompare(ab);
  });

  // Join the sorted strings to form the biggest number and return it
  return strNums.join('');
};