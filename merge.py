import sys


if sys.argv[1] == '-i':
    inp_1 = sys.argv[2]
    inp_2 = sys.argv[3]
    out_1 = sys.argv[4]
else:
    inp_1 = sys.argv[1]
    inp_2 = sys.argv[2]
    out_1 = sys.argv[3]

f1 = open(inp_1)
f2 = open(inp_2)
f3 = open(out_1, "w")

    

def merge_sort(f1,f2,f3):
    char_1 = f1.readline()
    char_2 = f2.readline()


    if sys.argv[1] == "-i":
        char_1.lower()
        char_2.lower()
        while char_1 or char_2 != '' :
            if char_1 == '' and char_2 != '': 
                f3.write(char_2)
                #print(char_2)
                char_2 = f2.readline()
            elif char_2 == '' and char_1 != '': 
                f3.write(char_1)
                #print(char_1)
                char_1 = f1.readline()
            elif char_1 < char_2:
                #cur1 = f1.readline()
                #print('List one',char_1)
                f3.write(char_1)
                char_1 = f1.readline() 
            else:
                #cur2 = f2.readline()
                #print('List two',char_2)
                f3.write(char_2)
                char_2 = f2.readline()
        



    # while f1.readline() and f2.readline() != '':
    while char_1 or char_2 != '':
        if char_1 == '' and char_2 != '': 
            f3.write(char_2)
            #print(char_2)
            char_2 = f2.readline()
        elif char_2 == '' and char_1 != '': 
            f3.write(char_1)
            #print(char_1)
            char_1 = f1.readline()
        elif char_1 < char_2:
            #cur1 = f1.readline()
            #print('List one',char_1)
            f3.write(char_1)
            char_1 = f1.readline() 
        else:
            #cur2 = f2.readline()
            #print('List two',char_2)
            f3.write(char_2)
            char_2 = f2.readline()
    f3.close()
merge_sort(f1,f2,f3)


