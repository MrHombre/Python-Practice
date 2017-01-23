Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> usr = 'Tuna McFish'
>>> usr[0]
'T'
>>> usr[5]
'M'
>>> usr[-1]
'h'
>>> usr[-5]
'c'
>>> usr[2:7]
'na Mc'
>>> usr[2\7]
SyntaxError: unexpected character after line continuation character
>>> usr[:7]
'Tuna Mc'
>>> usr[2:]
'na McFish'
>>> usr[:]
'Tuna McFish'
>>> usr.len
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    usr.len
AttributeError: 'str' object has no attribute 'len'
>>> len(usr)
11
>>> 
