// Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

// When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

// More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

// The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

// If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for Kotlin or "-1 -1 -1" for others.

// Examples:
// (form of the result depends on the language)

// race(720, 850, 70) => [0, 32, 18] or "0 32 18"
// race(80, 91, 37)   => [3, 21, 49] or "3 21 49"
// Note:
// See other examples in "Your test cases".

// In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

// ** Hints for people who don't know how to convert to hours, minutes, seconds:

// Tortoises don't care about fractions of seconds
// Think of calculation by hand using only integers (in your code use or simulate integer division)
// or Google: "convert decimal time to hours minutes seconds"

const race = (tortoiseA, tortoiseB, lead) => {

  //If tortoiseA is the faster tortoise return null and exit function
  if (tortoiseA > tortoiseB) {
    return null;
  }

  //Determine feet per second speeds
  let tortAPerSec = tortoiseA / 3600;
  let tortBPerSec = tortoiseB / 3600;
  //Start tortoiseA at lead distance, and tortoiseB at 0
  let tortoiseADistance = lead;
  let tortoiseBDistance = 0;
  //Start timer at -1, so first loop begins timer at 0 to start race
  let timer = -1;

  //While loop checks distance of each tortoise after each second
  while (tortoiseADistance > tortoiseBDistance) {
    //Increment tortoises by their feet per second speed
    tortoiseADistance += tortAPerSec;
    tortoiseBDistance += tortBPerSec;
    //Increment timer by 1 second
    timer++;
  }

  return convertSecondsToTime(timer);
};

//Helper function assists in formatting timer from seconds to [hours, minutes, seconds]
function convertSecondsToTime(totalSeconds) {
  var hours = Math.floor(totalSeconds / 3600); // 1 hour = 3600 seconds
  var minutes = Math.floor((totalSeconds % 3600) / 60); // 1 minute = 60 seconds
  var seconds = Math.floor(totalSeconds % 60);

  return [hours, minutes, seconds];
}

//TEST EXPECTED : 0h, 17m, 4 sec
console.log(race(720, 850, 37));