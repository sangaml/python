def my_func(st):

    res = []
    #Iterate over the characters
    for index, c in enumerate(st):
        if index % 2 == 0:
            #Refer to each character via index and append modified character to list
            res.append(c.upper())
        else:
            res.append(c.lower())

    #Join the list into a string and return
    return ''.join(res)
print(my_func('helloworld'))