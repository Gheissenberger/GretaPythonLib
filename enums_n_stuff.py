"""
Enums 'n Stuff

Ok, so like, you know when you want like a list of things, but it can only be like certain things?
But like, not big enough for a database. Just, a couple of things.
Like constants, or types of things that can switch.

Or you want to match all the names of a thingy to an id?

Try an Enum!

Official documentation here: https://docs.python.org/3/library/enum.html

@author Greta Heissenberger
@date 2/14/22
"""

from enum import Enum


class QueerEyeGuy(Enum):
    KARAMO = 1
    JONATHAN = 2
    JVN = 2
    ANTONI = 3
    TAN = 4
    BOBBY = 5


def stan(cast_member: QueerEyeGuy):
    """
    Prints a little message about one QueerEyeGuy object

    Oh and look how cool, an Enum can be a param and then you know EXACTLY what options are supported!
    :param cast_member: a QueerEyeGuy object
    """
    if type(cast_member) is not QueerEyeGuy:
        raise TypeError("Um, Excuse Me, that param is not a QueerEyeGuy object.")

    print(f"OMG {cast_member.name} is the BEST!!!1!")


def main():
    """
    Let's learn about Enum with the fab five!
    """
    print("Hello Gorgeous")

    # You can easily refer to a specific member
    my_bestie = QueerEyeGuy.KARAMO
    stan(my_bestie)

    # You can iterate through an Enum and get the full object, with a name and value
    for queer_eye_guy in QueerEyeGuy:
        print(f"So {queer_eye_guy.name} is number {queer_eye_guy.value}, which is SO PERFECT!")

    # An enum has members, too which, actually, might be easier
    print("But honestly they are all so great.")
    for name, number in QueerEyeGuy.__members__.items():
        print(f"{name} is so great!")

    # You can refer to Enum members individually by name a couple of ways.
    cast_member_with_least_screen_time = QueerEyeGuy.BOBBY
    cast_member_who_works_the_most_hours = QueerEyeGuy['BOBBY']
    if cast_member_with_least_screen_time == cast_member_who_works_the_most_hours:
        print("Ugh Bobby works so hard but they don't show it!")

    # Lookup by value is a bit weirder... I mean typically you want to look something up by name not value...
    # But you can if you want I guess
    most_underrated_guy = QueerEyeGuy(5)
    if most_underrated_guy == cast_member_with_least_screen_time:
        print("Maybe if they would give him more camera time...")

    """
    So ok, that's cool but why is any of this useful at all?
    Well, If you use Enums for lists, it's like, impossible to pick something not in the list.
    AAAand it's very easy to see what the possible options are!
    """
    try:
        stan("Eminem")
    except TypeError as err:
        print(f"""Um, Honey, I don't want to tell you how to write your code but... you just got an exception:
        {err}""")

    # I hope you learn to love the Enum class as much as JVM loves powdered doughnuts!


if __name__ == "__main__":
    # Magic Python incantation that makes everything go
    main()
