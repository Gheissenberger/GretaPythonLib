"""
Let's have fun with dictionaries and She-Ra!
Discusses vanilla dicts, how to create them, add to them and different ways to iterate through them.
Dictionary comprehensions are covered.
Also some ways to handle lookup of items that might not be in the dict: get() and defaultdict!

@author Greta Heissenberger
@date 2/14/22
"""
from collections import defaultdict
from random import randrange


class Weapon:
    """
    A class representing a weapon
    """

    def __init__(self, name: str = "Swordy McSword"):
        self.name = name
        self.attack_count = 0

    def attack(self, number: int) -> None:
        """
        Attack with your weapon
        :param number: The number of times to attack
        """
        print(f"{self.name} attacks: {('pew' * number)}")
        self.attack_count = self.attack_count + number


def main():
    """
    Let's have fun with dictionaries and She-Ra!
    """

    # OK let's start off with the basics.
    # Here's a vanilla dict
    glimmer_dict = {"location": "Bright Moon", "power_source": "Moonstone"}
    # and a different way to do a vanilla dict.
    frosta_dict = dict()
    frosta_dict["location"] = "Kingdom of the Snows"
    frosta_dict["power_source"] = "Fractal Flake"

    # You can just print a dict and it looks great. You do have to append them to strings
    print("Print Test!")
    print(f"glimmer_dict: " + str(glimmer_dict))
    print(f"frosta_dict: ")
    print(frosta_dict)

    # So, if you want to look up where a princess lives, it is pretty simple:
    print(f"Glimmer's location: {glimmer_dict['location']}")

    # Of course, you can make a dict of dicts.
    # There are no hashmaps or hashtables in Python, but you can use a dict.
    elemental_princesses = {"Glimmer": glimmer_dict, "Frosta": frosta_dict}

    # You can access the data in a multidimensional dict by just stacking up the square brackets
    print(f"Frosta's location: {elemental_princesses['Frosta']['location']}")

    # It's also easy to tell what's in a dict
    if "Glimmer" in elemental_princesses:
        print("Glimmer is an elemental princess")
    else:
        print("Glimmer is not an elemental princess")

    if "Catra" in elemental_princesses:
        print("Catra is an elemental princess")
    else:
        print("Catra is not an elemental princess")

    # Iterating through dicts is kinda weird, you only get the name back
    print("For Loop Example:")
    for name in elemental_princesses:
        current_princess_name = name
        # But that's ok, you can look up the item from the name
        current_princess_dict = elemental_princesses[name]
        print(f"The power source for {name} is {current_princess_dict['power_source']}")

    # But if you want all the items even more easily, you can get them, just use .items
    print("Items Example:")
    locations = {
        "Crimson Waste": ["Huntara", "Tung Lashor"],
        "Beast Island": ["Micah", "Entrapta"],
        "Mystacor": ["Castaspella"],
    }

    for location, resident_list in locations.items():
        print(f"The residents in {location} is (are) {resident_list}.")

    # You can also just get a key list if you want
    location_list = locations.keys()
    location_string = " ".join(location_list)
    print("The locations in She-Ra are: " + location_string)

    # Okay here's a cool thing you may not know:
    # So if you ask for a key that's not in the dict it throws an error:
    try:
        print("Looking for Krytis")
        melog_home = locations["Krytis"]
    except Exception as e:
        print(f"Oops, caught a {type(e).__name__}")

    # If you want to return a default value in case something is missing use get
    try:
        melog_home = locations.get("Krytis", "Unknown")
        print(f"Melog's home is {melog_home}")
    except Exception as e:
        print(f"Oops, caught a {type(e).__name__}")

    # Ok, but what if I actually want to make the thing in the dict if it is missing?
    # Use a default dict!
    weapons = defaultdict(lambda: Weapon())
    weapons["She-Ra"] = Weapon(name="Sword of Protection")
    weapons["Bow"] = Weapon(name="Bow")

    army = ["She-Ra", "Bow", "Soldier1", "Soldier2", "Soldier3", "Soldier4"]

    for combatant in army:
        print(f"Get 'em {combatant}!")
        randrange(0, 101, 2)
        weapons[combatant].attack(randrange(1, 4))

    # Comprehensions are a cool python thing: if you need to make a collection from another collection, you can easily.
    sea_hawks_favorite_sea_shanties_list = [
        "What should we do with a drunken sailor",
        "The Sea Hawk",
    ]
    brave_acts_by_sea_hawk = {
        "battle of mermista won": {"ships_destroyed": 60, "own_ship_set_on_fire": True},
        "bar brawl won": {"ships_destroyed": 1, "own_ship_set_on_fire": True},
        "bar brawl lost": {"ships_destroyed": 0, "own_ship_set_on_fire": False},
    }

    # list made from a dict
    auto_ship_arson_attacks = [
        name
        for (name, brave_act) in brave_acts_by_sea_hawk.items()
        if brave_act["own_ship_set_on_fire"] == True
    ]
    print(
        f"Here is a list of time Sea Hawk burned down his own ship: {auto_ship_arson_attacks}"
    )

    # dict made from a list
    sea_shanty_lengths = {
        sea_shanty: len(sea_shanty)
        for sea_shanty in sea_hawks_favorite_sea_shanties_list
    }
    print(f"Sea Shanty lengths: {sea_shanty_lengths}")

    # dict made from a dict
    score: {
        name: (
            brave_act["ships_destroyed"]
            - (1 if brave_act["own_ship_set_on_fire"] else 0)
        )
        for (name, brave_act) in brave_acts_by_sea_hawk.items()
    }
    print(f"Sea Hawk's score: {score}")

    #  And a last final note: Reemember dictionaries are unordered! Don't expect to get stuff outin the last order it
    #  went in! ... Although it often will be... don't count on it!


if __name__ == "__main__":
    # Magic Python incantation that makes everything go
    main()
