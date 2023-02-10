from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("audio.wav", format="wav")

# Remove silence from the start and end of the audio
start_trim = audio.start_trim(silence_threshold=1000)
end_trim = start_trim.end_trim(silence_threshold=1000)

# Save the trimmed audio to a file
end_trim.export("trimmed_audio.wav", format="wav")
