import PySimpleGUI as sg
import csv
import os

CSV_FILE = 'Pendaftaran.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama', 'No Telp', 'Alamat', 'Tgl Lahir', 'Jenis Kelamin', 'Pekerjaan'])

layout = [
    [sg.Text('', size=(19, 1)), sg.Text('POSISI PEKERJAAN', font=('Comic Sans MS', 22), justification='center')],
    [sg.Text('', size=(22, 1)), sg.Text('PERUSAHAAN', font=('Comic Sans MS', 22), justification='center')],
    [sg.Text('Nama', size=(15, 1), font=('Comic Sans MS', 18)), sg.InputText(key='Nama', size=(30, 1), font=('Comic Sans MS', 18))],
    [sg.Text('No Telp', size=(15, 1), font=('Comic Sans MS', 18)), sg.InputText(key='Tlp', size=(30, 1), font=('Comic Sans MS', 18))],
    [sg.Text('Alamat', size=(15, 1), font=('Comic Sans MS', 18)), sg.Multiline(key='Alamat', size=(30, 3), font=('Comic Sans MS', 18))],
    [sg.Text('Tgl Lahir', size=(15, 1), font=('Comic Sans MS', 18)),
     sg.InputText(key='Tgl Lahir', size=(15, 1), font=('Comic Sans MS', 18)),
     sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%m-%Y'), font=('Comic Sans MS', 18))],
    [sg.Text('Jenis Kelamin', size=(15, 1), font=('Comic Sans MS', 18)),
     sg.Combo(['pria', 'wanita'], key='Jenis Kelamin', size=(15, 1), font=('Comic Sans MS', 18))],
    [sg.Text('Pekerjaan', size=(15, 1), font=('Comic Sans MS', 18)),
     sg.Checkbox('Data Scientist', key='Data Scientist', font=('Comic Sans MS', 18)),
     sg.Checkbox('Game Developer', key='Game Developer', font=('Comic Sans MS', 18)),
     sg.Checkbox('Cyber Security', key='Cyber Security', font=('Comic Sans MS', 18))],
    [sg.Button('Submit', size=(15, 1), font=('Comic Sans MS', 18)), sg.Button('Exit', size=(15, 1), font=('Comic Sans MS', 18))]
]

window = sg.Window('Data Entry Form', layout, font=('Comic Sans MS', 18))

while True:
    event, values = window.read()  
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
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

window.close()
