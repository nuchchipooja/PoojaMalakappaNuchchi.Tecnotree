def sum_of_even_numbers(numbers):
    """
    Calculates the sum of all even numbers in a given list of integers.
    """
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_evens = sum_of_even_numbers(numbers)
print("Sum of even numbers:", sum_of_evens)
