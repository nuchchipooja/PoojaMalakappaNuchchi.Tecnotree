#Write a program that takes a list of numbers and returns a new list with the elements squared.
numbers = input("Enter a list of numbers, separated by spaces: ")
squared_numbers = [int(num) ** 2 for num in numbers.split()]
print(squared_numbers)
