# burtgeliin programm
    # hereglegchiin burtgel(Registriin Dugaar, Owog, Ner, Utas)
    # nomni burtgel(ner, zohiogch, on, turul, angilal)

# create, read, update, delete - CRUD

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('burtgeliin programm')
window.geometry('350x250')
window.resizable(0,0)

reg = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()

Label(window, text = 'Registr:').grid(row = 0, column = 0)
Entry(window, bd=1, textvariable = reg).grid(row = 0, column = 1)

Label(window, text = 'Owog:').grid(row = 1, column = 0)
Entry(window, bd=1, textvariable = owog).grid(row = 1, column = 1)

Label(window, text = 'Ner:').grid(row = 2, column = 0)
Entry(window, bd=1, textvariable = ner).grid(row = 2, column = 1)

Label(window, text = 'Utas:').grid(row = 3, column = 0)
Entry(window, bd=1, textvariable = utas).grid(row = 3, column = 1)

def user_save():
    if reg.get() == "" or owog.get() == "" or ner.get() == "" or utas.get() == "":
        messagebox.showerror("Warning", "dopishi do kontsa, pridurok")
    else:
        list_data.insert(END, reg.get() + ' ' + owog.get() + ' ' + ner.get() + ' ' + utas.get())
        clear()

def change():
    selected_user = list_data.get(list_data.curselection()[0])
    data = selected_user.split(' ')
    reg.set(data[0])
    owog.set(data[1])
    ner.set(data[2])
    utas.set(data[3])
    list_data.delete(list_data.curselection()[0])
    if reg.get() == "" or owog.get() == "" or ner.get() == "" or utas.get() == "":
        messagebox.showerror("Warning", "dopishi do kontsa, pridurok")
    else:
        list_data.insert(END, reg.get() + ' ' + owog.get() + ' ' + ner.get() + ' ' + utas.get())
        clear_entries()

    messagebox.showwarning("Ban", "tifu tebe v litso")

def delete():
    answer = messagebox.askyesno('Podumai', 'ti tochno hochesh udalit?')
    if answer == True:
        answer = messagebox.askyesno('Podumai', 'tochno tochno?')
        if answer == True:
            answer = messagebox.askyesno('Podumai', 'tochno tochno tochno tochno?')
            if answer == True:
                messagebox.showwarning('nu ladno', 'tak uzh i bit')
            list_data.delete(list_data.curselection()[0])
    else:
        messagebox.showwarning('hah', 'ne udalil')
def clear():
    reg.set('')
    owog.set('')
    ner.set('')
    utas.set('')


Button(window, text = 'hadgalah', command=user_save).grid(row=0,column=3)
    
Button(window, text = 'zasah', command = change).grid(row=1, column=3)

Button(window, text = 'ustgah', command = delete).grid(row=2, column=3)

Button(window, text = 'arilgah', command = clear).grid(row=3,column=3)

def select(event):   # eventeer damjdag
    selected_user = list_data.get(list_data.curselection()[0])
    data = selected_user.split(' ')
    reg.set(data[0])
    owog.set(data[1])
    ner.set(data[2])
    utas.set(data[3])
list_data = Listbox(window, width = 45, height = 8)
list_data.grid(row=4, rowspan=4, column=0, columnspan=3)
list_data.insert(END, 'registriin dugaar:    owog:    ner:    utas:')
list_data.bind('<<ListboxSelect>>', select)

scroll = Scrollbar(window)
scroll.grid(row=4,column=4)
list_data.configure(yscrollcommand = scroll.set)
scroll.configure(command=list_data.yview)

window.mainloop()