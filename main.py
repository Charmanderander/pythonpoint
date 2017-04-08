import re
import code
import os, os.path

DIR = "slides/"

slide_count = 1
total_slides = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
path = r'slides/slide' + str(slide_count) + '.txt'

while(input != "3"):
    with open(path,'r') as fin:
        read_data = fin.readlines()
        for line in read_data:
            # getting values in the brackets [] and ()
            # values in () indicates which point
            # values in [] represents the content
            m = re.search(r'\[([^\]]+)\]\(([^\)]+)\)', line)
            mark = m.group(1)
            content = m.group(2)
            if mark == "h": # if its the header
                print "\n" * 100
                print 80 * "^"
                print "Slide " + str(slide_count) + "/" + str(total_slides)
                print  content 
                print 80 * "-"
            else: # else print the contents
                point = mark.split(".")
                # len(mark) finds out which subpoint is it
                print point[0] + "." + (" "*(len(mark)-1)) + "~ " +content

    code.interact(local=locals())
    input = raw_input("Next Slide: 1\nPrev Slide: 2\nEnd Presentation: 3\nChoice:")
    if input == "1":
        slide_count += 1
        new_slide = r'slides/slide' + str(slide_count) + '.txt'
        if os.path.exists(new_slide):
            path = new_slide
        else:
            r'slide' + str(slide_count - 1) + '.txt'
            slide_count -= 1
    elif input == "2":
        slide_count -= 1
        if slide_count == 0:
            slide_count += 1
        


print "Thank you!"
