from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Set the silence threshold, in dBFS (decibels relative to full scale)
# This value depends on the audio's volume and noise level
silence_threshold = -50

# Split the audio into chunks of non-silent audio and silent audio
chunks = audio.split_to_mono()[0].silent_parts(min_silence_len=500, silence_thresh=silence_threshold)

# Combine the non-silent chunks into a single audio segment
result = AudioSegment.from_mono_audiosegments(*[chunk.left for chunk in chunks])

# Save the result
result.export("output.wav", format="wav")
