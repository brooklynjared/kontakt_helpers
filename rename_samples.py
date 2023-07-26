import glob
import os
import natsort

# Set path 
folder_path = '/Volumes/Authentic Soundware/Soul-Guitar/_Dev/Samples/chords/basic-short-DS/maj1/dyn1/' 

# Find all .wav files in current folder and subfolders
files = glob.glob(folder_path + "*.wav")

sorted_files = natsort.natsorted(files)

i = 0
rr = 1
note = 60

for file in sorted_files:

    old_filename = file

    base_file_name = 'basic - DS - maj1 - dyn1'
    new_filename = folder_path + base_file_name + ' - RR' + str(rr) + ' - ' + str(note) + '.wav'

    # advance note number if rr4 just completed
    if rr == 4:
        note += 1

    # update rr
    if rr < 4:
        rr += 1
    else:
        rr = 1

    os.rename(old_filename, new_filename)

