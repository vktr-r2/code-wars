"""
https://www.codewars.com/kata/5882b052bdeafec15e0000e6/train/python

You're modelling the interaction between a large number of quarks and have decided to create a Quark class so you can generate your own quark objects.

Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.

Your task
Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.

Example
>>> q1 = Quark("red", "up")
>>> q1.color
"red"
>>> q1.flavor
"up"
>>> q2 = Quark("blue", "strange")
>>> q2.color
"blue"
>>> q2.baryon_number
0.3333333333333333
>>> q1.interact(q2)
>>> q1.color
"blue"
>>> q2.color
"red"

"""

class Quark:

    def __init__(self, color, flavor):                                                      # Initialize function
        valid_colors = ("red", "blue", "green")                                             # Define tuples storing acceptable property values
        valid_flavors=("up", "down", "strange", "charm", "top", "bottom")

        if color not in valid_colors or flavor not in valid_flavors:                        # Check that Quark instance initialized with proper values.  If true...
            raise ValueError("Invalid color or flavor for Quark.")

            self.color = color                                                              # Define values based on arguments passed
            self.flavor = flavor
            self.baryon_number = 1 / 3

    def interact(self, quark2):                                                             # Interact function swaps color values between two quark objects
        temp_color_var = quark2.color
        quark2.color = self.color
        self.color = temp_color_var


example_quark = Quark("blue", "up")
print(example_quark)

invalid_quark = Quark("pink", "random")
print(invalid_quark)
print(invalid_quark.color)
print(invalid_quark.flavor)
print(invalid_quark.baryon_number)
