# The script of the game goes in this file.

define gui.text_font = "VCR_OSD_MONO.ttf"

define gui.name_xpos = 10000

define mc = Character("MC")

default world = Null

default current_area = Null

image apartments = "test/bg apartments.png"

init python:
    import random
    from world import World

    def generate_world():
        world = World()
        # world.add_connectors()
        store.world = world

label start:

    scene bg room

    # mc "It's midnight, and I can't sleep."

    # mc "I'm all out of melatonin, and the glass of wine I drank earlier isn't hitting."

    # mc "Oh well. I suppose I will go for a walk."

    # scene bg black

    # mc "I've always liked going out at night."

    # mc "By that, I don't mean I like to drink or party or whatever."

    # mc "I just... go out."

    # BEGIN PYTHON CODE

    python:
        generate_world()

    mc "Bruh"

    mc "[world]"

    jump go_outside

label go_outside:

    python:
        store.current_area = store.world.nodes[len(world.nodes) - 1]

    scene apartments

    mc "[current_area]"

    return


