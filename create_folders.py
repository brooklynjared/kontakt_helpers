import os

# path root
root = './' # curently set to folder where the script resides


# Create a list of main folders, (ie, for articulations, instruments, ...)
folders = [
  'sustain',
  'staccato',
  'marcato',
  'pizzicato',
  'crescendo',
  'diminuendo',
]

# Create a list of subfolders (ie, for round robins, dynamic levels, ...)
subfolders = [
  "RR1",
  "RR2",
  "RR3",
  "RR4",
]

# Loop over main and subfolders to make directories
for folder in folders:
    # maked the main folder
    os.mkdir(f"{root}/{folder}")

    # make the subfolders within each main folder
    for subfolder in subfolders:
        path = f"{root}/{folder}/{subfolder}"
        os.mkdir(path)