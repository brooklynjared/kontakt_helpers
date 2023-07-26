from math import floor
import re

# TO DO

# - gather all the files
# - from sys.argv determine the rename mode: append/replace new format to existing
# - extract matches for note numbers from a filename
# - extract matches for note names from a filename
# - do the conversion
# - construct the new filename
# - rename the file


filename = "sample - mf - F2 - 180 BPM"

def match_nums(f: str):
    # Search for 2 or 3 digits that aren't followed by "bpm", case-insensitive, with or without a space separator
    m = re.search(r'\d\d\d?(?!\d?\s?BPM)', f, re.IGNORECASE)
    if int(m.group()) < 128:
        return int(m.group())
    return 

def match_notes(f: str):
    m = re.search(r'[C,D,E,F,G,A,B]#?b?-?\d', f)
    
    # TO DO!!!
    # Split the note portion and the octave portion and return two values instead of one
    return m.group()




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


# Convert a note name ** without an octave ** to an int representing a midi note number for that note (ex D# -> 3)
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


