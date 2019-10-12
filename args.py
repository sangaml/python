def myfunc(*args):
    for num in args:
        if (num) % 2 == 0:
            print (num)

myfunc(1,2,3,4,5,6)