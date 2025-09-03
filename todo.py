class Todo:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} [{status}]"


class TodoManager:
    """
    Manages a list of Todo items, providing methods to add, list, complete, delete, and search todos.
    """
    def __init__(self):
        self.todos = []

    def add_todo(self, title):
        todo = Todo(title)
        self.todos.append(todo)
        return todo

    def list_todos(self):
        return self.todos

    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].mark_completed()
            return True
        return False

    def delete_todo(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            return True
        return False

    def search_todos(self, keyword):
        """
        Returns a list of todos whose titles contain the given keyword (case-insensitive).
        """
        return [todo for todo in self.todos if keyword.lower() in todo.title.lower()]