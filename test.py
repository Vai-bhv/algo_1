import sys
l = []
integer = None
for line in sys.stdin:
    for c in line.strip().split():
        # print(l.strip())12
        integer = int(c)
        l.append(integer)
print(l)