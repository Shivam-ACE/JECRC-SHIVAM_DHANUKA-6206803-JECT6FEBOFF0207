import time

class TODO:
    todos = []
    
    def add_todo(self, desc):
        # desc = input("Enter the description of the TODO: ")
        self.todos.append({
            'desc': desc,
            'id': int(time.time()),
            'is_completed': False
        })
    
    def remove_todo(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                self.todos.remove(todo)
                return
        print("Task not found.")
        
    
    def display_todos(self):
        if len(self.todos) == 0:
            print("No tasks in the list.")
        else:
            print('To-Do List: ')
            for todo in self.todos:
                print(f'{todo["desc"]} {todo["id"]} {"(Completed)" if todo["is_completed"] else "(Pending)"}')

    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if todo['id'] == id:
                todo['desc'] = new_desc
                return
        print("Task not found.")
    
    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                    todo['is_completed'] = not todo['is_completed']
                    return

    def completed_todos(self):
        flag = False
        for todo in self.todos:
            if todo['is_completed']:
                flag = True
                print(f'{todo["desc"]} {todo["id"]}')
        if not flag:
            print("No completed tasks available.")
    
    def incompleted_todos(self):
        flag = False
        for todo in self.todos:
            if not todo['is_completed']:
                flag = True
                print(f'{todo["desc"]} {todo["id"]}') 
        if not flag:
            print("No pending tasks available.")
            