# импортируем библиотеку tkinter всю сразу
from tkinter import *
from tkinter import messagebox

# главное окно приложения
window = Tk()
# заголовок окна
window.title('Авторизация')
# размер окна
window.geometry('460x230')
# можно ли изменять размер окна - нет
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


# обработчик нажатия на клавишу 'Войти'
def clicked():

    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()
# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

# метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)


# запускаем главный цикл окна
window.mainloop()