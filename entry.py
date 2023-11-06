import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGreen4')

EXCEL_FILE = 'Pendaftaran.xlsx'

df = pd.read_excel(EXCEL_FILE)

layout = [
[sg.Text('Masukkan Data: ')]
[sg.Text('Nama', size=(15,1)), sg.InputText(key='Nama')],
[sg.Text('No Telp', size=(15,1)), sg.InputText(key='Tlp')],
[sg.Text('Alamat', size=(15,1)), sg.Multiline(key='Alamat')],
[sg.Text('Tgl Lahir', size=(15,1)), sg.InputText(key='Tgl Lahir'),
                                        sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%M-%Y'))],
[sg.Text('Jenis Kelamin', size=(15,1)), sg.Combo(['pria','wanita'],key='Jenis Kelamin')]
[sg.Text('Hobi', size=(15,1)), sg.Checkbox('Main HP',key='Main HP'),
                                sg.Checkbox('Nonton Drama', key='Nonton Drama'),
                                sg.Checkbox('Mabar', key='Mabar')],






]