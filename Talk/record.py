#!/usr/bin/env python3


"""
Module Name: record.py

Description:Record a simple speach command in wave format 

Classes:

Functions:


Author: Messaoudi Dhia Elhak
Date: 2023-04
"""
import pyaudio
import wave

#Set parameters for audio recording
chunk = 1024  # number of samples per audio buffer
sample_format = pyaudio.paInt16  # audio bit depth
channels = 2  # stereo audio
sample_rate = 16000  # audio sampling rate (in Hz)
record_seconds = 1  # duration of audio recording (in seconds)



def record():
    audio = pyaudio.PyAudio()

    input("Press Enter to start recording...")
    stream = audio.open(format=sample_format, channels=channels, rate=sample_rate,
                        frames_per_buffer=chunk, input=True)
    frames = []
    for i in range(0, int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    wave_file = wave.open("recorded/recorded_audio.wav", "wb")
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(sample_format))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()

    audio.terminate()