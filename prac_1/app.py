chars = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'Ñ': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
    'a': 27,
    'b': 28,
    'c': 29,
    'd': 30,
    'e': 31,
    'f': 32,
    'g': 33,
    'h': 34,
    'i': 35,
    'j': 36,
    'k': 37,
    'l': 38,
    'm': 39,
    'n': 40,
    'ñ': 41,
    'o': 42,
    'p': 43,
    'q': 44,
    'r': 45,
    's': 46,
    't': 47,
    'u': 48,
    'v': 49,
    'w': 50,
    'x': 51,
    'y': 52,
    'z': 53,
    ' ': 54
}

# initializing string
test_str = 'Hello World'
extra = len(test_str)%3
for x in range(3-extra):
    test_str += ' '

i = 0
my_list = list()
while(i<len(test_str)):
    my_list.append(test_str[i:(i+3)])
    i+=3
print(my_list)

x = list()
y = list()
z = list()

for in_list in my_list:
    i = 0
    for k in in_list:
        if i==0:
            x.append(chars[k[0]])
        elif i==1:
            y.append(chars[k[0]])
        else:
            z.append(chars[k[0]])
        i+=1
print(x)
print(y)
print(z)
