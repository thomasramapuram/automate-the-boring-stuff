import pyinputplus as pyip
from pathlib import Path
import re

def get_dir(count=0):
    dir = pyip.inputFilepath(prompt='Enter a directory: ')
    if(Path(dir).is_dir()):
        return dir
    else:
        if(count > 5):
            raise Exception("Too many tries")
        get_dir(count+1)

try:
    dir = Path(get_dir())
except:
    print('Too many tries')
    exit()

regex = pyip.inputRegexStr(prompt='Enter the Regular Expression: ')
r = re.compile(regex)
files = list(dir.glob('*.txt'))
for file in files:
    file_handle = open(file)
    contents = file_handle.read()
    print(r.findall(contents))
