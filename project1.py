def main():
    my_tasks = []

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            if not my_tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\n--- YOUR TASKS ---")
                for index, task in enumerate(my_tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "2":
            task_name = input("\nEnter task description: ").strip()
            if task_name:
                my_tasks.append(task_name)
                print(f"Task '{task_name}' added!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            print("\nExiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            
if __name__ == "__main__":
    main()
    