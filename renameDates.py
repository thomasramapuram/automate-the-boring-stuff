#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re, shutil, os, sys

# Create an European Date Pattern
euroDatePattern = re.compile(r'''^(.*?)
((0?[1-9]])|1\d|2\d|30|31)-
((0?\d)|11|12)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)
# Create an International Date Pattern
intrDatePattern = re.compile(r'''^(.*?)
((19|20)\d\d)-
((0?\d)|11|12)-
((0?[1-9]])|1\d|2\d|30|31)-
(.*?)$
''', re.VERBOSE)
# Create an American Date Pattern
amerDatePattern = re.compile(r'''^(.*?)
((0?\d)|11|12)-
((0?[1-9]])|1\d|2\d|30|31)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)
if(len(sys.argv)<3):
    exit()
dateFrom = sys.argv[1]
dateTo = sys.argv[2]

if dateFrom == 'a':
    datePattern = amerDatePattern
elif dateFrom == 'e':
    datePattern = euroDatePattern
elif dateFrom == 'i':
    datePattern = intrDatePattern

# Loop over the files in the working directory.
def getToFilename(mo, dateFrom, dateTo):
    print('mo: %s, from: %s, to: %s'% (mo, dateFrom, dateTo))

    if dateFrom == 'a':
        dateParts = {
            'before':mo.group(1),
            'day': mo.group(4),
            'month': mo.group(2),
            'year': mo.group(6),
            'after': mo.group(8)
        }
    elif dateFrom == 'e':
        dateParts = {
            'before': mo.group(1),
            'day': mo.group(2),
            'month': mo.group(4),
            'year': mo.group(6),
            'after': mo.group(8)
        }
    elif dateFrom == 'i':
        dateParts = {
            'before': mo.group(1),
            'day': mo.group(6),
            'month': mo.group(4),
            'year': mo.group(2),
            'after': mo.group(8)
        }
    else:
        return ''

    if dateTo == 'a':
        toFilename = dateParts['before'] + \
                     dateParts['month'] + '-' + \
                     dateParts['day'] + '-' + \
                     dateParts['year'] + \
                     dateParts['after']
    elif dateTo == 'e':
        toFilename = dateParts['before'] + \
                     dateParts['day'] + '-' + \
                     dateParts['month'] + '-' + \
                     dateParts['year'] + \
                     dateParts['after']
    elif dateTo == 'i':
        toFilename = dateParts['before'] + \
                     dateParts['year'] + '-' + \
                     dateParts['month'] + '-' + \
                     dateParts['day'] + \
                     dateParts['after']
    else:
        toFilename = ''
    return toFilename

for fromFileName in os.listdir('.'):
    mo = datePattern.search(fromFileName)
    #Skip files without a date.
    if mo == None:
        continue
    toFilename = getToFilename(mo, dateFrom, dateTo)

    if toFilename == None:
        continue
    print(toFilename)

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    fromFileName = os.path.join(absWorkingDir, fromFileName)
    toFilename = os.path.join(absWorkingDir, toFilename)

    # TODO: Rename the files.
    #print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(fromFileName, toFilename)