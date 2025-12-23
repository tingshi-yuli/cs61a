#元组：不可变的列表
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250 #报错，元组不支持修改元素

foods=('burger','potato chips','pizza','fried chicken')
for f in foods:
    print(f.title())
foods=('steak','soup','salad')
for f in foods:
    print(f.title())