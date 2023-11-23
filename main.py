todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # Strip() The strip() method removes any leading, and trailing whitespaces.
    # Leading means at the beginning of the string, trailing means at the end.
    user_action = user_action.strip()

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
            # enumerate() allows you to enumerate what it is inside the function
            for index, item in enumerate(todos):
                # f-strings == formatting-strings to change the output of the print
                row = f"{index + 1 }--{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            # Complete was added and method pop() to delete
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")
