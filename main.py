while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # Strip() The strip() method removes any leading, and trailing whitespaces.
    # Leading means at the beginning of the string, trailing means at the end.
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # Add more info at the bottom
        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # enumerate() allows you to enumerate what it is inside the function
        for index, item in enumerate(todos):
            item = item.strip('\n')
            # f-strings == formatting-strings to change the output of the print
            row = f"{index + 1}--{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    # Complete was added and method pop() to delete
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

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
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("Bye!")
