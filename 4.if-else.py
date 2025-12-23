#条件测试
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#if-else语句
age = 18
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")

#if-elif-else链
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $"+str(price)+".")

#多个elif代码块
age = 68
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:#else亦可
    price = 5
print("Your admission cost is $"+str(price)+".")

#良好的格式设置习惯:在诸如== 、>= 和<= 等比较运算符两边各添加一个空格,让代码阅读起来更容易。

alien_color = 'green'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
print("you get "+str(score)+" points")

#确认列表非空
requested_toppings = []
if requested_toppings:
#在if 语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False 。
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza!")

user_names = ['admin','john','mary','susan','peter']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+user_name+",thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['john','mary','susan','peter','admin']
new_users = ['mike','susan','anna','peter','tom']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
    #检查小写的新用户名是否存在于小写的现有用户列表中（不区分大小写）
        print("The username '"+new_user+"' is already taken. Please enter a new username.")
    else:
        print("The username '"+new_user+"' is available.")

ordinal_numbers = [i for i in range(1,10)]
for i in ordinal_numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(str(i)+"th")