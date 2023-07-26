from math import floor


# List of note names using sharps
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# List of note names using flats
enharmonic_spellings = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G" "Ab", "A", "Bb", "B"]


# Convert an integer representing midi note number to a string with a note name and octave ex: 61 -> "C#3"
def num_to_note(n: int):
    if type(n) != int:
        print("Input must be an integer.")
        raise TypeError
    elif n not in range(0, 128):
        print("Input must be an int between 0 and 127")
        raise ValueError
    else:
        try:
            octave = int(floor(n / 12) - 2)
            note_name = str(note_names[n % 12]) + str(octave)
            return note_name
        except:
            return None


# Convert a note name ** without an octave ** to an int representing a midi note number for that note ex D# -> 3
# The octave can be added in a separate function
def note_to_num(s: str):
    if type(s) != str:
        print("Input must be a string")
        raise TypeError
    elif len(s) > 2:
        print("String is too long.")
        raise ValueError
    else:
        try:
            if s in note_names:
                return note_names.index(s)
            if s not in note_names and s in enharmonic_spellings:
                return enharmonic_spellings.index(s)
        except:
            return None


print(note_to_num("Db"))
