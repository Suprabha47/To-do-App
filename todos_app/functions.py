FILEPATH = 'todos'


def get_todos(filepath=FILEPATH):
    # opening todos file and saving the content in todos list
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print("Hello")

