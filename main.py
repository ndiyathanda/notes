import tkinter
from tkinter import * 
import tkinter as tk
import os
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

settings_lst = []
string9 = ""
string10 = ""
notes_list = []
note_name = ""
notes_index = 0
END = ""
c = 0

def settings():
    root2.geometry('200x150')
    root2.resizable(0, 0)
    root2.deiconify()
    root2['background']=string10
    root.title("Settings")
    l.pack()
    l.pack()
    entry10.pack()
    l2.pack()
    entry9.pack()
    m.pack()  
    root2.mainloop()

def apply_settings():
    file = open("settings.txt", "w")
    string10 = entry10.get()
    string9 = entry9.get()
    file.write(string10)
    file.write("\n"+string9)
    print(string10)
    root2.withdraw()
    tkinter.messagebox.showinfo(title="NdiNotes", message="You need restart app to apply settings. Remember to save notes!")
    l.pack() 
    
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

def delete_note():
    pozdrawiam = entry2.get()
    res = messagebox.askquestion('NdiNotes', 'Do you want to delete this note: '+pozdrawiam+"?")
    if res == 'no':
        return
    elif res == 'yes':
        print("n")
        os.remove(pozdrawiam+".txt")
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
    root2.withdraw()    

def load_notes():
    string1 = ""
    refresh_note_pad()
    file = open("notes.txt", "r+")
    for line in file:
        if not line.isspace():
            show_all_notes.insert("end", line)
    show_all_notes.configure(state='disabled')
    root2.withdraw()

def open_note():
    refresh_note_pad2()
    c = 0
    string2 = entry2.get()
    file = open(string2+".txt", "r")
    opened_note = string2 + ".txt"
    for line in file:
        print(line)
        note_pad.insert("end" ,line)
    file.close()

def save_to_file():
    string2 = entry2.get()
    file = open(string2+".txt", "w")
    data = note_pad.get("1.0", 'end-1c')
    file.write(data)
    messagebox.showinfo("NdiNotes", "Note saved!")
    file.close()
    
def refresh_note_pad2():
    note_pad.configure(state='normal')
    note_pad.event_generate("<<SelectAll>>")
    note_pad.event_generate("<<Clear>>")

def refresh_note_pad():
    show_all_notes.configure(state='normal')
    show_all_notes.event_generate("<<SelectAll>>")
    show_all_notes.event_generate("<<Clear>>")

file = open("settings.txt", "r")

for x in file:
    settings_lst.append(x) 

try:
    string10 = settings_lst[0]
    string9 = settings_lst[1]
except:
    tkinter.messagebox.showinfo(title="Warning", message="Settings file is empty!")
    
string10 = string10.strip()
string9 = string9.strip()

print(string10, string9)

if string10=="":
    string10="white"
if string9=="":
    string9="black" 

root2 = tk.Tk()
root = tkinter.Tk()
root['background']=string10
root.title("Notes")
root.geometry('1000x600')
root.resizable(0, 0)

l = tkinter.Label(root, text='Easy Notes app based on txt files by ndiyathanda_ ver0.3', bg=string10, fg=string9)
l.place(x=350, y=0)

l = tkinter.Label(root, text='Note name ^^^', bg=string10, fg=string9)
l.place(x=0,y=170)

m = tkinter.Button(root, text = 'Settings', command=settings, bg=string10, width = 13, fg=string9)
m.place(x=0, y=0)

m = tkinter.Button(root, text = 'Add note', command=add_note, bg=string10, width = 13, fg=string9)
m.place(x=0, y=25)

entry2 = tkinter.Entry(root, width=16)
entry2.place(x=0, y=150)

m = tkinter.Button(root, text = 'Open note', command=open_note, bg=string10, width = 13, fg=string9)
m.place(x=0, y=50)

m = tkinter.Button(root, text = 'Refresh', command=load_notes, bg=string10, width = 13, fg=string9)
m.place(x=0, y=100)

m = tkinter.Button(root, text = 'Delete note', command=delete_note, bg=string10, width = 13, fg=string9)
m.place(x=0, y=75)

m = tkinter.Button(root, text = 'Save note', command=save_to_file, bg=string10, width = 13, fg=string9)
m.place(x=0, y=125)

l = tkinter.Label(root, text='Notes list ↓↓↓', bg=string10, fg=string9)
l.place(x=0, y=338)

show_all_notes = ScrolledText(root, width = 10, height = 15, bg=string10, fg=string9)
show_all_notes.place(x=0, y=354.5)

note_pad = ScrolledText(root, width = 110, height = 36, bg=string10, fg=string9, insertbackground='white')
note_pad.place(x=100,y=20)

l = tkinter.Label(root2, text='Settings', bg=string10, fg=string9)
l = tkinter.Label(root2, text='Hud color', bg=string10, fg=string9)
entry10 = tkinter.Entry(root2, width=8)
l2 = tkinter.Label(root2, text='Font color', bg=string10, fg=string9)
entry9 = tkinter.Entry(root2, width=8)
m = tkinter.Button(root2, text = 'OK', command=apply_settings, bg=string10, fg=string9)

root2.withdraw()            
  
load_notes()

root.mainloop()