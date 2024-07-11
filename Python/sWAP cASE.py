def swap_case(s):
    l=list(s)
    my_list=[]
    for char in l:
        if char.islower() == True : 
            my_list.append(char.upper())
        elif char.isupper() == True : 
            my_list.append(char.lower())
        else : 
            my_list.append(char)

    result="".join(my_list)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
