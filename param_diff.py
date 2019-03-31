import os
import re

PATH = '.\\Профилактика'
path_new = '\\Профилактика\\2019\\=JM01E69+DRA01\\=JM01E69+DRA01\\'
path_old = '\\Профилактика\\2018\\=JM01E69+DRA01\\=JM01E69+DRA01\\'
file_new = path_new + 'A29_20190219.dwp'
file_old = path_old + 'A29_20180206.dwp'
result = file_new[-16:-12] + 'diff.txt'
path_result = path_new + result
DIR_NAME = '=JM01E69+DRA01'
PARAM_DIR = 'Param'
AREG = '^A\d{1,2}'
#^A[1-9]{1,2}_20\d{6}.dwp$ - pattern for file like A29_20190908.dwp
# ^A\d{1,2}(_|\s)\w+.+$ - pattern for drive folder name


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


def walk_through(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".dwp"):
                file_path = os.path.join(root, file)

                # file_list.append(file_path)
    # return file_list

#


if __name__ == '__main__':
    # new_param = readfile(file_new)
    # old_param = readfile(file_old)
    # write_diff(new_param, old_param, result, file_new, file_old)
    print(walk_through(PATH))





