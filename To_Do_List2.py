tasks = []

def add_task():
    while True:
        task = input("Please enter a task: ")
        if task.strip():  # Check if the task is not empty (strip() removes any leading/trailing whitespace)
            tasks.append(task)
            print(f"\nTask '{task}' has been added to the list")
            break  # Exit the loop once the task is added
        else:
            print("Task not entered. Try again.")

def list_tasks():
    if not tasks:
        print("\nTo-Do list is empty :(")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def delete_task():
    list_tasks()
    if tasks:  # Only prompt for deletion if there are tasks
        try:
            task_to_delete = int(input("Enter the task number to delete: "))
            if 0 <= task_to_delete < len(tasks):
                confirmation = input(f"Are you sure you want to delete task #{task_to_delete} ('{tasks[task_to_delete]}')? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    tasks.pop(task_to_delete)
                    print(f"\nTask #{task_to_delete} has been removed.")
                else:
                    print("Deletion canceled.")
            else:
                print(f"Task #{task_to_delete} was not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def display_menu():
    print("\nPlease select one of the following options:")
    print("----------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        else: 
            print("Invalid input. Please try again...")

    print("Goodbye!!! 👋🏼")
