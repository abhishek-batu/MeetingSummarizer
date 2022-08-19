with open('Transcripts/transcript.txt', 'r+') as f:
    lines = f.readlines()
    print(lines)
    if(lines == []):
        lines='aaaaaaa'
    if(lines[0] == '1'):
        f.truncate(0)
        f.seek(0)
        f.write('0')
    else:
        f.truncate(0)
        f.seek(0)
        f.write('1')
