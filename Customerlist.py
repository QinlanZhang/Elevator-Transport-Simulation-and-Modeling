from random_generator import *
import time
import random


##Create the customer object,creating the attributes of every customer:initial floor and destination floor

class Customer:
    def __init__(self,initfloor=1,destfloor=1,direction = "up"):
        #self.numfloor=num_of_floor
        self.init_floor=initfloor
        self.dest_floor=destfloor
        self.direction = direction
        self.customerUpdate()


    def customerUpdate(self):
        #rand = RNG(2**31-1)
        self.init_floor=RNG().randfloor()
        self.dest_floor=RNG().randdestination()
        while self.dest_floor==self.init_floor:
            self.dest_floor=RNG().randdestination()
        if self.dest_floor < self.init_floor:
            self.direction = "down"
        else:
            self.direction = "up"
        #print self.init_floor,self.dest_floor


            
    
## Create the customerlist
class Customerlist:

    def __init__(self,num_of_cus):
        self.num_of_cus=num_of_cus # RNG().randint(*)
        #self.numfloor=numfloor

    ## cutomer.regislist will return a customer list containing customer objects
    def regislist(self):
        regislist =[]
        for i in range(self.num_of_cus):
            customer= Customer()
            regislist.append(customer)
        return regislist



