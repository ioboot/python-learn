import re

a= r"www"
match = re.search(a,"www.baidu.com")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    print(type(match.group()))

phone = "2004-959-559 #This is a phone number."
num = re.sub(r"#.*$","",phone)
print("The phone number is: ",num)
num = re.sub(r"\D","",num)
print("The phone number is: ",num)

