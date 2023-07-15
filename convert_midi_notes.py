
"""
Function for converting a numerical MIDI note number to a string of the standard MIDI note name.

Examples: 60 converted to "C3" or 1 converted to  "C#-2"

Input to the function should be an int in standard MIDI range of 0 to 127.

"""


from math import floor

note_names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def num_to_note(n):
    
    if type(n) != int:
        print("Input must be an integer.")
        raise TypeError
    elif n not in range(0,128):
        print("Input must be an int between 0 and 127")
        raise ValueError
    else:
        try:
            octave = int(floor(n/12) - 2)
            note_name = str(note_names[n%12]) + str(octave)
            return note_name
        except:
            return
        
