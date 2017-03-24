import random
from Customerlist import*
from pool import*


class Building:
    def __init__(self,total_cus,num_of_floor=5):
        self.total_cus=total_cus
        self.num_of_floor=num_of_floor
        self.adict = {}
        self.dictioncreate()

    def dictioncreate(self):
        for i in range(1,self.num_of_floor+1):
            pool = Pool(i,self.total_cus)
            #pool.Updatepool()
            self.adict[i]=pool
        return self.adict
    ## adict is a dictionary of the pool of each floor,it is in the format of key:values pair,
    ## where the key is the number of the floor and the value is the pool(customerlist)of that floor
    ## building.dictioncreate() returns the dictionary

    def dictionUpdate(self):
        for pool in self.adict:
            self.adict[pool].Updatepool()
        return self.adict

