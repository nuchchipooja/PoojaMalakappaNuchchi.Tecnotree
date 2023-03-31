#Write a program that takes a list of words and returns the longest word in
#the list.
def find_longest_word(words):
    
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


words = input("Enter a list of words, separated by spaces: ").split()
longest_word = find_longest_word(words)
print("The longest word is:", longest_word)
