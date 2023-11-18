todos: list[str] = []

while True:
    user_action = input("Type add or show: ")

    '''
    Match-Case is the Switch Case of Python.
    Here we have to first pass a parameter then try to check with which case the parameter is getting satisfied. 
    If we find a match we will do something and if there is no match at all we will do something else.
    '''
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Bye!")
