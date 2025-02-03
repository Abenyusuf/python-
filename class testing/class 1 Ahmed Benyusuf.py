a = 1
dir(a)
b = 2
print(a.__add__(b))
num1 = 5
print(num1)
num2 = 5.0
print(num2)
num3 = "sdaf"
print(num3)
immutable_float = 1.0
print(immutable_float)
new_float = immutable_float + 1.0
print(new_float)
immutable_float += 1.0
print(immutable_float)
# immutable_float = 3.14
# immutable_float.append(2.7)
# immutable_float.append(2.7)
# ^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'float' object has no attribute 'append'
immutable_string = "hello"
# immutable_string[0] = "c" = Error

# using a list
my_list = [1, 4.5, "hello"]
print(my_list)
# add to a list
my_list.append("hi")
print(my_list)
# add at specific position
my_list.insert(2, 3)
print(my_list)
# remove from a list
print(my_list)
removed_item = my_list.pop(3)
print(removed_item)
print(my_list)
my_list.pop(3)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
del my_list[2]
print(my_list)
index_1 = my_list.index(4.5)
print(index_1)
index_1 = my_list.index(3)
print(index_1)
# I had a Wi-Fi issue that I spoke about with you, I believe you should remember.

# create sets
set_a = {1, 2, 3, }
set_b = {4, 5, 6, }
print(set_a)
print(set_b)
# union
union_set = set_a.union(set_b)
print(union_set)
# add to set
set_b.add(2)
print(set_b)
# intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)
# remove
set_b.remove(2)
print(set_b)

# create person dict
my_person = {"name": "John Doe",
             "age": 54,
             "city": "kansas"}
print(my_person)
person_name = my_person["name"]
print(person_name)

# modify values using keys

my_person["age"] = 40
print(my_person["age"])
# adding a new key value pair
my_person["gender"] = "male"
print(my_person["gender"])
# get a list of keys
print(my_person.keys())
# get a list of values
print(my_person.values())
# use items method to get list of key values
items_list = my_person.items()
print(items_list)


# functions
def contains(data, target):
    count = 0
    for i in data:
        if i == target:
            count += 1
            # return True
        return count


my_list = ['2', '4', '4']
print(contains(my_list, '2'))
