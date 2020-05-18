import re
import pyinputplus as pipl
filename = pipl.inputFilepath(prompt='Enter a File Path: ')
file = open(filename)
contents = file.read();
re = re.compile(r'(ADJECTIVE|NOUN|VERB)')
placeholders = re.findall(contents)
for i in placeholders:
    item = pipl.inputStr(prompt='Enter a '+ i + ': ')
    contents = contents.replace(i, item, 1)
print(contents)
filename = pipl.inputFilepath(prompt='Enter a New File Path: ')
file = open(filename, 'w')
file.write(contents)
file.close()