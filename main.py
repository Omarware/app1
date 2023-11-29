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
            # Get the todo from the user
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # Add more info at the bottom
            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # enumerate() allows you to enumerate what it is inside the function
            for index, item in enumerate(todos):
                item = item.strip('\n')
                # f-strings == formatting-strings to change the output of the print
                row = f"{index + 1}--{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            # Complete was added and method pop() to delete
        case 'complete':

            number = int(input("Number of the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

                message = f"TODO {todo_to_remove} was removed from the list."
                print(message)

        case 'exit':
            break

print("Bye!")
