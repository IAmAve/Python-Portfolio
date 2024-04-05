import json
import os

DATA_FILE = '../data/tasks.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def view_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)

def user_interface_add_task():
    task = input('Enter task: ')
    add_task(task)
    print('Task added successfully.')

def user_interface_view_tasks():
    print('Tasks:')
    view_tasks()

def user_interface_remove_task():
    index = int(input('Enter index of task to remove: '))
    remove_task(index)
    print('Task removed successfully.')

def main():
    while True:
        print('\nTodo List Application')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            user_interface_add_task()
        elif choice == '2':
            user_interface_view_tasks()
        elif choice == '3':
            user_interface_remove_task()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()