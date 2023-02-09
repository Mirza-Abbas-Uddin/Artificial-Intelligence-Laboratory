# list declaration
my_list = ['Mango', 'Banana', ' Apple', 'Banana']
print(my_list)

# set declaration: duplication is not allowed
my_set = {'Mango', 'Banana', ' Apple', 'Banana'}
print(my_set)

# True and 1 is considered the same value:
my_set = {'Mango', 'Banana', ' Apple', 'Banana', True, 1, 2}
print(my_set)
print(len(my_set))
print(type(my_set))

# Tuple Declaration
my_tuple = (1, 2, "Hello")
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))


# printing set values using loop
my_set = {"Mirza", "Abbas", "Uddin"}

for i in my_set:
    print(i, end=' ')
print()

# check weather Mirza is present or not:
print("Mirza" in my_set)

# add values in a set
my_set1 = {"Mirza", "Abbas"}
my_set2 = {"Tawsif", "Mahmood"}

my_set1.add("Uddin")
print(my_set1)

# add another set
my_set1.update(my_set2)
print(my_set1)

# join two sets
my_set3 = my_set1.union(my_set2)
print(f"My set3: {my_set3}")

# Keep ONLY the Duplicates
x = {1, 2, 3}
y = {2, 5, 4}
common_of_x_and_y = x.intersection(y)
print(f"Common Values:{common_of_x_and_y}")

# Remove Set Items
my_set1.remove("Uddin")
print(my_set1)

# using pop function : randomly removes values

my_set1.pop()
print(my_set1)

# make empty
my_set1.clear()
print(my_set1)

# delete set
del my_set1
del my_set2
# print(my_set1,my_set2) # Error : my_set1,my_set2 doesn't exist
