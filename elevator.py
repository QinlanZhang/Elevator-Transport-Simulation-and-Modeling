class elevator:
    def __init__(self,direction="stay",cur_floor=1,capacity = 16):
        self.direction=direction
        self.cur_floor=cur_floor
        self.remain_list=[]
        self.requireIn=[]
        self.capacity = capacity
        self.Aimminglist = [0]


    def move(self):
        if self.direction=="up":
            self.cur_floor+=1
        elif self.direction=="down":
            self.cur_floor-=1
        else:
            pass
            

    def add_customer(self,cus):
        ## when the passenger goes into the elevator,his or her id is added to the remain_list
        if self.cur_floor == cus.init_floor:
            self.remain_list.append(cus)
            if cus.dest_floor not in self.requireIn:
                self.requireIn.append(cus.dest_floor)



    def cancel_customer(self,cus):
    ##when the passenger reaches his or her destination floor and goes out of the elevator,the id is removed from the remain_list
        if self.cur_floor == cus.dest_floor:
            self.remain_list.remove(cus)
            if cus.dest_floor in self.requireIn:
                self.requireIn.remove(cus.dest_floor)



 
        

            

                
 
      
        
