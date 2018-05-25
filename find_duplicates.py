import sys

file_to_search = sys.argv[1]

tn = 'tempfilefourth.tmp'
splits = 3

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print('Copying Fourth Lines')

with open(file_to_search, 'rb') as f:
    with open(tn, 'wb') as w:
        for i, line in enumerate(f):
            if i % 4 == 0:
                w.write(line) 
                
print('Counting Lines')
num_lines = file_len(tn)
print('Number of Fourth Lines: ', num_lines)

print('Finding Section Offsets')

offsets = []
offset = 0

last = -1
with open(tn, 'rb') as f:
    for i, line in enumerate(f):
        if int(i * splits / num_lines) > last:
            last = int(i * splits / num_lines)
            offsets.append(offset)
            print(last + 1)
        
        offset += len(line)
offsets.append(offset)

duplicate_lines = set()

print('Searching For Duplicates')

for split in range(splits):
    offset = offsets[split]
    offsetEnd = offsets[split+1]
    
    lines = set()
    
    print('Starting Split: ', (1 + split))
    print('Reading Split Lines')
    
    with open(tn, 'rb') as f:
        f.seek(offset)
        for l in f:
            if l in lines:
                duplicate_lines.add(l)
            else:
                lines.add(l)
            offset += len(l)
            if offset == offsetEnd:
                break
                
    print('Reading Other Lines')
                
    with open(tn, 'rb') as f:
        for i, l in enumerate(f):
            if l in lines and int(i * splits / num_lines) != split:
                duplicate_lines.add(l)
                
    print('Finished Split')
    print('Current Num Dups: ', len(duplicate_lines))
    print()
    
print('Found Duplicates:')
for l in duplicate_lines:
    print(l.decode('utf-8'))

print('Deleting Temporary File')

import os
try:
    os.remove(tn)
except OSError:
    print('ERROR COULD NOT DELETE TEMP FILE')
