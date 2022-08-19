#pip install transformers[sentencepiece]
#pip install torch torchvision torchaudio

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("abhiBatu/MeetingSumm")

model = AutoModelForSeq2SeqLM.from_pretrained("abhiBatu/MeetingSumm")

from transformers import pipeline

global flag
flag=0
fhand=open("Transcripts/transcript.txt", 'r')
tra=fhand.read()
text =tra

generator = pipeline(task = "summarization",model=model, tokenizer=tokenizer,truncation = True, max_length=5000)
preds = generator(text)
s=""
s=s+str(preds)
s=s.replace("{","")
s=s.replace("[","")
s=s.replace("}","")
s=s.replace("]","")
s=s.replace("[{\'summary_text\': \'","")
s=s[17:]
s=s[:-1]
s = s.replace("\\n", "\n")

print(s)

with open('Transcripts/summary.txt', 'w') as f:
    f.write(s)
flag=1
