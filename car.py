class Car(object):
    def __init__(self , model , color , company, speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
#creating a object for the class car
a = Car("a6", "turquoise" , "audi" , "4353")    
#a.start()   
print(a.start())
print(a.color)