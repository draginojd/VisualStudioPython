def comment():
    '''This is a comment inside of a function''' # Use tripple quoteation mark to comment inside of a function
    print('Hello')

name = input('Whats\'s your name?')
# this is how you declare variables
# and input something in it
print('Hello ' + name + '!')
# but its nicer to use string interpolation (f-strings)
print(f'Hello {name}!')

# If...elif...else
if name == 'python':
    print('You are the best language!')
elif name == 'Java':
    print('You are a very structured language!')
else:
    print(f'{name} is a nice name!')

# Ternary operator
# Different from java and most languages
# In Java: condition? [value if true] : [value if false]
# In Python [value if true] if condition else [value if false]
print('You are a great' if name == 'Python' else 'You are ok!')

# There are no traditional for loops
# but here is the equivilent of for(i =1; i <= 10; i++)
for i in range(1, 11):
    # print(i, end=' ') # with spaces instead of line feed
    print(i, end=' ')

    counter = 1
    print('\n')  # \n stands for new line and is universal for all programming languages
    while counter <= 10:
        print(counter)
        counter += 1  # There are no ++ or --, use += 1 and -= 1
