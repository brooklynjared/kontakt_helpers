import sys
import os
import argparse
from math import floor
import re


# TO DO


# - display a preview of the conversion
# - do the conversion and rename all files


# List of note names using sharps
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# List of note names using flats
enharmonic_spellings = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


# -----------------------------------------------------------------------
#  MAIN 
# -----------------------------------------------------------------------

def main():

    path, mode, direction = check_args(args)

    # print("Path:", path)
    # print("Mode:", mode)
    # print("Direction: to", direction)

    files = get_files(path)

    if direction == "names":
        try:
            num, start, end = match_nums(files[0])
            new_val = num_to_note(num)
            old_filename = files[0]
            new_filename = replace(old_filename, new_val, start, end)

            print(" --- Preview changes --- ")
            print("Orig: ", old_filename)
            print("New: ", new_filename)

            confirm = input("Proceed? y/n: ")
            if confirm.lower() == 'y' or confirm.lower() == 'yes':
                print("processing files....")
            else:
                sys.exit("Cancelling process.")
        except:
            sys.exit("An error ocuured.")

    return


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

    return path, mode, direction


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
                return None
        
        else:
            print('Could not find a match for this value.')
            raise ValueError
        
    except:
        return None

# Replace the current value with the value in the new format. Returns a new filename as a string
def replace(old_filename: str, new_val: str, start: int, end: int):
    return old_filename[:start] + new_val + old_filename[end:-1]

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog='MIDI Note Helper',
        description="Rename a batch of files containing MIDI note numbers or names. Match and convert MIDI note text to or from names/numbers."
        )
    parser.add_argument("-p", default="/", help="Path: full path to directory of files to rename.")
    parser.add_argument("-d", help="Direction: 'numbers' converts names to numbers, 'names' converts numbers to names.")
    parser.add_argument("-m", default="append", help="Mode: append/replace to either add new format, or replace existing with new format")
    args = parser.parse_args()
    main()