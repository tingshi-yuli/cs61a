message="asdf ghjkl"
print(message.title())
#  .title() 首字母大写
print(message.upper())
print(message.lower())
#  .upper() 全部大写
#  .lower() 全部小写

first_name="John"
last_name="Smith"
full_name=first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")
#  py以“+”拼接字符串str

print("\tPython")
print("Language:\nPython\nC++\nJavaScript")
print("Language:\n\tPython\n\tC++\n\tJavaScript")
#  \t添加制表符  \n添加换行符 \n\t

language=' python '
print(language)
print(language.rstrip())
#    .rstrip()删除字符串末尾的空白字符
print(language.lstrip())
#    .lstrip()删除字符串开头的空白字符
print(language.strip())
#    .strip()删除字符串开头和末尾的空白字符
print(language)
#    原字符串并没有改变
language=language.strip()
print(language)
#    将删除空白字符后的字符串重新赋值给原变量

name='Eric'
print("Hello "+name.strip()+", would you like to learn some Python today?")
greatman='Albert Einstein '
wisdomsaying="A person who never made a mistake never tried anything new."
print(greatman.title().strip()+' once said,"'+wisdomsaying+'"')

#    number calculations
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(3**2)
print(10**5)
print(2+3*4)
print((2+3)*4)
print(0.1+0.2)

#    use function str()
age=18
message="Happy "+str(age)+"rd Birthday!"
print(message)