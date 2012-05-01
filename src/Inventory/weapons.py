from random import randint
from items import Item


class Weapon(Item):
    def __init__(self, name,  uses, strength):
        Item.__init__(self, name, uses)
        self.strength = strength

    def weaken_strength(self, amount):
        self.strength -= amount

    def attack(self, attacker, defender):

        if randint(0, 10000) > defender.accuracy:
            defence_factor = randint(0, defender.strength) * defender.strength
        else:
            defence_factor = defender.strength

        if randint(0, 10000) > attacker.accuracy:
            attack_factor = self.strength * self.uses_left
        else:
            attack_factor = 1

        if defence_factor >= attack_factor:
            self.weaken_strength(defence_factor / attack_factor)
        else:
            defender.take_damage(attack_factor - defence_factor)

        self.use()

    def __repr__(self):
        return '{}. Uses: {}, strength: {}'.format(self.name, self.uses_left, self.strength)