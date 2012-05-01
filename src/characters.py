from items import *

class Character(object):
    def __init__(self, name, health, strength, speed, accuracy):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.accuracy = accuracy
        self.item_stash = ItemStash(strength)

    def heal(self, healing):
    	'''Add healing to health.'''
        self.health += healing

    def take_damage(self, damage):
    	'''Take damage away from health.'''
        self.health -= damage

    @property
    def is_dead(self):
        '''Return True if dead, False otherwise.'''
        return self.health <= 0
    

    def pickup_item(self, item):
        self.item_stash.add_item(item)

    def drop_item(self, item):
        self.item_stash.drop_item(item)

    def drop_worthless(self):
        for item in self.item_stash:
            if item.uses_left <= 0:
                self.item_stash.drop_item(item)

    def strongest_weapon(self):
        strongest_weapon = Weapon("Fists", 1, self.strength / 2)

        for item in self.item_stash:
            if isinstance(item, Weapon) and item.strength > strongest_weapon.strength:
                strongest_weapon = item

        return strongest_weapon

    def attack(self, defender):
        self.strongest_weapon().attack(self, defender)
        
class PlayerCharacter(Character):
    def __init__(self, *args, **kwargs):
        Character.__init__(self, *args, **kwargs)


def characters_sorted_by_speed(characters):
    return sorted(characters, key=lambda character: randint(0, character.speed) * character.speed, reverse=True)

def fight_between_characters(*characters):
    characters = characters_sorted_by_speed(characters)

    characters[0].attack(characters[-1])
    characters[-1].attack(characters[0])

def any_dead(*characters):
    return any(character.is_dead for character in characters)
