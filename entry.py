import PySimpleGUI as sg
import csv
import os
import pandas as pd

sg.theme('DarkBlue')

CSV_FILE = 'Pendaftaran.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama', 'No Telp', 'Alamat', 'Tgl Lahir', 'Jenis Kelamin', 'Pekerjaan'])


layout = [
    [sg.Text('Masukkan Data Kamu: ')],
    [sg.Text('Nama', size=(15, 1)), sg.InputText(key='Nama')],
    [sg.Text('No Telp', size=(15, 1)), sg.InputText(key='Tlp')],
    [sg.Text('Alamat', size=(15, 1)), sg.Multiline(key='Alamat', size=(30, 3))],
    [sg.Text('Tgl Lahir', size=(15, 1)),
     sg.InputText(key='Tgl Lahir', size=(15, 1)),
     sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%m-%Y'))],
    [sg.Text('Jenis Kelamin', size=(15, 1)),
     sg.Combo(['pria', 'wanita'], key='Jenis Kelamin', size=(15, 1))],
    [sg.Text('Pekerjaan', size=(15, 1)),
     sg.Checkbox('Data Scientist', key='Data Scientist'),
     sg.Checkbox('Game Developer', key='Game Developer'),
     sg.Checkbox('Cyber Security', key='Cyber Security')],
    [sg.Button('Submit', size=(15, 1)), sg.Button('Clear', size=(15,1)), sg.Button('Exit', size=(15, 1))]
]

window = sg.Window('Posisi Pekerjaan Perusahaan', layout)

def bersihin():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()  
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
    elif event == 'Clear' :
        bersihin()
    elif event == 'Submit':
        
        if not values['Nama'].replace(" ", "").isalpha():
            sg.popup_error('Nama harus diisi dengan huruf!')
        elif not values['Tlp'].isdigit():
            sg.popup_error('Nomor Telepon harus berisi digit!')
        elif not values['Tgl Lahir']:
            sg.popup_error('Tanggal Lahir harus diisi!')
        elif not values['Jenis Kelamin']:
            sg.popup_error('Jenis Kelamin harus diisi!')
        elif not any(values[key] for key in ['Data Scientist', 'Game Developer', 'Cyber Security']):
            sg.popup_error('Pilih setidaknya satu Pekerjaan!')
        elif not values['Alamat']:
            sg.popup_error('Alamat harus diisi!')
        else:
            
            with open(CSV_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                
                writer.writerow([
                    values['Nama'],
                    values['Tlp'],
                    values['Alamat'],
                    values['Tgl Lahir'],
                    values['Jenis Kelamin'],
                    ', '.join([key for key in values.keys() 
                    if values[key] and key != 'Nama' and 
                    key != 'Tlp' and key != 'Alamat' and 
                    key != 'Tgl Lahir' and key != 'Jenis Kelamin'])
                ])
            sg.popup('Data berhasil disimpan!!!')
            bersihin()

window.close()
