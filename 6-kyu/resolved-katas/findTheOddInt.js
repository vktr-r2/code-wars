/*

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

*/
// MY SOLUTION
function findOdd(A) {
  // object to count each numbers occurrance
  const counter = {};

  // count how many times each element occurs in array
  A.forEach((ele) => {
    if (counter[ele]) {
      counter[ele] += 1;
    } else {
      counter[ele] = 1;
    }
  });

  // iterate through counter obj and return Number(key) that is odd
  for (key in counter) {
    if (counter[key] % 2 !== 0) {
      return Number(key);
    }
  }
}


/* MORE EFFICIENT SOLUTION

The code defines a function findOdd that takes an array xs as its argument. 
The function uses the reduce method to apply the bitwise XOR (^) operation 
on all elements of the array.

In the context of an array containing integers, the XOR operation 
will essentially cancel out numbers that appear an even number of 
times, leaving only the number that appears an odd number of times. 
This is because XORing a number with itself results in 0, and XORing 
any number with 0 results in the number itself.

*/

const findOdd = (A) => A.reduce((a, b) => a ^ b);


