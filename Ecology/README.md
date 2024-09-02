Task Description

In the begin directory, there is a definition of a world governed by the following rules:

    The world is flat and has both height and width.
    Every organism in the world has:
        power: increases by 1 each turn; determines the strength of the organism.
        initiative: priority that determines the order of action within a turn.
        position: location in the world.
        liveLength: number of turns left to live.
        powerToReproduce: minimum power required for reproduction; after reproducing, the organism loses half of its power.
        sign: a symbol representing the organism in the world.
        world: the world in which the organism lives.
    The only organisms living in the world are grass and sheep.

Lynx

Based on the animal definition, add a lynx with the following attributes:

    power = 6
    initiative = 5
    liveLength = 18
    powerToReproduce = 14
    sign = 'R'

Antelope

Add an antelope that behaves like a sheep, but if a Lynx appears in its vicinity, it will escape from it by two squares (in the direction opposite to the Lynx’s position); if escape is not possible, it will attack the Lynx.

    power = 4
    initiative = 3
    liveLength = 11
    powerToReproduce = 5
    sign = 'A'

Plague

Add the option to enable a plague mode that shortens the life of all organisms by half. The plague lasts only two turns and does not affect future generations of organisms.
Adding an Organism

Implement the ability to add any new organism to any available free space after any turn.