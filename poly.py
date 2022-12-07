import sys

coefficients1 = []
exponents1 = []
coefficients2 = []
exponents2 = []
operation = sys.stdin.readline()
resulting_coefficient = []
resulting_exponents = []
while True:
    inp = sys.stdin.readline().split(" ")
    inpu = [v for v in inp if v != ""]
    inpu = [int(x) for x in inpu]
    if inpu[0] == inpu[1] == -1:
         break
    else:
        coefficients1.append(inpu[1])
        exponents1.append(inpu[0])

while True:
    inp = sys.stdin.readline().split(" ")
    inpu = [v for v in inp if v != ""]
    inpu = [int(x) for x in inpu]
    if inpu[0] == inpu[1] == -1:
         break
    else:
        coefficients2.append(inpu[1])
        exponents2.append(inpu[0])

def __add__(self, other):
    coefficients = list(self.coefficients)
    for i in range(0,other.length):
        try:
            coefficients[i] = coefficients[i] + other.coefficients[i]
        except:
            coefficients.append(0)
            coefficients[i] = coefficients[i] + other.coefficients[i]
    return Polynom(coefficients)


# def mul ():
# def div ():