"""
https://www.codewars.com/kata/517b0f33cd023d848d000001/train/python

Something is wrong with our Warrior class. The strike method does not work correctly. The following shows an example of this code being used:

ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
Can you figure out what is wrong?
"""


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        enemy.health = max([-1, enemy.health-(swings*10)])


ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)

print(ninja.health)
