import PySimpleGUI as sg
from zip_extractor import archive_extractor

sg.theme('Dark2')

label1 = sg.Text("Select archive ")
input_box1 = sg.InputText(tooltip="enter file path")
file_button = sg.FilesBrowse("select", tooltip="select file", key="file")

label2 = sg.Text("Select dest dir")
input_box2 = sg.InputText(tooltip="enter destination path")
dest_button = sg.FolderBrowse("select", tooltip="select folder", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", layout=[[label1, input_box1, file_button],
                                                [label2, input_box2, dest_button],
                                                [extract_button, output_label]])

while True:
    event, values = window.read()
    print('1', event)
    print('2', values)
    archivepath = values['file']
    dest_dir = values['folder']
    archive_extractor(archivepath, dest_dir)
    window['output'].update(value="Extraction Successful!")
    window.close()

