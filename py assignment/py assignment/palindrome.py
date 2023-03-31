# check if a string is a palindrome
def is_palindrome(string):
    # compare the string to its reverse
    if string == string[::-1]:
        
        return True
    else:
        
        return False

strings = input("Enter a list of strings, separated by spaces: ")

strings_list = strings.split()

# empty list to store the palindromes
palindromes = []

for string in strings_list:
    # check if the string is a palindrome
    if is_palindrome(string):
      
        palindromes.append(string)
print(palindromes)
