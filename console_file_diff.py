import sys
import re

#^A[1-9]{1,2}_20\d{6}.dwp$ - pattern for file like A29_20190908.dwp
# ^A\d{1,2}(_|\s)\w+.+$ - pattern for drive folder name
#
def result_file(file_path):
    return file_path[:8] + '.txt'

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

if __name__ == '__main__':
    print(sys.executable)
    new_param = readfile(sys.argv[1])
    old_param = readfile(sys.argv[2])
    result = result_file(sys.argv[1])
    print(result)
    write_diff(new_param, old_param, result, sys.argv[1], sys.argv[2])