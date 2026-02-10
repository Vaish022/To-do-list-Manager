def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
