import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Load audio file
filename = "path/to/your/audio.wav"
y, sr = librosa.load(filename)

# Trim silent parts of the audio
y_trimmed, index = librosa.effects.trim(y, top_db=30, frame_length=2, hop_length=500)

# Save the trimmed audio
librosa.output.write_wav("trimmed_audio.wav", y_trimmed, sr)
