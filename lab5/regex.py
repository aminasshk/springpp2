#1
import re
s = input('Input your string: ')
check = re.compile('ab*')
n = check.search(s)
if n:
    print("Found: ", n.group())
else:
    print('No match')

#2
import re
s = input('Input your string: ')
check = re.compile('ab{2, 3}')
n = check.search(s)
if n:
    print("Found: ", n.group())
else:
    print('No match')

#3
import re
s = input('Input your string: ')
check = re.compile('[a-z]+_[a-z]+')
n = check.search(s)
if n:
    print("Found: ", n.group())
else:
    print('No match')

#4
import re
s = input('Input your string: ')
check = re.compile('[A-Z][a-z]+')
n = check.search(s)
if n:
    print("Found: ", n.group())
else:
    print('No match')

#5
import re
s = input('Input your string: ')
check = re.compile('a.*b$')
n = check.search(s)
if n:
    print("Found: ", n.group())
else:
    print('No match')

#6
import re
s = input('Input your string: ')
print(re.sub(r'[ ,.]', ':', s))

#7
import re
s = input('Input your string: ')
def snake_to_camel(s):
    words = s.split('_')
    c_words = words[0].capitalize() + ''.join(word.capitalize() for word in words[1:])
    return c_words    
print(snake_to_camel(s))

#8
import re
s = input('Input your string: ')
def split_between_big(s):
    result = re.split(r'(?=[A-Z])', s)
    return result
print(split_between_big(s))

#9
import re
s=input('Input your string: ')
def space(s):
    result=re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return result
print(space(s))

#10
import re
s = input('Input your string: ')
def camel_to_snake(s):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', s)
    return result
print(camel_to_snake(s))