from todos_app import functions as fun
import time

now = time.strftime("%d %b, %Y %H:%M:%S")
print("It is", now)

while True:
    # getting user input and removing trailing spaces
    user_action = input("Type add, edit, complete, show and exit : ")
    user_action = user_action.strip()

    todos = fun.get_todos()
    # adding new todo in the list
    if user_action.startswith('add'):

        todo = user_action[4:]
        todos.append(todo + '\n')

        fun.write_todos(todos)

    # editing the existing todo
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:])
            number -= 1
            existing_todo = todos[number]
            print(existing_todo.strip('\n'))
            new_todoo = input("Enter new todo: ")
            todos[number] = new_todoo + "\n"

            fun.write_todos(todos)

        except ValueError:
            print("Invalid Command!")
            ''' will only take input for editing
            user_action = input("Type add, edit, complete, show and exit : ")
            user_action = user_action.strip() '''
            continue
        except IndexError:
            print("There is no item with that number!")
            continue

    # removing todo from the list after completion
    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:])
            index -= 1
            todo_to_remove = todos[index]
            todos.pop(index)

            fun.write_todos(todos)

            msg = "Todo "+todo_to_remove.strip('\n')+" is removed."
            print(msg)

        except IndexError:
            print("There is no item with that number!")
            continue

    # displaying the current todo list
    elif user_action.startswith('show'):
        # new_todo = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command not valid!")

print("bye!")
