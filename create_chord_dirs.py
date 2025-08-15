import os
chords = ['Am', 'Dm', 'E', 'C', 'F', 'G']
base_dir = "data"
os.makedirs(base_dir,exist_ok=True)

for chord in chords:
    chord_path = os.path.join(base_dir, chord)
    os.makedirs(chord_path, exist_ok=True)
    print(f"Created: {chord_path}")