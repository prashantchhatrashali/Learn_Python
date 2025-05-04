#Python Assignment: Simple To-Do List Manager
#Create a command-line to-do list application that allows users to add tasks,
# view tasks, mark tasks as complete, and exit the program.

'''
to_do=[]
user_input=int(input("Please enter your choice\n 1 - Add Task\n 2 - View Task\n 3 - Mark Task as completed\n 4 - Exit \n"))

while True:
    if user_input==1:
        task_1=input("Please enter task to be Added: \n")
        to_do.append(task_1)
        print("Task is added to the to_do list")
        var=input("Do you want to add more task (Yes/No): \n")
        if var =="Yes":
            to_do.append(task_1)
            print("Task is added to the to_do list")
            print(to_do)
        else:
            break
    elif user_input==2:
        print(to_do)

    elif user_input==3:
        print("Task is marked completed.")

    elif user_input==4:
        print("Exiting the Application. Thank you!")
        break


'''

to_do = []

while True:
    # Display menu every time
    print("\n===== To-Do List Manager =====")
    print("1 - Add Task")
    print("2 - View Task")
    print("3 - Mark Task as completed")
    print("4 - Exit")
    print("=============================")

    # Get user choice inside the loop
    user_input = input("Please enter your choice (1-4): ")

    # Convert to integer, with error handling
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number (1-4)")
        continue

    if user_input == 1:
        while True:
            task = input("Please enter task to be Added: ")
            to_do.append({"task": task, "completed": False})
            print("Task is added to the to_do list")

            var = input("Do you want to add more tasks? (Yes/No): ").strip().lower()
            if var != "yes":
                break

    elif user_input == 2:
        if len(to_do) == 0:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, item in enumerate(to_do, 1):
                status = "✓" if item["completed"] else "□"
                print(f"{i}. [{status}] {item['task']}")

    elif user_input == 3:
        if len(to_do) == 0:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, item in enumerate(to_do, 1):
                status = "✓" if item["completed"] else "□"
                print(f"{i}. [{status}] {item['task']}")

            try:
                task_num = int(input("\nEnter the number of the task to mark as completed: "))
                if 1 <= task_num <= len(to_do):
                    to_do[task_num - 1]["completed"] = True
                    print(f"Task '{to_do[task_num - 1]['task']}' marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif user_input == 4:
        print("Exiting the Application. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")





