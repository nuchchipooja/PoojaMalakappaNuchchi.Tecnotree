# write a python program that uses lambda functions and list comprehensions to filter out even numbers
# from the list and double the remaining odd numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [2*x for x in nums if x % 2 != 0]

print(result)

# write a python program that uses lambda functions and list comprehensions to filter out odd numbers
# from the list and double the remaining even numbers

nums = [0,-1,1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(map(lambda x: 2*x, filter(lambda x: x % 2 == 0, nums)))    #lambda&filter fun

print(result)
