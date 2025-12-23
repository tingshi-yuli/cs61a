bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
#    -1表示最后一个元素

message="My first bicycle was a "+bicycles[0].title()+"."
print(message)

#   for循环
names=['Alice','Bob','Charlie','David','Eve']
for name in names:
    print(name)
    print(name.title()+", welcome to the party!")

vhicles=['walking','cycling','taking bus','taking a taxi']
for vhicle in vhicles:
    print("I like "+vhicle+" to company.")

#   修改列表
video_players=['bilibili','kazumi','potplayer','MXplayer','VLC']
print(video_players)
video_players[0]='YouTube'
print(video_players)
video_players.append('Netflix')
print(video_players)
video_players.insert(0,'Disney+')
print(video_players)
del video_players[1]
print(video_players)
popped_player=video_players.pop()
#默认弹出最后一个元素，也可以指定索引位置
print(video_players)
print(popped_player)
video_players.remove('kazumi')
print(video_players)

guests=['mjq','dcx','syx','lyw','yhx','hjl']
print(guests)
for guest in guests:
    print("Dear "+guest.title()+",I'd like to invite you to dinner.")
print(guest[1]+" can't come to the dinner.")
guests[1]='sjl'
for guest in guests:
    print("Dear "+guest.title()+",I'd like to invite you to dinner.")
print("I found a bigger dinner table!")
guests.insert(0,'jjs')
guests.insert(3,'sml')
guests.append('wxz')
for guest in guests:
    print("Dear "+guest.title()+",I'd like to invite you to dinner.")
print("Sorry, the new dinner table won't arrive in time. I can only invite two people for dinner.")
while len(guests)>2:
    remove_guest=guests.pop()
    print("Sorry "+remove_guest.title()+",I can't invite you to dinner.")
for guest in guests:
    print("Dear "+guest.title()+",you're still invited to dinner.")
del guests[0:2]    #[0:2]表示从索引0开始到索引2结束，但不包括索引2
print(guests)

#    组织列表
citys=['beijing','shanghai','guangzhou','shenzhen','hangzhou']
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)
print(sorted(citys))
citys.reverse()
print(citys)
print(len(citys))

travel_places=['Japan','America','England','France','Australia']
print(travel_places)
print(sorted(travel_places))
print(travel_places)
print(sorted(travel_places, reverse=True))
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort()
print(travel_places)
travel_places.sort(reverse=True)
print(travel_places)

print(len(guests))

#循环
pizzas=['pepperoni','mushrooms','green peppers','extra cheese']
for pizza in pizzas:
    print("I like "+pizza+" pizza")
print("I really love pizza!")

animals=['cat','dog','bird','sheep','chicken']
for animal in animals:
    print("A "+animal+" would make a great pet.")
print("Any of these animals would make a great pet!")

#数值列表
for value in range(1,5):
    print(value)
numbers=list(range(1,6))
print(numbers)
even_number=list(range(2,21,2))
print(even_number)
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
digits=[1,2,3,4,5,6,7,8,9,0]
minimum=min(digits)
maximum=max(digits)
total=sum(digits)
print(minimum)
print(maximum)
print(total)
# 列表解析
squares=[value**2 for value in range(1,11)]
print(squares)
giant_numbers=[]
for i in range (1,1000001):
    giant_numbers.append(i)
#    print(giant_numbers)这行会把电脑卡死
print(min(giant_numbers))
print(max(giant_numbers))
print(sum(giant_numbers))
odds=[i for i in range(1,21,2)]
print(odds)

#切片
tableware=['chopsticks','spoon','knife','fork','cup']
print(tableware[0:3])
print(tableware[1:4])
print(tableware[:3])
print(tableware[2:])
print(tableware[-3:])#从倒数第三个开始到最后
print(tableware[::-1])#倒序排列

#遍历切片
for item in tableware[1:4]:
    print(item.title())

#复制列表
my_stationery=['pen','pencil','eraser','ruler']
friend_stationery=my_stationery[:]
my_stationery.append('notebook')
friend_stationery.append('marker')
print("My stationery items:")
for item in my_stationery:
    print(item.title())
print("\nFriend's stationery items:")
for item in friend_stationery:
    print(item.title())

print("The first three items in the list are:")
for i in tableware[0:3]:
    print(i.title())
print("Three items from the middle of the list are:")
for i in tableware[1:4]:
    print(i.title())
print("The last three items in the list are:")
for i in tableware[-3:]:
    print(i.title())
