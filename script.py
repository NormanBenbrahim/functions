## Intro to functions

def print_cool_stuff(x):
    for i in x:
        print(x[i])

def file_printer(filename):
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        print(line)




if __name__ =="__main__":
    file_printer('file1.txt')
    file_printer('file2.txt')
    file_printer('file3.txt')