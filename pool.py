import random
from Customerlist import*
from random_generator import *

## put all the passengers whose init floor is the same into the pool of that floor
class Pool:
    def __init__(self,floor_num,total_cus):
        #self.num_of_cus=num_of_cus
        self.floor_num = floor_num
        self.pool_up = []
        self.pool_down = []
        self.overall = []
        self.alreadyIn = 0
        self.total_cus = total_cus
        #self.regislist=Customerlist(self.num_of_cus).regislist()

        
    ##update the pool of the specific floor each time step with new-coming customer
    def Updatepool(self):
        num_of_cus = RNG().randpeople([0,20])
        if num_of_cus > (self.total_cus - self.alreadyIn):
            num_of_cus = self.total_cus - self.alreadyIn
        self.alreadyIn = self.alreadyIn + num_of_cus
        if num_of_cus != 0:
            regis = Customerlist(num_of_cus).regislist()
            for cus in regis:
                if cus.init_floor==self.floor_num:
                    if cus.direction == "up":
                        self.pool_up.append(cus)
                    else:
                        self.pool_down.append(cus)
        self.overall = [self.pool_up,self.pool_down]
        #return self.overall



    ## remove customer from two pools

    def Uppoolremove(self,cus):
        self.pool_up.remove(cus)

    def Downpoolremove(self,cus):
        self.pool_down.remove(cus)

        
    



        

        
        
 
        
        
        
        
        




