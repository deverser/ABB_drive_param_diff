from tkinter import *
from tkinter import filedialog as fd
import json
import os
import glob
import re

root = Tk()
# root.withdraw() # we don't want a full GUI, so keep the root window from appearing
root.title("ABB Param diff")
root.geometry('500x200')
root.resizable(False, False)
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)


def readfile(path):
    """Read param data from files line by line"""
    REG = r'^[2-9][0-9]\.[0-9]{2}\:'
    with open(path, 'r', encoding='utf-8') as f:
        params = list(f.readlines())
        result = [param for param in params if re.match(REG, param)]
        return result


# For DEFAULT condition use files in root dir like A35_20190219.dwp

def write_diff(new_data, old_data, file_new, file_old):
    """Write different params in new result file"""
    count = []
    with open(file_new[:8] + 'diff.txt', 'w', encoding='utf-8') as f:
        for new, old in zip(new_data, old_data):
            if new != old:
                count.append(new)
                f.write('-----------------  ' + str(len(count)) + '  ---------------\n')
                f.write(' | ' + file_new[:8] + ' | ' + new + '\n')
                f.write(' | ' + file_old[:8] + ' | ' + old + '\n')
        f.write('Difference was found in ' + str(len(count)) + ' params.\n')


def file_select1():
    """Actions for getting data from NEW param file"""
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text", ".txt, .dwp")])
    file_new.config(text=file_name[-16:])
    param_new = readfile(file_name)
    with open('param_new.json', 'w', encoding='utf-8') as tmp_data:
        json.dump(param_new, tmp_data)


def file_select2():
    """Actions for getting data from OLD param file"""
    file_name = fd.askopenfilename(defaultextension=".dwp", filetypes=[("Text", ".txt, .dwp")])
    file_old.config(text=file_name[-16:])
    param_old = readfile(file_name)
    with open('param_old.json', 'w', encoding='utf-8') as tmp_data:
        json.dump(param_old, tmp_data)


def compare_data():
    """Comparison of OLD and NEW data"""
    if os.path.exists('param_new.json') and os.path.exists('param_old.json'):
        with open('param_new.json', 'r') as nd:
            new_data = json.load(nd)
        with open('param_old.json', 'r') as od:
            old_data = json.load(od)
        files = glob.glob('*.dwp')
        write_diff(new_data, old_data, files[0], files[1])
        os.remove('param_new.json')
        os.remove('param_old.json')


new = StringVar()
old = StringVar()

file_new = Button(text='File new', justify=CENTER, font=20, command=file_select1)
file_new.place(relheight=0.25, relwidth=0.5, x=250, y=30, anchor='c')

# new_entry = Entry()
# new_entry.place(anchor='c', x=300, y=28, relheight=0.2, relwidth=0.75)

file_old = Button(text='File old', justify=CENTER, font=20, command=file_select2)
file_old.place(relheight=0.25, relwidth=0.5, x=250, y=95, anchor='c')


# old_entry = Entry()
# old_entry.place(anchor='c', x=300, y=93, relheight=0.2, relwidth=0.75)
# old.set()

compare = Button(text='Compare', font=20, justify=CENTER, command=compare_data)
compare.place(relheight=0.3, relwidth=0.3, x=250, y=165, anchor='c')


root.mainloop()
