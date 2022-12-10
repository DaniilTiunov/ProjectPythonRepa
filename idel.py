import PySimpleGUI as sg
'''
sg.theme('DarkBlue')
layout = [ [sg.Button('Регистрация'), sg.Button('Авторизация')]

]
window = sg.Window('Window tittle', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('Вы вошли', values[0])
window.close()
'''
event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
