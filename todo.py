import os

FILE_NAME = "tasks.txt"

def add_task(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added.")

def view_tasks():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task(task_number):
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        task = tasks.pop(task_number - 1).strip()
        with open(FILE_NAME, "w") as file:
            file.writelines(tasks)
        print(f"Task '{task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
