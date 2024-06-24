from functions import write_todos, get_todos
import PySimpleGUI as sg
import time
import os

if not os.path.exists('../todos_app/todos'):
    with open('../todos_app/todos', 'w') as file:
        pass

sg.theme('PythonPlus')

time_label = sg.Text('', key='time')
label = sg.Text("Type in a to-do ")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button(image_source=r'C:\Users\supra\PycharmProjects\App1\todos_app\add.png', key='Add', tooltip='add todo')
list_box = sg.Listbox(values=get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button(image_source=r'C:\Users\supra\PycharmProjects\App1\todos_app\complete.png', key='Complete', tooltip='mark complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-do App',
                   layout=[[time_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window['time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
# switch statement over button clicked
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select a todo to edit!", font=("Helvetica", 10))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select a todo to complete!", font=("Helvetica", 10))
        case "Exit":
            break
# for updating list box
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

