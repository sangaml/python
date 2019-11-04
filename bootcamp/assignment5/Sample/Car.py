from Sample.Vehicle import Vehicle
class Car (Vehicle):

    def __init__(self,make,model,weight,year):
        super().__init__(make,model,weight,year)
        self.IsDriving=False

    
    def start(self):
        if self.IsDriving == False:
            self.tripSinceMaintainance+=1
        if self.tripSinceMaintainance >= 100:
            self.needsMaintainance=True
        self.IsDriving = True

    def stop(self):
        self.IsDriving = False

    def repair(self):
        self.tripSinceMaintainance = 0
        self.needsMaintainance=False

    def details(self):
        print("Model:{0}, Make:{1}, Weight:{2}, TripsSinceMaintainance:{3}, Needs Maintainance:{4}".format(self.model,self.make,self.weight,self.tripSinceMaintainance, self.needsMaintainance))