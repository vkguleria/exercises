'''
The script reads N lines and writes them to the files

'''

import sys
from itertools import islice
filename=sys.argv[1]
print(f'got {filename}')
part=1
with open(filename,'r') as f:
    for line in f:
        with open(filename+str(part),'w') as fw:
            fw.write(line)
            for lines in islice(f,29):
                fw.write(lines)
                #print(f'{part}: {lines.strip()}')
        part += 1
