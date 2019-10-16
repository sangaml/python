def myfunc(i):
    for j in range(i):
        for k in range(j, i):
            print(" ", end ="")
        if j>1:
            for l in range(j):
                print(l+1, end =" ")
            rev = j-1
            while rev>0:
                print(rev, end =" ")
                rev -= 1

        else:   
             for l in range(j+1):
                print(l+1, end =" ")

        print("\n", end ="")

myfunc(10)