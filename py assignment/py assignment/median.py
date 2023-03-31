#median of the list of numbers
def median(numbers):
    
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        # even number of elements,average of the two middle values
        middle_right = length // 2
        middle_left = middle_right - 1
        return (numbers[middle_left] + numbers[middle_right]) / 2
    else:
        #  odd number of elements, return the middle value
        middle = length // 2
        return numbers[middle]

numbers = [1, 2, 7, 4, 5,13]
median_value = median(numbers)
print("Median value:", median_value)
