def mutate_string(string, position, character):
    string_in_list=list(string)
    string_in_list[position] = character
    
    string="".join(string_in_list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
