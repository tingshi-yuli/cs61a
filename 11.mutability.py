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
nest = list(suits)#复制一个与 suits 相同的列表
nest[0] = suits
print(nest)
suits.insert(2, 'Joker')
print(nest)
nest[0].pop(2)
print(suits)
# 设置标准输出为UTF-8
import sys
import io
import locale
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')
print([lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])

#   dictionary
#字典的键(keys)必须是可哈希的(hashable)
from collections.abc import Hashable
print(isinstance([1, 2], Hashable))#False
print(isinstance((1, 2), Hashable))#True

numerals = dict([('I', 1), ('V', 5), ('X', 10)])#{'I': 1, 'V': 5, 'X': 10}
print(numerals['X'])
numerals['X'] = 11
print(numerals)
numerals['L'] = 50
print(numerals)
numerals.pop('X')#。pop()默认弹出最后一个
print(numerals.get('X'))
print(numerals)
def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which
    match(k, v) is a true value.
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    """
    return {keys: v for v in values if match(k, v) for k in keys}

#   tuple
#任何逗号隔开的东西都会被解释为元组
s = 3, 4, 5, 6
print(type(s))
print(s)
print(())
#只包含一个元素
one = 1,
print(one)
num = (2, 5, 8) + (9, 8 ,5) * 2
print(num)
print(len(num))
print(num[3])
print(num.count(5))
print(num.index(8))
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
    def withdraw(amount):
        nonlocal balance
        """当 balance 属性为声明为 nonlocal 后，每当它的值发生更改时，
        相应的变化都会同步更新到 balance 属性第一次被声明的位置。
        效果：当前执行帧之外的变量可以通过赋值语句更改。"""
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    return withdraw

# 测试代码
withdraw = make_withdraw_list(100)

print(withdraw(25))  # 输出: 75
print(withdraw(25))  # 输出: 50
print(withdraw(60))  # 输出: "Insufficient funds"
print(withdraw(15))  # 输出: 35