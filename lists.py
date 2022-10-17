# This is how you create a list in Python.


names = ['Erik', 'Felicia', 'Gunnar', 'Helena']

print(names[0])  # 0-index, so names [0] == 'Erik'
print('\n')

print(len((names)))  # len = length and in this case its 4


# loop trough all items in the list #this is a for each loop from java but written in python.
def print_names():
    print('\nnames:')
    for name in names:
        print(name)


# Add a new name to the list without declaring where to create it.
names.append('Ivar')
print_names()

# add at the end of the list
print('\nnames again:')
for name in names:
    print(name)

# add at the beginning of the list/loop
print('\nnames again:')
for name in names:
    print(name)

print_names()

# add Frey before Gunnar
gunnar_index = names.index('Gunnar')  # -> 3
names.insert(gunnar_index, 'Frey')
print_names()

# remove items by value (first occurance)
names.remove('Helena')
print_names()

# remove the person at index 1 (second from top)
erased_name = names.pop(1)
print(f'I erased {erased_name}...')
print_names()

# remove the last item
erased_name_2 = names.pop()
print(f'I erased {erased_name_2}...')

# remove item at index 1
# without returning the removed item
del names[1]
print_names()

# Get a new list with from index 1 to index 2
print(names[1:2])

# Get a new list with items from index 1 to end of list
print(names[1:])


names = ['Anna',
         'Beata',
         'Cecilia',
         'David',
         'Erik',
         'Fredrik'
         ]
# Last name -> Erik
print(names[-1])

# Next to last name -> Erik
print(names[-2])

# Slicing
print(f'First three names:   {names[:3]}')
print(f'Last three names:    {names[3:]}')
print(f'Names in the middle: {names[2:4]}')

# Reverse with slicing
# (because third argument is step)
print(f'Reversed: {names[::-1]}')
# or (probably)
print(f'Reversed: {list(reversed(names))}')
