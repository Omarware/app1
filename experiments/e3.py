todos: list[str] = []

while True:
    user_action = input("Type add or show: ")
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
        # Bitwise or operator
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        # For not matching scenarios, please use _ for everything else
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
