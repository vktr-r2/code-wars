"""
https://www.codewars.com/kata/5863f1c8b359c4dd4e000001

DESCRIPTION:
You've been going to the gym for some time now and recently you started taking
care of your nutrition as well. You want to gain some weight but who wants to
bother counting calories every day. It said somewhere that protein is the
foundation of building muscle, so let's try to calculate the total amount of
calories and proteins we take in.

Task:
Given an array of meals where each element is a string in the form
'300g turkey, 300g potatoes, 100g cucumber' find out how many proteins and
calories you consumed. You like to keep things simple so all values will be
expressed in grams. In case you didn't know every gram of protein and
carbohydrate has 4 calories, while 1 gram of fat provides 9 calories.
An object food (in Ruby $food ) is preloaded for you that contains the
information about the given food per 100 grams:

Round your results to 2 decimal places and return a string in the form
"Total proteins: n grams, Total calories: n".
Delete all trailing zeros on every float and remove trailing point if
the result is an integer. Note: No invalid input testing.

"""

food = {
  "chicken": [20, 5, 10],   # 20g protein, 5 grams carbs and 10 grams of fat.
  "eggs": [10, 5, 15],      # protein:10g , carbs:5g , fats: 15g
  "salmon": [27, 0, 10],
  "beans": [8, 25, 0],
  "bananas": [1, 23, 0]
}


def bulk(arr):

    # Variables to track nutritional metrics
    protein = 0
    carbs = 0
    fat = 0
    calories = 0

    # OUTER LOOP
    for meal in arr:

        # Split each meal string into list of ingredients strings
        ingredients = meal.split(',')

        # INNER LOOP
        for ingred in ingredients:

            # Remove whitespaces with strip
            # Split ingredient string by ' '
            # Assign first split to weight, second split to name
            weight, name = ingred.strip().split(' ', 1)

            # Take weight string, remove last character 'g' and convert to int
            # Divide int by 100 (since nutrition will be measured per 100gs)
            weight = int(weight[:-1]) / 100

            if name in food:
                nutrient_values = food[name]
                protein += nutrient_values[0] * weight
                carbs += nutrient_values[1] * weight
                fat += nutrient_values[2] * weight

    # calculate calories
    calories += ((protein + carbs) * 4) + (fat * 9)

    # Use format function with '.7g' flag to return int/float 7 digits or less
    return (f"Total proteins: {format(protein, '.7g')} grams, "
            f"Total calories: {format(calories, '.7g')}")
