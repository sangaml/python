class Vehicle():
    needsmaintenace = False
    tripSincemaintenance = 0

    def __init__(self,make,model,weight,year):
    
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year

    def NeedsMaintenace(self):
        pass

    def TripSinceMaintenance(self):
        pass

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