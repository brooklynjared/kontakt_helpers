import sys
import os
import argparse
from math import floor
import re


# TO DO

# - do the conversion and renaming all files

# List of note names using sharps
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# List of note names using flats
ENHARMONIC_SPELLINGS = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


# -----------------------------------------------------------------------
#  MAIN 
# -----------------------------------------------------------------------

def main():

    path, mode, direction, offset = check_args(args)

    files = get_files(path)

    # Generate a preview filename.
    preview_filename = generate_new_filename(files[0], mode, direction, offset)

    # Display preview and ask user to confirm before proceeding.
    if preview(files[0], preview_filename):
        print("Replace the files")
    return




# -----------------------------------------------------------------------
#  FUNCTIONS 
# -----------------------------------------------------------------------

# Check args and configure settings
def check_args(args):

    # Check file path
    if not os.path.isdir(args.p):
        sys.exit("Invalid path.")
    else:
        path = args.p

    # Check direction
    if not args.d:
        sys.exit("Please specify the direction of the operation. Use -h for usage tips.")
    elif args.d != "numbers" and args.d != "names":
        sys.exit("Invalid conversion type. Use -h for usage tips.")
    else:
        direction = args.d

    # Check mode
    if args.m != "append" and args.m != "replace":
        sys.exit("Invalid Mode")
    else:
        mode = args.m

    # Check octave offset
    if int(args.o) != 0 and int(args.o) != 1:
        sys.exit("Invalid octave offset")
    else:
        offset = int(args.o)


    return path, mode, direction, offset


# Get files
def get_files(path):
    return [file for file in os.listdir(path)]

# Retrieve the first occurence of a MIDI note number in a string
def match_nums(f: str):
    # Search for 2 or 3 digits that aren't followed by "bpm", case-insensitive, with or without a space separator
    m = re.search(r'\d\d\d?(?!\d?\s?BPM)', f, re.IGNORECASE)
    if int(m.group()) < 128:
        return int(m.group()), m.start(), m.end()
    else:
        return None

# Retrieve the first occurence of a note name with an octave number in a string
def match_notes(f: str):
    m = re.search(r'[C,D,E,F,G,A,B]#?b?-?\d', f)
    return m.group(), m.start(), m.end()


# Convert an integer representing midi note number to a string with a note name and octave ex: 61 -> "C#3"
def num_to_note(n: int, offset):
    if type(n) != int:
        print("Input must be an integer.")
        raise TypeError
    elif n not in range(0, 128):
        print("Input must be an int between 0 and 127")
        raise ValueError
    else:
        try:
            octave = int(floor(n / 12) - 2 + offset)
            note_name = str(NOTE_NAMES[n % 12]) + str(octave)
            return note_name
        except:
            return None


# Convert a note name without an octave to an int representing a midi note number for that note (ex C3 -> 60)
def note_to_num(s: str, offset):
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
            
            if note in NOTE_NAMES:
                return NOTE_NAMES.index(note) + ((octave + 2 - offset) * 12)
            elif note not in NOTE_NAMES and note in ENHARMONIC_SPELLINGS:
                return ENHARMONIC_SPELLINGS.index(note) + ((octave + 2 - offset) * 12)
            else:
                return None
        
        else:
            print('Could not find a match for this value.')
            raise ValueError
        
    except:
        return None


def generate_new_filename(filename, mode, direction, offset):
    if direction == "names":
        try:
            num, start, end = match_nums(filename)
            new_val = num_to_note(num, offset)
        except:
            sys.exit("An error ocuured.")            
        
    if direction == "numbers":
        try:
            note, start, end = match_notes(filename)
            new_val = note_to_num(note, offset)
        except:
            sys.exit("An error ocuured.")
    
    # Convert int to string if necessary
    if type(new_val) != str:
        new_val = str(new_val)

    # Assemble the new filename
    return filename[:start] + new_val + filename[end:-1]


def preview(old_filename, new_filename):
    print(" --- Preview changes --- ")
    print("Orig: ", old_filename)
    print("New: ", new_filename)

    confirm = input("Proceed? y/n: ")
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        print("processing files...")
        return True
    else:
        sys.exit("Cancelling process.")



# -----------------------------------------------------------------------
#  Call Main 
# -----------------------------------------------------------------------

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog='MIDI Note Helper',
        description="Rename a batch of files containing MIDI note numbers or names. Match and convert MIDI note text to or from names/numbers."
        )
    parser.add_argument("-p", default="/", help="Path: full path to directory of files to rename.")
    parser.add_argument("-d", help="Direction: 'numbers' converts names to numbers, 'names' converts numbers to names.")
    parser.add_argument("-m", default="append", help="Mode: append/replace to either add new format, or replace existing with new format")
    parser.add_argument("-o", default=0, help="Octave offset: Default value of 0 equates 'middle C'/MIDI note 60 with C3, set to 1 to equate 'middle C'/note 60 to C4")
    args = parser.parse_args()
    main()