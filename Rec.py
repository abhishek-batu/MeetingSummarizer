
import os
from datetime import datetime, date
import transcribe
import subprocess
import time
from pydub import AudioSegment




import pyaudio
import wave
import shutil

global flag1
flag1=1

with open('Transcripts/transcript.txt') as f:
    lines = f.readlines()
lines = lines[0]


sound = True
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "output.wav"
WAVE_OUTPUT_FILENAME1 = "output1.wav"

p = pyaudio.PyAudio()
p1 = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
        dev_index = dev['index'];

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=dev_index,
                frames_per_buffer=CHUNK)


stream1 = p1.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=0,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []
frames1 = []
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#    data = stream.read(CHUNK)
#    frames.append(data)
while (lines == '1'):
    with open('Transcripts/transcript.txt') as f:
        lines = f.readlines()
    lines = lines[0]

    data = stream.read(CHUNK)
    frames.append(data)
    data1 = stream1.read(CHUNK)
    frames1.append(data1)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
stream1.stop_stream()
stream1.close()
p1.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames1))
wf.close()


wf = wave.open(WAVE_OUTPUT_FILENAME1, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p1.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()




speakersound = AudioSegment.from_file("output.wav")
micsound = AudioSegment.from_file("output1.wav")

mixsound = speakersound.overlay(micsound)

mixsound.export("mixsound.wav", format='wav')



#os.system("python D:\\vsp\pythonProject2\\assemblyai-and-python-in-5-minutes\\transcribe.py D:\\vsp\pythonProject2\\assemblyai-and-python-in-5-minutes\output.wav --local --api_key 964420e2607e4374b3fe3378113b4e5d")
p1=subprocess.Popen(["python","transcribe.py","mixsound.wav","--local","--api_key","964420e2607e4374b3fe3378113b4e5d"]   ,shell=True)
p1.wait()
today = datetime.now()
dateS=str(today.strftime("%c"))
dateS=dateS[4:-5]
dateS=dateS.replace(":","-")
original = r'Transcripts\transcript.txt'
s1=f'Transcripts\\{dateS}.txt'

target = s1
shutil.copyfile(original, target)