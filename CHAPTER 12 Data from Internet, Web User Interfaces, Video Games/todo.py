import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|delete] [args]")
        return
    
    command = sys.argv[1]
    filename = "todo.txt"
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task to add.")
            return
        
        task = sys.argv[2]
        
        with open(filename, 'a') as f:
            f.write(task + '\n')
        
        print("Task added.")
    
    elif command == "list":
        if not os.path.exists(filename):
            print("No tasks.")
            return
        
        with open(filename, 'r') as f:
            tasks = f.readlines()
        
        if len(tasks) == 0:
            print("No tasks.")
            return
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    
    elif command == "show":
        if not os.path.exists(filename):
            print("No tasks.")
            return
        
        with open(filename, 'r') as f:
            tasks = f.readlines()
        
        if len(tasks) == 0:
            print("No tasks.")
            return
        
        for task in tasks:
            print(task.strip())
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task number to delete.")
            return
        
        try:
            task_number = int(sys.argv[2])
        except ValueError:
            print("Error: Task number must be an integer.")
            return
        
        if not os.path.exists(filename):
            print("Error: No tasks to delete.")
            return
        
        with open(filename, 'r') as f:
            tasks = f.readlines()
        
        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return
        
        tasks.pop(task_number - 1)
        
        with open(filename, 'w') as f:
            f.writelines(tasks)
        
        print("Task deleted.")
    
    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, list, show, delete")

if __name__ == "__main__":
    main()
