def myfunc(st):

    res = []
    for sl in range(len(st)):
        if sl % 2 == 0:
           res.append(st[sl])
            #Refer to each character via index and append modified character to list
        else:
            res.append(st[sl].upper())
    return ''.join(res) #Join the list into a string and return

print(myfunc('sangamlonk'))