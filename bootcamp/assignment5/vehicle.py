from Sample import Car

def renault():
    car1 = Car.Car("pulse","renault","250","2019")
    car1.details()

    for i in range(1,101):
        car1.start()
        car1.stop()
    
    car1.details()

def Duster():
    car2 = Car.Car("pulse","Duster","250","2019")
    car2.details()

    for i in range(1,101):
        car2.start()
        car2.stop()
    
    car2.details()

    # for i in range(1,5):
    #     car2.start()
    #     car2.stop()
    
    # car2.details()

def BMW():
    car3 = Car.Car("pulse","BMW","250","2019")
    car3.details()

    for i in range(1,101):
        car3.start()
        car3.stop()
    
    car3.details()

    # for i in range(1,5):
    #     car3.start()
    #     car3.stop()
    
    # car3.details()

car = input("Enter single car name at a time(renault,Duster,BMW):")
if car == "BMW":
    BMW()

