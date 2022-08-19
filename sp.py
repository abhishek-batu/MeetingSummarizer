import torch
import transformers
from fastai.text.all import *

from blurr.text.data.all import *
from blurr.text.modeling.all import *

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from huggingface_hub import from_pretrained_fastai

# repo_id = "YOUR_USERNAME/YOUR_LEARNER_NAME"
repo_id = "AdShenoy/Bart_summarizer"

global flag
flag=0
fhand=open("Transcripts/transcript.txt", 'r')
tra=fhand.read()
text =tra

learner_blurr = from_pretrained_fastai(repo_id)
outputs = learner_blurr.blurr_generate(text, early_stopping=False, num_return_sequences=1, min_length=150, max_length=800)

for idx, o in enumerate(outputs):
    print(f'=== Prediction {idx+1} ===\n{o}\n')

op=""
op=op+str(outputs[0])
print(type(op))
op= op[22:-2]
with open('Transcripts/summary.txt', 'w') as f:
    f.write(op)
f.close()
flag=1