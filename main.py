import re

path = r'slides.txt'

mainpoint = '1'

with open(path,'r') as fin:
    read_data = fin.readlines()
    for line in read_data:
        m = re.search(r'\[([^\]]+)\]\(([^\)]+)\)', line)
        mark = m.group(1)
        content = m.group(2)
        if mark == "h": # if its the header
            print  content 
            print (len(content) + 4) * "#"
        else:
            point = mark.split(".")
            if point[0] != mainpoint: # if not a sub point of previous point
                mainpoint = point[0]
                
            print mainpoint + "." + ("~"*(len(mark)-1)) + content

import pdb; pdb.set_trace()
            
