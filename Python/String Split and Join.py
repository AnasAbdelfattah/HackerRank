

def split_and_join(line):
    my_list=line.split()
    return "-".join(my_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
