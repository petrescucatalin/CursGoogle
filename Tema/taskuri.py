import datetime
import os
import json

class ToDoList:
    def __init__(self):
        self.categories = set()
        self.tasks = []

    def add_category(self, category):
        if category in self.categories:
            print("Categoria deja exista.")
        else:
            self.categories.add(category)

    def add_task(self, task, deadline, person, category):
        if category not in self.categories:
            print("Error: Categoria nu exista.")
            return

        if any(t['task'] == task for t in self.tasks):
            print("Eroare: Taskul cu acelasi nume deja exista.")
            return

        self.tasks.append({
            'task': task,
            'deadline': deadline.isoformat(),
            'person': person,
            'category': category
        })

    def save_data(self):
        with open('categories.json', 'w') as f:
            json.dump(list(self.categories), f)

        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_data(self):
        if os.path.exists('categories.json'):
            with open('categories.json', 'r') as f:
                self.categories = set(json.load(f))

        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)

    def display_data(self):
        print("\nTasks:")
        for i, task in enumerate(self.tasks):
            task_id = i + 1
            print(f"Task ID: {task_id}")
            print(task)

    def sort_data(self, option):
        if option == 1:
            self.tasks.sort(key=lambda x: x['task'])
        elif option == 2:
            self.tasks.sort(key=lambda x: x['task'], reverse=True)
        elif option == 3:
            self.tasks.sort(key=lambda x: (x['deadline'], x['task']))
        elif option == 4:
            self.tasks.sort(key=lambda x: (x['deadline'], x['task']), reverse=True)
        elif option == 5:
            self.tasks.sort(key=lambda x: (x['person'], x['task']))
        elif option == 6:
            self.tasks.sort(key=lambda x: (x['person'], x['task']), reverse=True)
        elif option == 7:
            self.tasks.sort(key=lambda x: (x['category'], x['task']))
        elif option == 8:
            self.tasks.sort(key=lambda x: (x['category'], x['task']), reverse=True)

    def filter_data(self, option, value):
        if option == 1:
            filtered_tasks = [t for t in self.tasks if value in t['task']]
        elif option == 2:
            filtered_tasks = [t for t in self.tasks if value in str(t['deadline'])]
        elif option == 3:
            filtered_tasks = [t for t in self.tasks if value in t['person']]
        elif option == 4:
            filtered_tasks = [t for t in self.tasks if value in t['category']]

        print("\nFiltered Tasks:")
        for task in filtered_tasks:
            print(task)

    def edit_task(self, task_id, field, value):
        if field not in {'task', 'deadline', 'pers8on', 'category'}:
            print("Camp invalid.")
            return

        task_id -= 1  # Adjust for zero-indexing
        if task_id < 0 or task_id >= len(self.tasks):
            print("Task ID invalid.")
            return

        task = self.tasks[task_id]
        if field == 'category' and value not in self.categories:
            print("Eroare: Categoria nu exista.")
            return

        task[field] = value

    def delete_task(self, task_id):
        task_id -= 1  # Adjust for zero-indexing
        if task_id < 0 or task_id >= len(self.tasks):
            print("Task ID invalid.")
            return

        del self.tasks[task_id]

def main():
    todo_list = ToDoList()
    todo_list.load_data()

    while True:
        print("\nMenu:")
        print("1. Adauga categorie")
        print("2. Adauga task")
        print("3. Afiseaza datele")
        print("4. Sorteaza datele")
        print("5. Filtreaza datele")
        print("6. Editeaza taskul")
        print("7. Sterge taskul")
        print("8. Salveaza si iesi")

        choice = int(input("Introdu alegerea ta: "))

        if choice == 1:
            category = input("Introdu categoria: ")
            todo_list.add_category(category)
            todo_list.save_data()

        elif choice == 2:
            task = input("Introdu task-ul: ")
            deadline_str = input("Introduce deadline-ul: (dd.mm.yyyy hh:mm): ")
            deadline = datetime.datetime.strptime(deadline_str, "%d.%m.%Y %H:%M")
            person = input("Introdu persoana responsabila: ")
            category = input("Introdu categoria: ")
            todo_list.add_task(task, deadline, person, category)
            todo_list.save_data()

        elif choice == 3:
            todo_list.load_data()
            todo_list.display_data()
            todo_list.save_data()

        elif choice == 4:
            option = int(input("Introdu optiunea de sortare (1-8): "))
            todo_list.sort_data(option)
            todo_list.save_data()

        elif choice == 5:
            option = int(input("Introdu campul de filtrare (1-4): "))
            value = input("Introdu valoarea de filtrare: ")
            todo_list.filter_data(option, value)
            todo_list.save_data()

        elif choice == 6:
            task_id = int(input("Introdu ID-ul taskului: "))
            field = input("Introdu field-ul pe care il editezi (task, deadline, person, category): ")
            value = input("Introdu valoarea noua: ")
            if field == 'deadline':
                value = datetime.datetime.strptime(value, "%d.%m.%Y %H:%M")
            todo_list.edit_task(task_id, field, value)
            todo_list.save_data()

        elif choice == 7:
            task_id = int(input("Introdu ID-ul task-ului: "))
            todo_list.delete_task(task_id)
            todo_list.save_data()

        elif choice == 8:
            todo_list.save_data()
            break

        else:
            print("Optiune invalida.")

if __name__ == "__main__":
        main()
