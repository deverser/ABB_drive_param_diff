from tkinter import *
from tkinter import filedialog as fd
import json, os


root = Tk()
# root.withdraw() # we don't want a full GUI, so keep the root window from appearing
root.title("ABB Param diff")
root.geometry('500x200')
root.resizable(False, False)
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)
files = []

def readfile(path):
    """Read param data from files line by line"""
    with open(path, 'r', encoding='utf-8') as f:
        param = tuple(f.readlines())
        return param


def write_diff(new_data, old_data, path, file_new, file_old):
    """Write different params in new result file"""
    count = []
    REG = r'^[2-9][0-9]\.[0-9]{2}\:'
    for new, old in zip(new_data, old_data):
        if re.match(REG, new):
            if new != old:
                count.append(new)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write('Difference was found in ' + str(len(count)) + ' params.\n')
                    f.write(' | ' + file_new[-16:-8] + ' | ' + new)
                    f.write(' | ' + file_old[-16:-8] + ' | ' + old + '\n')


def file_select1():
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text",".txt, .dwp")])
    file_new.config(text=file_name[-16:])
    param_new = readfile(file_name)
    with open('param_new.json', 'w', encoding='utf-8') as tmp_data:
        json.dump(param_new, tmp_data)


def file_select2():
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text",".txt, .dwp")])
    file_old.config(text=file_name[-16:])
    param_old = readfile(file_name)
    with open('param_old.json', 'w', encoding='utf-8') as tmp_data:
        json.dump(param_old, tmp_data)


def compare_data():
    if os.path.exists('param_new.json') and os.path.exists('param_old.json'):



new = StringVar()
old = StringVar()

file_new = Button(text='File new',justify=CENTER, font=20, command=file_select1)
file_new.place(relheight=0.25, relwidth=0.5, x=250, y=30, anchor='c')

# new_entry = Entry()
# new_entry.place(anchor='c', x=300, y=28, relheight=0.2, relwidth=0.75)

file_old = Button(text='File old', justify=CENTER, font=20, command=file_select2)
file_old.place(relheight=0.25, relwidth=0.5, x=250, y=95, anchor='c')

print(files)
if files:
    new_param_file = files.pop(0)
    old_param_file = files.pop(0)
else:
    file_new.config(text='File new')
    file_old.config(text='File old')

# old_entry = Entry()
# old_entry.place(anchor='c', x=300, y=93, relheight=0.2, relwidth=0.75)
# old.set()

compare = Button(text='Compare', font=20, justify=CENTER, command=compare_data)
compare.place(relheight=0.3, relwidth=0.3, x=250, y=165, anchor='c')


root.mainloop()
