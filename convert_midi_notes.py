from math import floor
import re

# TO DO

# - gather all the files
# - from sys.argv determine the rename mode: append/replace new format to existing

# - display a preview of the conversion
# - do the conversion and rename all files



filename = "sample - mf - F2 - 180 BPM"

def match_nums(f: str):
    # Search for 2 or 3 digits that aren't followed by "bpm", case-insensitive, with or without a space separator
    m = re.search(r'\d\d\d?(?!\d?\s?BPM)', f, re.IGNORECASE)
    if int(m.group()) < 128:
        return int(m.group())
    else:
        return None

def match_notes(f: str):
    m = re.search(r'[C,D,E,F,G,A,B]#?b?-?\d', f)
    return m.group()




# List of note names using sharps
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# List of note names using flats
enharmonic_spellings = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


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


# Convert a note name without an octave to an int representing a midi note number for that note (ex C3 -> 60)

def note_to_num(s: str):
    # Check the if the argument is valid
    if type(s) != str:
        print("Input must be a string")
        raise TypeError
    
    if len(s) not in range(2,5):
        print("Invalid string length.")
        raise ValueError

    try:
        if m := re.match(r'([C,D,E,F,G,A,B]#?b?)(-?\d)', s):
            note = m.group(1)
            octave = int(m.group(2))


            if octave not in range(-2, 9): 
                print("Invalid octave range.")
                raise ValueError
            
            if note in note_names:
                return note_names.index(note) + ((octave + 2) * 12)
            elif note not in note_names and note in enharmonic_spellings:
                return enharmonic_spellings.index(note) + ((octave + 2) * 12)
            else:
                print("this!")

        
        else:
            print('Could not find a match for this value.')
            raise ValueError
        

    except:
        return None
