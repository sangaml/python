def printFibonacciNumbers(n): 
      
    f1 = 0
    f2 = 1
    print (f1)
    print (f2)
    for x in range(0, n): 
        c = f1 + f2 
        f1 = f2 
        f2 = c
        print(c)
          
# Driven code 
printFibonacciNumbers(10) 