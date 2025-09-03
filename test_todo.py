import unittest
from todo import TodoManager

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_add_todo(self):
        todo = self.manager.add_todo("Test Task")
        self.assertEqual(todo.title, "Test Task")
        self.assertFalse(todo.completed)

    def test_complete_todo(self):
        self.manager.add_todo("Test Task")
        result = self.manager.complete_todo(0)
        self.assertTrue(result)
        self.assertTrue(self.manager.todos[0].completed)

    def test_delete_todo(self):
        self.manager.add_todo("Test Task")
        result = self.manager.delete_todo(0)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.todos), 0)

    def test_list_todos(self):
        self.manager.add_todo("Task 1")
        self.manager.add_todo("Task 2")
        todos = self.manager.list_todos()
        self.assertEqual(len(todos), 2)

if __name__ == "__main__":
    unittest.main()