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

            """# Check files content with read (r) mode
            file = open('files/todos.txt', 'r')
            # Store the info in the todos list
            todos = file.readlines()
            # Close the file
            file.close() """

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Add more info at the bottom
            todos.append(todo)

            """# Open the file in write (w) mode
            file = open('files/todos.txt', 'w')
            # Adds the data to the file
            file.writelines(todos)
            # Closes the file
            file.close()"""

            with open('todox.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            # todos needs to be defined as if add is being skipped, it will crash the program
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            """# New list
            new_todos = []

            for item in todos:
                # The strip () method removes any leading, and trailing whitespaces.
                new_item = item.strip('\n')
            print(todos)"""

            """# List comprehension
            new_todos = [item.strip('\n') for item in todos]"""

            # enumerate() allows you to enumerate what it is inside the function
            for index, item in enumerate(todos):
                item = item.strip('\n')
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
