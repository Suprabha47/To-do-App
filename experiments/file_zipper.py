import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.InputText()
choose_button1 = sg.Button("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.InputText()
choose_button2 = sg.Button("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[[label1, input1, choose_button1],
                                          [label2, input2, choose_button2],
                                          [compress_button]])

window.read()
window.close()