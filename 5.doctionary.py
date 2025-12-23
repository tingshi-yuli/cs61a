#字典
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print("you just earned " + str(alien_0['points']) + " points!")

#添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#根据外星人速度决定其位置的变化
speed = ['slow','medium','fast']
alien_0['speed'] = speed[1]
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#删除键-值对
del alien_0['color']
print(alien_0)

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
#保证中文能够正常输出

#遍历所有的键-值对
glossary = {
    'list': '一组有序的元素集合',
    'dictionary': '键值对的无序集合', 
    'loop': '重复执行某段代码的结构',
    'function': '可重复使用的代码块',
    'variable': '存储数据的容器'
}

for word, meaning in glossary.items():
    print(f"\n{word}:\n\t{meaning}")

#遍历字典中的所有键
for word in glossary.keys():#.keys()可以省略
#实际上，key()返回一个列表，其中包含字典中的所有键
    print(word.title())

#按顺序遍历字典中的所有键
for word in sorted(glossary.keys()):
    print(word.title())

#遍历字典中的所有值
for meaning in glossary.values():#.values()不能省略，否则遍历的是键
    print(meaning.title())

#遍历字典中的所有不同的值：使用集合.set()
for meaning in set(glossary.values()):
    print(meaning.title())