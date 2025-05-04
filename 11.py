# Simple To-Do List Manager

def display_menu():
    """Display the menu options to the user."""
    print("\n===== To-Do List Manager =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")
    print("=============================")


def add_task(todo_list):
    """Add a new task to the to-do list."""
    task = input("Enter a new task: ")
    # TODO: Add the task to the todo_list with a "Not completed" status


def view_tasks(todo_list):
    """Display all tasks with their status."""
    # TODO: Display all tasks with their numbers and completion status
    # If there are no tasks, print a message saying so


def mark_complete(todo_list):
    """Mark a task as complete."""
    # TODO: Ask the user for the task number to mark as complete
    # Update the task's status to "Completed"
    # Handle cases where the user enters an invalid task number


def main():
    """Main program loop."""
    todo_list = []  # List to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        # TODO: Implement the logic for each menu option
        # Call the appropriate function based on the user's choice
        # Exit the loop if the user chooses option 4


if __name__ == "__main__":
    main()