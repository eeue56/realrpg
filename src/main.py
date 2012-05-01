from characters import PlayerCharacter, Character
from Inventory.weapons import Weapon
from Gameplay.characters import *


def test_attacking():
    every_round = []
    n = 1000

    for x in xrange(n):
        player = PlayerCharacter("Noah", 100, 12, 20, 50)
        player.pickup_item(Weapon("Bronze sword", 12, 10))

        hostile = Character("Jim", 100, 12, 5, 100)
        hostile.pickup_item(Weapon("Sharp flaming knife", 5, 18))

        rounds = 0
        while True:
            rounds += 1

            fight_between_characters(player, hostile)

            if any_dead(player, hostile):
                break

            player.drop_worthless()
            hostile.drop_worthless()
        every_round.append(rounds)

    """print '{} : {}'.format(player.name, player.health)
    print '{} : {}'.format(hostile.name, hostile.health)
    print 'Winner : {}'.format(player.name if player.health > hostile.health else hostile.name)
    print 'Rounds: {}'.format(rounds)"""

    print sum(every_round) / (n + 0.0)


def test_item_stash():
    item_stash = ItemStash(1)
    item_stash[1] = 2
    print item_stash[1]


if __name__ == '__main__':
    test_attacking()
