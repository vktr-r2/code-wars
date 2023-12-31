// Create Phone Number

// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// Example:
// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

// The returned format must be correct in order to complete this challenge.
// Don't forget the space after the closing parentheses!

//FIRST IMPLEMENTATION

const createPhoneNumber = (digits) => {
  //Declare variables
  let areaCode = [];
  let phoneNumberFront = [];
  let phoneNumberBack = [];

  //Check if 10 digits were passed
  if (digits.length !== 10) {
    console.log("Please enter 10 digits");
  }
  //If 10 digits passed, slice phone number pieces
  if (digits.length === 10) {
    areaCode = digits.slice(0, 3);
    phoneNumberFront = digits.slice(3, 6);
    phoneNumberBack = digits.slice(6, 10);
  }

  //Transform arrays into strings
  areaCode = areaCode.join('');
  phoneNumberFront = phoneNumberFront.join('');
  phoneNumberBack = phoneNumberBack.join('');

  //Return template literal string
  return `(${areaCode}) ${phoneNumberFront}-${phoneNumberBack}`;
};

//REFACTORED IMPLEMENTATION

// const createPhoneNumber = (digits) => {

//   // Use template literals to slice phone number pieces and transform them into string
//   const phoneNumber = `(${digits.slice(0, 3).join("")}) ${digits.slice(3, 6).join("")}-${digits.slice(6, 10).join("")}`;

//   // Return phoneNumber
//   return phoneNumber;
// };

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
