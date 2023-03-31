# import os

# # Define the file name for storing the to-do list items
# TODO_FILE = "todo.txt"

# # Define the main function for the to-do list application
# def main():
#     # Display the welcome message
#     print("Welcome to the To-Do List App!")
#     print("-" * 30)

#     # Load the existing to-do list items from the file
#     todos = load_todos()

#     # Display the current to-do list items
#     display_todos(todos)

#     # Ask the user for the next action
#     while True:
#         action = input("What would you like to do (add/update/delete/quit)? ").lower()
#         if action == "add":
#             add_todo_item(todos)
#         elif action == "update":
#             update_todo_item(todos)
#         elif action == "delete":
#             delete_todo_item(todos)
#         elif action == "quit":
#             break
#         else:
#             print("Invalid action. Please try again.")

#     # Save the updated to-do list items to the file
#     save_todos(todos)

#     # Display the goodbye message
#     print("Goodbye!")

# # Define the function for loading the to-do list items from the file
# def load_todos():
#     todos = []
#     if os.path.exists(TODO_FILE):
#         with open(TODO_FILE, "r") as f:
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     todos.append(line)
#     return todos

# # Define the function for displaying the current to-do list items
# def display_todos(todos):
#     if todos:
#         print("Current To-Do List:")
#         print("-" * 30)
#         for i, todo in enumerate(todos):
#             print(f"{i+1}. {todo}")
#         print("-" * 30)
#     else:
#         print("No to-do list items found.")

# # Define the function for adding a new to-do list item
# def add_todo_item(todos):
#     item = input("Enter the new to-do list item: ")
#     todos.append(item)
#     print(f"'{item}' added to the to-do list.")

# # Define the function for updating an existing to-do list item
# def update_todo_item(todos):
#     index = int(input("Enter the index of the to-do list item to update: "))
#     if 1 <= index <= len(todos):
#         item = input("Enter the updated to-do list item: ")
#         todos[index-1] = item
#         print(f"'{item}' updated in the to-do list.")
#     else:
#         print("Invalid index. Please try again.")

# # Define the function for deleting an existing to-do list item
# def delete_todo_item(todos):
#     index = int(input("Enter the index of the to-do list item to delete: "))
#     if 1 <= index <= len(todos):
#         item = todos.pop(index-1)
#         print(f"'{item}' deleted from the to-do list.")
#     else:
#         print("Invalid index. Please try again.")

# # Define the function for saving the updated to-do list items to the file
# def save_todos(todos):
#     with open(TODO_FILE, "w") as f:
#         for todo in todos:
#             f.write(todo + "\n")

# # Call the main function to start the application
# if __name__ == "__main__":
#     main()




#TO-DO LIST WITH ADD,DELETE,UPDATE,QUIT OPERATIONS:

# Initialize an empty list to hold the to-do items
todos = []

print("Welcome to the To-Do List App!")
print("-" * 30)

# Actions
while True:
    action = input("What would you like to do (add/update/delete/quit)? ").lower()

    #ADD
    if action == "add":
        item = input("Enter the new to-do list item: ")
        todos.append(item)
        print(f"'{item}' added to the to-do list.")

    #UPDATE
    elif action == "update":
        index = int(input("Enter the index of the item to update: "))
        if index >= 1 and index <= len(todos):
            item = input("Enter the new value: ")
            todos[index-1] = item
            print(f"'{item}' updated in the to-do list.")
        else:
            print("Invalid index.")

    #DELETE
    elif action == "delete":
        index = int(input("Enter the index of the item to delete: "))
        if index >= 1 and index <= len(todos):
            item = todos.pop(index-1)
            print(f"'{item}' deleted from the to-do list.")
        else:
            print("Invalid index.")

    #QUIT
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please try again.")
    
    # Display the updated to-do list
    print("-" * 30)
    print("To-Do List:")
    for index, item in enumerate(todos):
        print(f"{index+1}. {item}")
    print("-" * 30)


print("All the elements in the to-do list:")
for index, item in enumerate(todos):
    print(f"{index+1}. {item}")
