#嵌套
#在列表中存储字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
import random

speeds = ['slow', 'medium', 'fast']
colors = ['green', 'yellow', 'red']
points = [5, 10, 15]
color_points = {'green': 5, 'yellow': 10, 'red': 15}

aliens = []
for i in range(30):
    index = random.randint(0, 2)
    alien = {
        'speed': speeds[index],
        'color': colors[index], 
        'points': points[index] 
    }
    aliens.append(alien)

for i, alien in enumerate(aliens[:5]):
    print(f"外星人{i+1}: 速度-{alien['speed']}, 颜色-{alien['color']}, 分数-{alien['points']}")

print(f"\n总共生成了{len(aliens)}个外星人")

#在字典中存储字典
botany = {
    'vegetables': {
       'tomato' :{'color': 'red', 'taste': 'sweet'},
       'potato' :{'color': 'brown', 'taste': 'starchy'},
       'carrot' :{'color': 'orange', 'taste': 'sweet'},
       'corn'   :{'color': 'yellow', 'taste': 'sweet'},
        },

    'fruits': {
       'apple'  :{'color': 'red', 'taste': 'sweet'},
        'banana' :{'color': 'yellow', 'taste': 'sweet'},
        'grape'  :{'color': 'purple', 'taste': 'sweet'},
        'lemon'  :{'color': 'yellow', 'taste': 'sour'},
        }
    }

for category, plants in botany.items():
    print(f"\n{category.upper()}:")
    for plant, info in plants.items():
        print(f"\t{plant.title()}: 颜色-{info['color']}, 味道-{info['taste']}")

#函数input()
name = input("请输入你的名字：")
print("你好，" + name + "!")
#Sublime Text不能运行提示用户输入的程序。你可以使用Sublime Text来编写提示用户输入的程序，但必须从终端运行它们。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")