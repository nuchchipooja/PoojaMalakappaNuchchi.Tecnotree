
#Write a program that takes two lists of numbers and returns a new list with
#the elements that appear in both lists.
def common_elements(list1, list2):
    
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements_list = common_elements(list1, list2)
print("Common elements:", common_elements_list)