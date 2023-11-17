from typing import List

user_prompt = "Enter a todo: "

todos: list[str] = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
