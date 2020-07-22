import random

def make_list():
    list = []
    for i in range(0, 10000):
        list.append(random.randrange(0,10000))
    return list

def build_max_heap(list, n):
    if list[n] > list[0]:
        temp = list[0]
        list[0] = list[n]
        list[n] = temp
    if n >= 1:
        build_max_heap(list, n-1)
    return list

def max_heapify(list):
    conflict = 1
    while conflict != 0:
        conflict = 0
        for i in range(0, len(list)):
            conflict += sort(list, i)
    return list

def visualize(list):
    print("                               {o}".format(o=list[0]))
    print("                  {i}                              {s}".format(i=list[1], s=list[2]))
    print("         {x}           {y}                 {z}             {a}".format(x=list[3], y=list[4], z=list[5], a=list[6]))
    print("    {a}     {b}   {c}      {d}       {e}      {f}    {g}       {h}".format(a=list[7], b=list[8], c=list[9], d=list[10], e=list[11], f=list[12], g=list[13], h=list[14]))
def add_to_heap(list, num):
    list.append(num)
    x = len(list) - 1
    while x > 0:
        y = get_parent(x)
        if list[x] > list[y]:
            temp = list[x]
            list[x] = list[y]
            list[y] = temp
        else:
            break
        x = y

def change_key(list, num, new_num):
    found = False
    for i in range(0, len(list)):
        if list[i] == num:
            list[i] = new_num
            found = True
            print(i)
            x = sort(list, i)
    if not found:
        print("Not Found in list!")
    return list

def sort(list, i):
    max_len = len(list)-1
    conflict = 0
    while i > -1 and i <= max_len:
        y = get_left(i, max_len)
        x = get_right(i, max_len)
        z = get_parent(i)
        if z != -1 and list[i] > list[z]:
            temp = list[i]
            list[i] = list[z]
            list[z] = temp
            if z != 0:
                i = z
            else:
                return conflict + 1
        elif y != -1 and list[i] < list[y] and list[y] > list[x]:
            temp = list[i]
            list[i] = list[y]
            list[y] = temp
            i = y
            conflict += 1
        elif x != -1 and list[i] < list[x]:
            temp = list[i]
            list[i] = list[x]
            list[x] = temp
            i = x
            conflict += 1
        else:
           return conflict


def peek(list):
    print("Peek: {l}".format(l=list[0]))

def pop(list):
    print("Pop!: {p}".format(p=list[0]))
    list[0] = list[-1]
    del list[-1]
    x = sort(list, 0)
    return list



def get_left(i, max_len):
    x = 2 * i + 1
    if x < max_len:
        return x
    else:
        return -1

def get_right(i, max_len):
    x = 2 * i + 2
    if x < max_len:
        return x
    else:
        return -1

def get_parent(c):
    x = (c-1) // 2
    if x >= 0:
        return x
    else:
        return -1

def has_left(i):
    return get_left(i) != None

def has_right(i, n):
    return get_right(i) < n

def has_parent(i):
    return get_parent(i) >= 0


if __name__ == "__main__":
    ans = ''
    while ans != "X":
        print("\n\n")
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        print("(0) - Create New List")
        print("(1) - Create Heap From List")
        print("(2) - Add Key To Heap")
        print("(3) - Change Key in Heap")
        print("(4) - Print Heap")
        print("(5) - Peek Max Key")
        print("(6) - Pop Max Key")
        print("(X) - Exit")
        ans = input("> ")
        print("\n\n")
        if ans == '0':
            list = make_list()
            visualize(list)
            ans = ""
        elif ans == '1':
            max_heap = max_heapify(list)
            visualize(max_heap)
        elif ans == '2':
            print("What Key Would You Like To Add?")
            num = int(input("> "))
            add_to_heap(max_heap, num)
            print(max_heap)
        elif ans == '3':
            print("What Key Would You Like to Change?")
            num = int(input("> "))
            if num in max_heap:
                print("What Is The New Key?")
                new_num = int(input("> "))
                change_key(max_heap, num, new_num)
                print(max_heap)
            else:
                print("Value Not In List!")
        elif ans == '4':
            print(max_heap)
        elif ans == '5':
            peek(max_heap)
        elif ans == '6':
            max_heap = pop(max_heap)

        elif ans == 'X' or ans == 'x':
            break
        else:
            print("Invalid Entry, Please Try Again")
