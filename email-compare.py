
#compares 2 email lists

import os
import re
import collections

#transpose the list and copy to string
lst_XL = ''
#extract the list in mail send field and copy to string
lst_DL = ''
output = ''
list_all = ''
str_dupes = ''

lst_XL = re.findall('[\w.+-]+@[\w-]+\.[\w.-]+', lst_XL.lower())
lst_DL = re.findall('[\w.+-]+@[\w-]+\.[\w.-]+', lst_DL.lower())

for x in [item for item, count in collections.Counter(lst_XL).items() if count > 1]:
        str_dupes += 'Duplicates: ' + x + ' \n'
print(str_dupes) 

list_all = list(dict.fromkeys(lst_XL + lst_DL))
list_all.sort()

for item in list_all:
    if item in lst_XL:
        output += item + ',F'
    else:
        output += item + ',x'
    if item in lst_DL:
        output += ',DL' + '\n'
    else:
        output += ',x' + '\n'

print(output)
