def remove_vowels(string):
   
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result


string = input("Enter a string: ")


new_string = remove_vowels(string)

print("New string without vowels:", new_string)
