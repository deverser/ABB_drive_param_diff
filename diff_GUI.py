from tkinter import *
from tkinter import filedialog as fd

root = Tk()
# root.withdraw() # we don't want a full GUI, so keep the root window from appearing
root.title("ABB Param diff")
root.geometry('500x200')
root.resizable(False, False)
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)
def file_select1():
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text",".txt, .dwp")])
    file_new.config(text=file_name[-16:])
    return file_name

def file_select2():
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text",".txt, .dwp")])
    file_old.config(text=file_name[-16:])
    return file_name

def readfile(path):
    """Read param data from files line by line"""
    with open(path, 'r', encoding='utf-8') as f:
        param = tuple(f.readlines())
        return param

new = StringVar()
old = StringVar()

file_new = Button(text='File new',justify=CENTER, font=20, command=file_select1)
file_new.place(relheight=0.25, relwidth=0.5, x=250, y=30, anchor='c')

# new_entry = Entry()
# new_entry.place(anchor='c', x=300, y=28, relheight=0.2, relwidth=0.75)

file_old = Button(text='File old', justify=CENTER, font=20, command=file_select2)
file_old.place(relheight=0.25, relwidth=0.5, x=250, y=95, anchor='c')

# old_entry = Entry()
# old_entry.place(anchor='c', x=300, y=93, relheight=0.2, relwidth=0.75)
# old.set()

compare = Button(text='Compare', font=20, justify=CENTER)
compare.place(relheight=0.3, relwidth=0.3, x=250, y=165, anchor='c')





root.mainloop()