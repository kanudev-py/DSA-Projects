TodoList = []
StatusList = []

while True:
    print("\n📋 To-Do Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option (1/2/3/4/5): ").strip()

    # View Tasks
    if choice == "1":
        if not TodoList:
            print("No tasks yet.")
        else:
            print("\n📝 Tasks:")
            for i, task in enumerate(TodoList, start=1):
                status = "✓" if StatusList[i-1] else "✗"
                print(f"{i}. {task} [{status}]")

    # Add Task
    elif choice == "2":
        tasks = input("Enter tasks separated by commas: ").strip()
        if tasks == "":
            print("You entered nothing.")
            continue

        task_list = [t.strip() for t in tasks.split(",") if t.strip()]
        TodoList.extend(task_list)
        StatusList.extend([False] * len(task_list))
        print("Tasks added successfully.")

    # Mark as Complete
    elif choice == "3":
        if not TodoList:
            print("No tasks to mark as complete.")
            continue
        print("\n Mark a task as completed:")
        for i, task in enumerate(TodoList, start=1):
            status = "✓" if StatusList[i-1] else "✗"
            print(f"{i}. {task} [{status}]")
        
        try:
            num = int(input("Enter the task number to mark complete: "))
            if 1 <= num <= len(TodoList):
                StatusList[num - 1] = True
                print(f"Task '{TodoList[num - 1]}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if not TodoList:
            print("No tasks to delete.")
            continue
        print("Delete a Task:")
        for i, task in enumerate(TodoList, start=1):
            status = "✓" if StatusList[i-1] else "✗"
            print(f"{i}. {task} [{status}]")
        
        try:
            num = int(input("Enter the task number to delete: "))
            if 1 <= num <= len(TodoList):
                removed_task = TodoList.pop(num - 1)
                StatusList.pop(num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Exiting To-Do App. Have a productive day!")
        break

    else:
        print("Invalid choice. Please select from the menu options.")
