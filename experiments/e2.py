
user_prompt = "Enter a todo: "

todos: list[str] = []

if len(user_prompt) <= 1:
    todo = input(user_prompt)
    # capitalize() will capitalize the first word of the string
    print(todo.capitalize())
    todos.append(todo)
else:
    todo = input(user_prompt)
    # title() will capitalize each word of the string
    print(todo.title())
    todos.append(todo)
