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

food = {
  "chicken": [20, 5, 10], # 20g protein, 5 grams carbs and 10 grams of fat.
  "eggs": [10, 5, 15],    # protein:10g , carbs:5g , fats: 15g
  "salmon": [27, 0, 10],
  "beans": [8, 25, 0],
  "bananas": [1, 23, 0],
  ...
  ...
}

Round your results to 2 decimal places and return a string in the form
"Total proteins: n grams, Total calories: n".
Delete all trailing zeros on every float and remove trailing point if
the result is an integer. Note: No invalid input testing.

"""


def daily_diet_string_to_dict(arr):

    daily_food = {}

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

            # Check current value for daily_food[name] using .get
            # If key doesn't exist return 0
            # Take weight string, remove last character 'g' and convert to int
            # Divide int by 100 (since nutrition will be measured per 100gs)
            # Add new weight value to value returned by .get() method
            daily_food[name] = daily_food.get(name, 0) + int(weight[:-1]) / 100

    return daily_food


a = [
    "175g pork, 100g eggs, 25g chocolate",
    "175g goose, 200g cheddar, 250g milk, 300g kiwi",
    "100g catfish, 250g eggs, 125g parmesan, 75g chocolate, 125g watermelon",
    "125g chicken, 25g beans, 50g lemons"
    ]

daily_diet_string_to_dict(a)
