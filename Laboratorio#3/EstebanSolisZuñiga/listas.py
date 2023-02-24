my_list = [44, 97, 10, 24, 2, 68, 68]
print(my_list)

print(my_list.index(44))

my_list.append(47)
print(my_list)

my_list.insert(1, 33)
print(my_list)

my_list.remove(24)
print(my_list)

my_list.remove(68)
print(my_list)

my_list.pop()
print(my_list)

for x in my_list:
    print(x)

print("---------------")

for x in range(1,len(my_list)-2):
    print(my_list[x])