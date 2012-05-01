from random import randint


class Item(object):
    def __init__(self, name, uses):
        self.name = name
        self._uses = uses

    def use(self, amount=1):
        self._uses -= amount

    @property
    def uses_left(self):
        return self._uses


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


class ItemStash(object):
    def __init__(self, size):
        self.size = size
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def drop_item(self, item):
        if item in self._items:
            self._items.remove(item)

    def next(self):
        pass

    def __iter__(self):
        for item in self._items[:]:
            yield item
        raise StopIteration


def test_weapon():
    pass

if __name__ == '__main__':
    test_weapon()
