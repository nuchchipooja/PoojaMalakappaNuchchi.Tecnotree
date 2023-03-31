#Write a program that takes a string and returns the number of times each letter appears in the string.
def count_letters(string):
    letter_counts = {}
    for letter in string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts
string = input("Enter a string: ")
letter_counts = count_letters(string)
print(letter_counts)
