def calcRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    # Redundancy bits are placed at the positoins
    # which correspond to the power of 2.
    j= 0
    k = 0
    m = len(data)
    res = ''

    # If position is power of 2 then insert '0'
    # Else append data
    for i in range(1, m + r+1):
        if(i==2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[k]
            k += 1
    return res

def calcParityBits(arr, r):
    newlist = []

    for i in [2**x for x in range(r)]:
        var = 0
        for j in range(1, len(arr) + 1):
            if (j not in [2**x for x in range(r)]):
                #sublist.append(int(arr[j-1]))
                if j&i:
                    var += int(arr[j-1])

        newlist.append(var%2)

    my_iter = iter(newlist)
    new_arr = ''
    for j in range(1, 1 + len(arr)):
        if (j not in [2**x for x in range(r)]):
            new_arr += arr[j-1]
        else:
            new_arr += str(next(my_iter))
    print(new_arr)
    print(newlist)
    return new_arr

data = '0101001'
r = calcRedundantBits(len(data))
arr = posRedundantBits(data, r)
print(arr)
res = calcParityBits(arr,r)
calcParityBits('10001011000', r)  

    