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
#字典的键(key)必须是可哈希的(hashable)
from collections.abc import Hashable
print(isinstance([1, 2], Hashable))#False
print(isinstance((1, 2), Hashable))#True

numerals = {'I': 1, 'V': 5, 'X': 10}
print(numerals['X'])
numerals['X'] = 11
print(numerals)
numerals['L'] = 50
print(numerals)
numerals.pop('X')#。pop()默认弹出最后一个
print(numerals.get('X'))
print(numerals)

#   tuple
#任何逗号隔开的东西都会被解释为元组
s = 3, 4, 5, 6
print(s)
#只包含一个元素
one = 1,
print(one)
print((2, 3, 4) + (9, 8 ,7))
print(5 in s)
tl = ([1, 2], 3)
print(tl[0])
print(tl[0][0])
#tl[0] = 4 不行
tl[0][0] = 4
print(tl)

#   identity and equality
print([10])
a = [10]
b = a
print(a is b)
print(a == b)
b = [10]
print(a == b)
print(a is b)#False

#   mutable default agruments are DANGEROUS
def f(s=[]):
    s.append(1)
    return len(s)
print(f())#1
print(f())#2
print(f())#3

#   funtion varies over time
def make_withdraw_list(balance):
    """创建一个可以记住余额的取款函数"""
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return "Insufficient funds"
        b[0] -= amount
        return b[0]
    
    return withdraw

# 测试代码
withdraw = make_withdraw_list(100)

print(withdraw(25))  # 输出: 75
print(withdraw(25))  # 输出: 50
print(withdraw(60))  # 输出: "Insufficient funds"
print(withdraw(15))  # 输出: 35