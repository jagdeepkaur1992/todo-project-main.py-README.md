# To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed}' deleted!\n")
        else:
            print("Invalid task number!\n")
    except:
        print("Please enter a valid number!\n")

def menu():
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    menu()