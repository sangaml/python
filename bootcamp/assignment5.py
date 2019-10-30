class Vehicle():
    needsmaintenace = False
    tripSincemaintenance = 0

    def __init__(self,make,model,weight,year):
    
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year

    # def NeedsMaintenace1(self):
    #     print(self.needsmaintenace)

    # def TripSinceMaintenance(self):
    #     pass

class Cars(Vehicle):

    def __init__(self):
        #Vehicle.__init__(self)
        pass

    def Drive (self,IsDriving='True'):
        pass
        
    def stop (self,IsDriving='False'):
        pass

    def repair (self):
        pass

def main():
    vehi = Vehicle(12,22,33,44)
    #print(vehi.make)
    return vehi.NeedsMaintenace1()
if __name__ == "__main__":
    main()