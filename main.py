import tkinter
import os
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

notes_list = []
note_name = ""
notes_index = 0
END = ""
c = 0

def add_note():
    note_name = ""
    note_name = entry2.get()
    file = open("notes.txt", "a")
    file.write(note_name+"\n")
    file.close()
    file = open(note_name+".txt", "x")
    file.write(note_name)
    file.close()
    messagebox.showinfo("NdiNotes", "Note added")
    load_notes()

  #  notes_list.clear()
   # note_name = ""
    #note_name = entry2.get()
   # notes_list.append(note_name)
   # file = open("../../Desktop/notes.txt", "w")
   # for note_name in notes_list:
   #     file.write("\n" + note_name + "\n" + "END-NOTE")
   # file.close()
   # print(notes_list)
   # load_tasks()

def delete_note():
    pozdrawiam = entry2.get()
    res = messagebox.askquestion('NdiNotes', 'Do you want to delete this note: '+pozdrawiam+"?")
    if res == 'no':
        return
    elif res == 'yes':
        print("n")
        os.remove(pozdrawiam+".txt")
        #leje kurwa belweder

        f = open('notes.txt', 'r')
        a = []
        a.clear()
        a.append(pozdrawiam)
        print(a)
        lst = []
        for line in f:
            for word in a:
                if word in line:
                    line = line.replace(word, '')
            lst.append(line)
        f.close()
        f = open('notes.txt', 'w')
        for line in lst:
            f.write(line)
        messagebox.showinfo("NdiNotes", "Note deleted")
        f.close()


def load_notes():
    string1 = ""
    refresh_note_pad()
    file = open("notes.txt", "r+")
    for line in file:
        if not line.isspace():
            show_all_notes.insert("end", line)
    show_all_notes.configure(state='disabled')
   # show_all_notes2()

def open_note():
    refresh_note_pad2()
    c = 0
    string2 = entry2.get()
    file = open(string2+".txt", "r")
    opened_note = string2 + ".txt"
    #for line in file:
     #   print(line)
    for line in file:
        print(line)
        note_pad.insert("end" ,line)
        #   print(line)
    file.close()
    #show_all_notes2()

def save_to_file():
    string2 = entry2.get()
    file = open(string2+".txt", "w")
    data = note_pad.get("1.0", 'end-1c')
    file.write(data)
    messagebox.showinfo("NdiNotes", "Note saved!")
    file.close()

#def show_all_notes2():
#    #refresh_note_pad()
#    show_all_notes.configure(state='normal')
#    notes_index = 0
#    for notes in notes_list:
#        show_all_notes.insert(0.0, notes + "\n")
#    show_all_notes.configure(state='disabled')

def refresh_note_pad2():
    note_pad.configure(state='normal')
    note_pad.event_generate("<<SelectAll>>")
    note_pad.event_generate("<<Clear>>")

def refresh_note_pad():
    show_all_notes.configure(state='normal')
    show_all_notes.event_generate("<<SelectAll>>")
    show_all_notes.event_generate("<<Clear>>")

root = tkinter.Tk()
root['background']='grey'
root.title("Notes")
root.geometry('500x410')
root.resizable(0, 0)

l = tkinter.Label(root, text='Easy Notes app based on txt files by ndiyathanda_ ver0', bg='grey')
l.pack()

l = tkinter.Label(root, text='Note name ^^^', bg='grey')
l.place(x=0,y=170)

m = tkinter.Button(root, text = 'Add note', command=add_note, bg='grey', width = 13)
m.place(x=0, y=25)

entry2 = tkinter.Entry(width=16)
entry2.place(x=0, y=150)

m = tkinter.Button(root, text = 'Open note', command=open_note, bg='grey', width = 13)
m.place(x=0, y=50)

m = tkinter.Button(root, text = 'Refresh', command=load_notes, bg='grey', width = 13)
m.place(x=0, y=100)

m = tkinter.Button(root, text = 'Delete note', command=delete_note, bg='grey', width = 13)
m.place(x=0, y=75)

m = tkinter.Button(root, text = 'Save note', command=save_to_file, bg='grey', width = 13)
m.place(x=0, y=125)

show_all_notes = ScrolledText(root, width = 10, height = 12.5, bg='black', fg='white')
show_all_notes.place(x=0, y=197)

note_pad = ScrolledText(root, width = 47, height = 25, bg='black', fg='white', insertbackground='white')
note_pad.place(x=100,y=20)

load_notes()

root.mainloop()