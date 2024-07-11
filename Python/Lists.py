listAll = []

def switch(command):
    if command[0] == "insert":
        listAll.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        listAll.remove(int(command[1]))
    elif command[0] == "append":
        listAll.append(int(command[1]))    
    elif command[0] == "pop":
        listAll.pop()
    elif command[0] == "reverse":
        listAll.reverse()
    elif command[0] == "print":
        print(listAll)
    elif command[0] == "sort":
        listAll.sort()

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        command = input().split()
        switch(command)
