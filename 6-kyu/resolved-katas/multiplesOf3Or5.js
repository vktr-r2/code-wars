// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 , 9. The sum of these multiples is 23.

// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

// Note: If the number is a multiple of both 3 and 5, only count it once.

const solution = (num) => {
  //Check that arg passed is legitimate
  if (num < 0) {
    return 0;
  }

  //Declare sum variable
  let sum = 0;

  //For loop to iterate through range of numbers
  for (i = 0; i < num; i++) {
    //Check if current value of i is multiple of 3 or 5
    if (i % 3 === 0 || i % 5 === 0) {
      //If true, add i to current sum value
      sum += i;
    }
  }
  return sum;
};

console.log(solution(10));
