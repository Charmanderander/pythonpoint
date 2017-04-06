import re

path = r'slides.txt'


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
            print point[0] + "." + ("~"*(len(mark)-1)) + content

import pdb; pdb.set_trace()
            
