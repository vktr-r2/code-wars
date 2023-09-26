"""
// Create Phone Number

// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// Example:
// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

// The returned format must be correct in order to complete this challenge.
// Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
  area_code = []
  phone_number_front = []
  phone_number_back = []

  if len(n) != 10:
    print("Please enter 10 digits")
  
  else:
    area_code = n[slice(0, 3)]
    phone_number_front = n[slice(3, 6)]
    phone_number_back = n[slice(6, 10)]

  area_code = ''.join(map(str, area_code))
  phone_number_front = ''.join(map(str, phone_number_front))
  phone_number_back = ''.join(map(str, phone_number_back))

  return f"({area_code}) {phone_number_front}-{phone_number_back}"