import re

data = ['  abc  ', 'def  ', '  ghi', 'jkl', 'm n o', 'p q ']
def regstrip(item, char=' '):
    if(char == ' '):
        regex = re.compile(r'^(\s*)(.*?)(\s*)$')
        return regex.sub(r'\2', item)
    else:
        regex = re.compile('%s'%char)
        return regex.sub(' ', item)
for item in data:
    print('RS:%s:\nST:%s:\nRP:%s:' % (item, item.strip(), regstrip(item, 'jk')))