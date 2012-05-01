from items import Item


class Potion(Item):
    def __init__(self, name, strength):
        Item.__init__(self, name, 1)
        self.strength = strength

    def use(self):
        self._uses = 0


class HealingPotion(Potion):
    def __init__(self, name, strength):
        Potion.__init__(self, name, strength)

    def take_potion(self, character):
        self.use()
        character.heal((self.strength ** 2) / character.health)


class DamagingPotion(Potion):
    def __init__(self, name, strength):
        Potion.__init__(self, name, strength)

    def take_potion(self, thrower, character):
        self.use()
        character.take_damage((self.strength ** 2) + thrower.stength)
        