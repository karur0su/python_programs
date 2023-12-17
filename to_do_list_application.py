import os

# Function to display the current to-do list
def show_todo_list(todo_list):
    print("\n--- To-Do List ---")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print("------------------\n")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    show_todo_list(todo_list)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed_task = todo_list.pop(index)
        print(f"Task '{removed_task}' removed from the to-do list.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

# Function to save the to-do list to a file
def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(task + "\n")

# Function to load the to-do list from a file
def load_from_file(filename="todo_list.txt"):
    todo_list = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            todo_list = [line.strip() for line in file.readlines()]
    return todo_list

# Main function to run the To-Do List Application
def main():
    todo_list = load_from_file()

    while True:
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            remove_task(todo_list)
        elif choice == "4":
            save_to_file(todo_list)
            print("To-Do List saved. Quitting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

