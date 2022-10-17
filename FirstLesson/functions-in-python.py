# A definition of a function
# with one argument value 'Jane Doe'
# that will be used if someone calls  #Indrag is very important in Python!
# the function without the argument
def say_hello(name='Jane Doe'):
    return f'Hello {name}!'


print(say_hello('Anna'))
print(say_hello('Beata'))
say_hello(())

