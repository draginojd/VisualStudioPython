numbers = [1, 101, 3, 50, 102, 1373, 9, 32]

# filter using list comprehension
numbers_bigger_than_100 =\
    [x for x in numbers if x > 100]  # (if you want to make less change the > to <)

print(numbers_bigger_than_100)
