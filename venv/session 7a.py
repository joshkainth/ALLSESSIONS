file = open("Session 7.py","r")
# data = file.read()
# print(data)
# print(type(data)) 

lines = file.readlines()
print(lines)
print(type(lines))

count = 0

for i in lines:
    print(i)
    if i.startswith("#"):
        count = count+1

print("Comments with # are {} in number".format(count))