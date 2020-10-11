'''Poblem: word count problem 
   - Find the ten most commonly used words in a text file
   - sample input file aka paradise-lost.txt is downloaded as:
     wget -O paradise-lost.txt 'http://www.gutenberg.org/cache/epub/26/pg26.txt'
'''
from re import sub

def concordance(text):
    freq={}
    for word in text.split():
        word = sub('[^\w]', '',word.lower())
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

with open('paradise-lost.txt') as f:
    text = ''.join(f)

freq = concordance(text)
results=sorted(freq.items(),key=lambda kv: kv[1],reverse=True)[:10]
for result in results:
    print(result)

