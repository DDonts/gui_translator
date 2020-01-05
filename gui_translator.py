from tkinter import *
from googletrans import Translator, constants
from tkinter import ttk

win = Tk()
win.title("Translator")
win.resizable(width=False, height=False)
win.geometry('253x215')


def translation():
    global lang
    word = entry.get()
    translator = Translator(service_urls=['translate.google.com'])
    try:
        translation1 = translator.translate(word, dest=lang)
    except ValueError:
        Result.insert(1.0, f'Choose language!!!\n')
    else:
        Result.insert(1.0, f'Translated In {language} : {translation1.text}\n')


def choice(event):
    global lang, language
    lang = combobox.get()[0:combobox.get().find(' ')]
    language = combobox.get()[combobox.get().find(' - ') + 3:]


def clear():
    Result.delete('1.0', END)


lang, language = '', ''
lang_list = ['Choose language']
keys = list(constants.LANGUAGES.items())
for i, k in keys:
    tmp = [i, k]
    tmp1 = str(tmp[0] + ' - ' + tmp[1])
    lang_list.append(tmp1)

label = Label(win, text='Enter Word: ')
label.grid(row=0, column=0, sticky="W")

entry = Entry(win)
entry.grid(row=1, column=0, sticky="W")

label2 = Label(win, text='Choose language: ')
label2.grid(row=2, column=0, sticky="W")

label3 = Label(win, text=r'©\\ Donts_   2020')
label3.grid(row=6, column=0, sticky="E")

combobox = ttk.Combobox(win, values=lang_list)
combobox.current(0)
combobox.bind("<<ComboboxSelected>>", choice)
combobox.grid(row=4, column=0, sticky="W")

translation_button = Button(win, text='Translate!', command=translation)
translation_button.grid(row=4, columnspan=1, sticky="E")

clear_button = Button(win, text='Clear', command=clear)
clear_button.grid(row=1, columnspan=1, sticky="E")

Result = Text(win, height=6, width=29, wrap=WORD)
Result.grid(row=5, column=0, sticky='W')

Scroll = Scrollbar(win, command=Result.yview)
Scroll.grid(row=5, column=5, ipady=15)
Result.config(yscrollcommand=Scroll.set)
win.mainloop()
