
my_string = "abcdef"
interval = my_string[3:5]
print(interval)

my_list = [3, 5, 1, 6, 4, 7]
my_list[3] = 8   # my_list == [3, 5, 1, 8, 4, 7]
print(my_list[2:])

my_set = {1, 2, 3, 1, 2}.union({1, 6})   # my_set == {1, 2, 3, 6}
print(my_set)

my_tuple = (1, 2) + (1, 4, 5)
print(my_tuple)
list1 = list(my_tuple)
print(list1)
set1 = set(my_tuple)
print(set1)
print(list(set1))

map1 = {1: "one", 2: "two", 3: "three"}
for i in map1:
    print(map1[i])

print(map1)

map2 = {1: "one", 2: "two"}
print(map2)

