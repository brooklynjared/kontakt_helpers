import os

articulations = [
  'basic-short-DS',
  'basic-short-US',
  'basic-medium-DS',
  'basic-medium-US',
  'basic-long',
  'basic-fat',
  'rake-short',
  'rake-long',
  'semitone-scoop',
  'fall',
]

chords = [
  "maj1",
  "maj2",
  "maj3",
  "maj7",
  "min1",
  "min2",
  "min3",
  "min7",
  "dom7",
  "dom7sus4",
]

# make folder for each articulation
for artic in articulations:
    os.mkdir(f"./{artic}")

# make folder for each chord type
for artic in articulations:
    for chord in chords:
        path = f"./{artic}/{chord}"
        os.mkdir(path)