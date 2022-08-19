import shutil
from datetime import date

today = date.today()
dateS=(today.strftime("%c"))
dateS=dateS[4:]
original = r'\assemblyai-and-python-in-5-minutes\transcript.txt'
s1=f'\Transcripts\{dateS}.txt'
target = r's1'
shutil.copyfile(original, target)