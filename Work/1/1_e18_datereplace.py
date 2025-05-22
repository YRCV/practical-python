# regular expressions - date replacer
# exercise 1.18
import re
text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
re.findall(r'\d+/\d+/\d+',text)
print(text)
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
print(text)