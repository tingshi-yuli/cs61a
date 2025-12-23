#   date
from datetime import date
today = date

#   string
s = 'Hello World'
print(s)
print(s.upper())
print(s.lower())
print(s.swapcase())#交换大小写

a = 'A'
print(ord(a))
print(hex(ord(a)))
print('\a\a\a')

#   unicode
from unicodedata import name, lookup
print(name('A'))
print(name('a'))

#   list
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
print(suits)
suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
print(suits)
print(original_suits)#一个对象的修改会反映到与之绑定的对象

#   dictionary
numerals = {'I': 1, 'V': 5, 'X': 10}
print(numerals['X'])
numerals['X'] = 11
print(numerals)
numerals['L'] = 50
print(numerals)
numerals.pop('X')
print(numerals.get('X'))
print(numerals)