import PySimpleGUI as sg
from convertor_function import convert

sg.theme('Black')

label1 = sg.Text('Enter feet ')
input_feet = sg.InputText(tooltip='enter feet value', key='feet')

label2 = sg.Text('Enter inches')
input_inches = sg.InputText(tooltip='enter inches', key='inches')

convert_button = sg.Button('Convert')
output_label = sg.Text('', key='output')
exit_button = sg.Button('Exit', key='exit')

window = sg.Window('Convertor', layout=[[label1, input_feet],
                                        [label2, input_inches],
                                        [convert_button, output_label],
                                        [exit_button]])

while True:
    event, values = window.read()
    print('1', event)
    print('2', values)
    feet = float(values['feet'])
    inches = float(values['inches'])
    result = convert(feet, inches)
    window['output'].update(value=f"{result}m")
    if event == sg.WIN_CLOSED or event == 'exit':
        break
window.close()

