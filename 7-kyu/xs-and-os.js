/*

Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

*/

/*  MY ORIGINAL SOLUTION

function XO(str) {
  let x = 0;
  let o = 0;
  str = str.toUpperCase();

  for (let char of str) {
    if (char === "X") {
      x += 1;
    }
    if (char === "O") {
      o += 1;
    }
  }
  return x === o;
}
*/

// BETTER SOLUTION
function XO(str) {

  // .match function returns ARRAY of matches
  // /x/gi is regex > looks for 'x's, g is global flag (checks whole string), i is case-insensitive flag
  let x = str.match(/x/gi);
  let o = str.match(/o/gi);

  // Check if x length is equal to o length
  return (x && x.length) === (o && o.length);
}
