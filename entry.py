import PySimpleGUI as sg
import csv

# Nama file CSV

CSV_FILE = 'Pendaftaran.csv'

layout = [
    [sg.Text('Masukkan Data:')],
    [sg.Text('Nama', size=(15, 1)), sg.InputText(key='Nama')],
    [sg.Text('No Telp', size=(15, 1)), sg.InputText(key='Tlp')],
    [sg.Text('Alamat', size=(15, 1)), sg.Multiline(key='Alamat')],
    [sg.Text('Tgl Lahir', size=(15, 1)),
     sg.InputText(key='Tgl Lahir'),
     sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%M-%Y'))],
    [sg.Text('Jenis Kelamin', size=(15, 1)),
     sg.Combo(['pria', 'wanita'], key='Jenis Kelamin')],
    [sg.Text('Hobi', size=(15, 1)),
     sg.Checkbox('Main HP', key='Main HP'),
     sg.Checkbox('Nonton Drama', key='Nonton Drama'),
     sg.Checkbox('Mabar', key='Mabar')],
    [sg.Button('Submit'), sg.Button('Exit')]
]

window = sg.Window('Data Entry Form', layout)

while True:
    event, values = window.read() # data2 yg di dpt disimpen di event n values
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
    elif event == 'Submit':
        # Menyimpan data ke dalam file CSV
        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                values['Nama'],
                values['Tlp'],
                values['Alamat'],
                values['Tgl Lahir'],
                values['Jenis Kelamin'],
                values.get('Main HP', False),
                values.get('Nonton Drama', False),
                values.get('Mabar', False)
            ])
        sg.popup('Data berhasil disimpan ke dalam CSV!')
window.close()

