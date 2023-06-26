# //REFACTORED IMPLEMENTATION

# const race = (tortoiseA, tortoiseB, lead) => {
#   //If tortoiseA is the faster tortoise return null and exit function
#   if (tortoiseA > tortoiseB) { return null; }
  
#   //Calculate totalSeconds based on lead and difference in tortoise speeds
#   const totalSeconds = Math.floor(lead / (tortoiseB - tortoiseA) * 3600);
#   //Calculate hours, mins, secs
#   const hours = Math.floor(totalSeconds / 3600);
#   const mins = Math.floor((totalSeconds - hours * 3600) / 60);
#   const secs = totalSeconds - hours * 3600 - mins * 60;
  
#   //Return result
#   return [hours, mins, secs];
# };

def race(tortoise_a, tortoise_b, lead)

  if tortoise_a > tortoise_b
    return nil
  end

  total_seconds = (lead * 3600 / (tortoise_b - tortoise_a)).floor
  hours = (total_seconds / 3600).floor
  mins = ((total_seconds - hours * 3600) / 60).floor
  secs = total_seconds - hours * 3600 - mins * 60

  [hours, mins, secs]

end

# TEST EXPECTED RESULT: 0h, 17m, 4 sec

puts race(720, 850, 37)

