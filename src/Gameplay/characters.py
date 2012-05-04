from random import randint


def characters_sorted_by_speed(characters):
    return sorted(characters,
                  key=lambda character: randint(0, character.speed) * character.speed,
                  reverse=True)


def fight_between_characters(*characters):
    characters = characters_sorted_by_speed(characters)

    characters[0].attack(characters[-1])
    characters[-1].attack(characters[0])


def any_dead(*characters):
    return any(character.is_dead for character in characters)
