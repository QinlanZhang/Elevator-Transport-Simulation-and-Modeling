import math
import time
import random

class RNG(object):

    def __init__(self):
        self.x = random.random()
    
    
    def randfloor(self):
        '''Returns a certain int (start floor) between [1,5] which follows the distribution obtained by observation. '''
        randnum = self.x
        
        if randnum <= 0.1:
            return 1
        elif randnum <= 0.4:
            return 2
        elif randnum <= 0.6:
            return 3
        elif randnum <= 0.9:
            return 4
        else:
            return 5


    def randdestination(self):
        '''Returns a certain int (destination floor) between [1,5] which follows the distribution obtained by observation. '''
        randnum = self.x
        
        if randnum <= 0.1:
            return 1
        elif randnum <= 0.4:
            return 2
        elif randnum <= 0.6:
            return 3
        elif randnum <= 0.9:
            return 4
        else:
            return 5
    
    def randpeople(self,interval=[0,1]):
        randnum = self.x
        randomint = interval[0] + int( randnum *(interval[1]-interval[0]))
        return randomint
        





        
 
