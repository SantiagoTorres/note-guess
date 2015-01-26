#/usr/bin/env python
"""
    <Name>
        note-guess.py

    <Purpose> 

        Play a note, ask the user to guess it.

    <Usage>
        ./note-guess.py [args]

    <Author>
        Santiago Torres Arias

"""
import random
from virtualbeep.virtualbeep import play_beep

# we will define a table of the first octave
C      = 16.35 
CSHARP = 17.32 
D      = 18.35 
DSHARP = 19.45 
E      = 20.60 
F      = 21.83 
FSHARP = 23.12 
G      = 24.50 
GSHARP = 25.96
A      = 27.50 
ASHARP = 29.14 
B      = 30.87 

FUNDAMENTAL_FREQUENCIES = [ C, CSHARP, D, DSHARP, E, F, FSHARP, G, GSHARP,
        A, ASHARP, B]

NOTE_NAMES = ["C", "CSHARP", "D", "DSHARP", "E", "F", "FSHARP", "G", "GSHARP",
        "A", "ASHARP", "B"]

"""
    <Name>
        pick_random_note

    <Purpose>
        Produce a frequency from the available notes inside an octave range

    <Parameters>
        octaves (int)
            The range of octaves to include. 0 is a valid choice.

        start   (int)
            The starting octave to use.

    <Returns>
        A tuple of: (random_frequency, its name, its octave

"""

def pick_random_note(octaves = 2, start = 4):

    assert(type(octaves) == int)
    assert(type(start) == int)
    assert(octaves > 0 and octaves < 10)
    assert(start > 0 and start < 10)
    assert(start + octaves < 10)

    fundamental = random.randint(0, len(FUNDAMENTAL_FREQUENCIES) - 1)
    name = NOTE_NAMES[fundamental]
    octave = random.randint(start, start + octaves - 1)
    frequency = FUNDAMENTAL_FREQUENCIES[fundamental] * 2**octave

    return frequency, name, octave


if __name__ == "__main__":

    frequency, name, octave = pick_random_note()

    play_beep(secs = 3, notefreq = frequency)

    choices = []
    choices.append(random.choice(NOTE_NAMES))
    choices.append(random.choice(NOTE_NAMES))
    choices.append(name)
    random.shuffle(choices)

    guess = None

    while guess not in choices:
        print("Which of these is the right note?: ")
        guess = raw_input("{}: ".format(choices))

        if guess not in choices:
            print("This is a wrong guess, try again")

    if guess == name:
        print("Correct!")

    else:
        print("That was a wrong guess :(")
        print("The right guess was {}".format(name))

    

    






