from pathlib import Path

# path root
root = Path("./samples/")  # curently set to folder where the script resides


# Create a list of main folders, (ie, for articulations, instruments, ...)
folders = [
    "sustain",
    "staccato",
    "marcato",
    "pizzicato",
    "crescendo",
    "diminuendo",
]

# Create a list of subfolders (ie, for round robins, dynamic levels, ...)
subfolders = [
    "RR1",
    "RR2",
    "RR3",
    "RR4",
]


try:
    # Loop over main and subfolders to make directories
    for folder in folders:
        for subfolder in subfolders:
            subfolder_path = Path(root, folder, subfolder)
            Path.mkdir(subfolder_path, parents=True, exist_ok=False)

except FileExistsError:
    print("One or more of the directories already exists.")
    exit(1)
