from elevator import *
from Customerlist import *
from pool import *
from random_generator import *
from Building import *
import time

class System(object):
    def __init__(self,num_elevator):
        self.num_elevator = num_elevator
        self.elevators = {}
        for i in range(self.num_elevator):
            self.elevators[i]=elevator()
        self.requireout_up=[0,0,0,0,0]
        self.requireout_down=[0,0,0,0,0]

    def requireOut(self,adict):
        for key in adict:
            if len(adict[key].pool_up)!=0:
                self.requireout_up[key-1]=1
            else:
                self.requireout_up[key-1]=0
            if len(adict[key].pool_down)!=0:
                self.requireout_down[key-1]=1
            else:
                self.requireout_down[key-1]=0


    def DecisionDecide(self,elevator):
        if len(elevator.Aimminglist)==1:
            if elevator.Aimminglist[0]==0:
                elevator.direction='stay'
            elif elevator.Aimminglist[0]==elevator.cur_floor and elevator.cur_floor == 1:
                elevator.direction='stay'
            elif  elevator.Aimminglist[0]==elevator.cur_floor and elevator.cur_floor==len(self.requireout_up):
                elevator.direction='stay'
            elif elevator.Aimminglist[0]==elevator.cur_floor:
                elevator.direction='stay'
            elif elevator.Aimminglist[0]> elevator.cur_floor:
                elevator.direction='up'
            elif elevator.Aimminglist[0]< elevator.cur_floor and elevator.Aimminglist[0]> 0:
                elevator.direction='down'
        else:
            if elevator.Aimminglist[1] > elevator.cur_floor:
                elevator.direction='up'
            elif elevator.Aimminglist[1] < elevator.cur_floor:
                 elevator.direction='down'
            else:
                elevator.direction='stay'

    def outdemand(self,ho):
        if ho>0:
            for h2 in range(ho):
                if self.elevators[ho].direction==self.elevators[h2].direction and self.elevators[ho].cur_floor==self.elevators[h2].cur_floor:
                    self.elevators[h2].Aimminglist[0]=0
                    break
        if self.elevators[ho].direction=="up":
            p=self.elevators[ho].cur_floor
            for i in range(p-1,len(self.requireout_up)):
                if self.requireout_up==1:
                    self.elevators[ho].Aimminglist[0]=i+1
                    break
                else:
                    for xx in range(1,self.num_elevator):
                        if self.elevators[(xx+ho)%self.num_elevator].direction=="up" and self.elevators[(xx+ho)%self.num_elevator].cur_floor==i:
                            self.elevators[ho].Aimminglist[0]=0
                            break
                        break
                    self.elevators[ho].Aimminglist[0] = 0

        elif self.elevators[ho].direction=="down":
            p=self.elevators[ho].cur_floor
            for i in range(p,-1,-1):
                if self.requireout_down[i-1]==1:
                    self.elevators[ho].Aimminglist[0]=i
                    break
                else:
                    for xx in range(1,self.num_elevator):
                        if self.elevators[(xx+ho)%self.num_elevator].direction=="down" and self.elevators[(xx+ho)%self.num_elevator].cur_floor==i:
                            self.elevators[ho].Aimminglist[0]=0
                            break
                        break
                self.elevators[ho].Aimminglist[0]=0
        elif self.elevators[ho].direction=="stay":
            p=self.elevators[ho].cur_floor
            if p<100:
                for m in range(0,len(self.requireout_up)):
                    if p+m<=len(self.requireout_up):
                        if self.requireout_up[p+m-1]==1:
                            m1=m
                            break
                        for xx in range(1,self.num_elevator):
                            if self.elevators[(ho+xx)%self.num_elevator].direction=="up" and self.elevators[(ho+xx)%self.num_elevator].cur_floor==p+m:
                                m1=-1
                                break
                        m1=-1
                for m in range(0,len(self.requireout_up)):
                    if p+m<=len(self.requireout_up):
                        if self.requireout_down[p+m-1]==1:
                            m2=m
                            break
                        m2=-1
                for m in range(0,len(self.requireout_up)):
                    if p-m>0:
                        if self.requireout_up[p-m-1]==1:
                            m3=m
                            break
                        m3=-1
                for m in range(0,len(self.requireout_up)):
                        if self.requireout_down[p-m-1]==1:
                            m4=m
                            break
                        for xx in range(1,self.num_elevator):
                            if self.elevators[(xx+ho)%self.num_elevator].direction=="down" and self.elevators[(xx+ho)%self.num_elevator].cur_floor==p-m:
                                m4=-1
                                break
                        m4=-1
                # finding min
                if m1==-1 and m2!=-1:
                    p1=m2
                elif m1==-1 and m2==-1:
                    p1=-1
                elif m1!=-1 and m2==-1:
                    p1=m1
                elif m1<=m2:
                    p1=m1
                else:
                    p1=m2
                if m3==-1 and m4!=-1:
                    p2=m4
                elif m3==-1 and m4==-1:
                    p2=-1
                elif m3!=-1 and m4==-1:
                    p2=m3
                elif m3<=m4:
                    p2=m3
                else:
                    p2=m4
                if p1==0 or p2==0:
                    self.elevators[ho].Aimminglist[0]=p
                elif p1>0 and p2<0:
                    self.elevators[ho].Aimminglist[0]=p+p1
                elif p1<0 and p2>0:
                    self.elevators[ho].Aimminglist[0]=p-p2
                elif p1<0 and p2<0:
                    self.elevators[ho].Aimminglist[0]=0
                elif p1<=p2:
                    self.elevators[ho].Aimminglist[0]=p+p1
                else:
                    self.elevators[ho].Aimminglist[0]=p-p2







def main(num_people):
    #initial the elevator system
    system = System(3)
    #initial the building with total number of customers, total floor by default is 5
    building = Building(num_people)
    #pools = building.adict
    max_iter = 2500
    count = {0:3,1:3,2:3}
    peoplecount = 0
    a=0
    # start the simulation
    for step in range(max_iter):
        # print step
        # print peoplecount
        ## if peoplecount < building.total_cus
        if peoplecount < 0.6*building.total_cus or (len(system.elevators[0].remain_list)+len(system.elevators[1].remain_list)+len(system.elevators[2].remain_list))>0:


            #Update pool in each level
            pools = building.dictionUpdate()
            system.requireOut(pools)
            #print pools[1].alreadyIn

            for key in system.elevators:
                #print 1,system.elevators[0].direction,system.elevators[0].cur_floor
                #print system.requireout_up,system.requireout_down,len(system.elevators[0].remain_list),len(system.elevators[1].remain_list)
                #update RequireOut information

                system.outdemand(key)
                #print system.elevators[key].cur_floor
                #direction change
                system.DecisionDecide(system.elevators[key])
                #print system.elevators[2].Aimminglist
                #move or load & release customers
                #if elevator stops, it will stop 4 time step
                # print count[0]
                # print 0,system.elevators[0].Aimminglist
                #print key,system.elevators[0].cur_floor,len(system.elevators[0].remain_list),system.elevators[0].Aimminglist,system.elevators[0].direction,count[0]
                # print system.elevators[key].Aimminglist,key
                if count[key] == 3:
                    if (system.elevators[key].cur_floor==1 and system.elevators[key].direction=='down'):
                        system.elevators[key].direction='stay'
                    elif(system.elevators[key].cur_floor==len(system.requireout_up) and system.elevators[key].direction=='up'):
                        system.elevators[key].direction='stay'
                    system.elevators[key].move()
                    # print system.requireout_up,system.requireout_down
                    # if there's requires,open the door, upload & release customers
                    if len(system.elevators[key].Aimminglist)==1:
                        if system.elevators[key].Aimminglist[0]==system.elevators[key].cur_floor :
                            count[key] = 0
                    else:
                        if system.elevators[key].Aimminglist[0]==system.elevators[key].cur_floor or system.elevators[key].Aimminglist[1]==system.elevators[key].cur_floor or system.elevators[key].Aimminglist[-1]==system.elevators[key].cur_floor:
                            count[key] = 0
                else:
                    #print system.elevators[0].cur_floor,system.elevators[0].direction,count[0]
                    if len(system.elevators[key].Aimminglist)==1:
                        count[key] = count[key] + 1
                        if system.elevators[key].Aimminglist[0]==system.elevators[key].cur_floor:
                            j=0
                            while j<len(system.elevators[key].remain_list):
                                cus=system.elevators[key].remain_list[j]
                                if cus.dest_floor == system.elevators[key].cur_floor:
                                    system.elevators[key].cancel_customer(cus)
                                    A4=system.elevators[key].Aimminglist[1:]
                                    if system.elevators[key].cur_floor in A4:
                                        A4.remove(system.elevators[key].cur_floor)
                                    system.elevators[key].Aimminglist=[system.elevators[key].Aimminglist[0]]+A4
                                    peoplecount = peoplecount + 1
                                else:
                                    j=j+1
                            if len(system.elevators[key].remain_list)==system.elevators[key].capacity:
                                pass
                            else:
                                if (system.elevators[key].direction == "up" ) or ((system.elevators[key].direction =='stay') and (len(pools[system.elevators[key].cur_floor].pool_up)>=len(pools[system.elevators[key].cur_floor].pool_down))):
                                    z=0
                                    while z<len(pools[system.elevators[key].cur_floor].pool_up):
                                        cus=pools[system.elevators[key].cur_floor].pool_up[z]
                                        system.elevators[key].add_customer(cus)
                                        pools[system.elevators[key].cur_floor].Uppoolremove(cus)
                                        if len(system.elevators[key].remain_list) == system.elevators[key].capacity:
                                            break
                                elif (system.elevators[key].direction == "down") or (system.elevators[key].direction =='stay' and len(pools[system.elevators[key].cur_floor].pool_up)<len(pools[system.elevators[key].cur_floor].pool_down)):
                                    z=0
                                    while z<len(pools[system.elevators[key].cur_floor].pool_down):
                                        cus=pools[system.elevators[key].cur_floor].pool_down[z]
                                        system.elevators[key].add_customer(cus)
                                        pools[system.elevators[key].cur_floor].Downpoolremove(cus)
                                        if len(system.elevators[key].remain_list) == system.elevators[key].capacity:
                                            break
                                else:
                                    pass
                                system.elevators[key].requireIn.sort()
                            for i in system.elevators[key].requireIn:
                                if i not in system.elevators[key].Aimminglist[1:]:
                                    system.elevators[key].Aimminglist.append(i)
                                Aimin=system.elevators[key].Aimminglist[1:]
                                Aimin.sort()
                                system.elevators[key].Aimminglist=[system.elevators[key].Aimminglist[0]]+Aimin
                    else:
                        count[key] = count[key] + 1
                        if system.elevators[key].Aimminglist[1]==system.elevators[key].cur_floor or system.elevators[key].Aimminglist[(len(system.elevators[key].Aimminglist)-1)]==system.elevators[key].cur_floor:
                            #print 100,system.elevators[key].Aimminglist
                            i=0
                            while i<len(system.elevators[key].remain_list):
                                cus=system.elevators[key].remain_list[i]
                                if cus.dest_floor == system.elevators[key].cur_floor:
                                    system.elevators[key].cancel_customer(cus)
                                    A4=system.elevators[key].Aimminglist[1:]
                                    if system.elevators[key].cur_floor in A4:
                                        A4.remove(system.elevators[key].cur_floor)
                                    system.elevators[key].Aimminglist=[system.elevators[key].Aimminglist[0]]+A4
                                    peoplecount = peoplecount + 1
                                else:
                                    i=i+1

                            if len(system.elevators[key].remain_list)==system.elevators[key].capacity:
                                pass
                            else:
                                if (system.elevators[key].direction == "up" ) or ((system.elevators[key].direction =='stay') and (len(pools[system.elevators[key].cur_floor].pool_up)>=len(pools[system.elevators[key].cur_floor].pool_down))):
                                    z=0
                                    while z<len(pools[system.elevators[key].cur_floor].pool_up):
                                        cus=pools[system.elevators[key].cur_floor].pool_up[z]
                                        system.elevators[key].add_customer(cus)
                                        pools[system.elevators[key].cur_floor].Uppoolremove(cus)
                                        if len(system.elevators[key].remain_list) == system.elevators[key].capacity:
                                            break


                                elif (system.elevators[key].direction == "down") or (system.elevators[key].direction =='stay' and len(pools[system.elevators[key].cur_floor].pool_up)<len(pools[system.elevators[key].cur_floor].pool_down)):
                                    z=0
                                    while z<len(pools[system.elevators[key].cur_floor].pool_down):
                                        cus=pools[system.elevators[key].cur_floor].pool_down[z]
                                        system.elevators[key].add_customer(cus)
                                        pools[system.elevators[key].cur_floor].Downpoolremove(cus)
                                        if len(system.elevators[key].remain_list) == system.elevators[key].capacity:
                                            break
                                else:
                                    pass
                            system.elevators[key].requireIn.sort()
                            for i in system.elevators[key].requireIn:
                                if i not in system.elevators[key].Aimminglist[1:]:
                                    system.elevators[key].Aimminglist.append(i)
                                Aimin=system.elevators[key].Aimminglist[1:]
                                Aimin.sort()
                                system.elevators[key].Aimminglist=[system.elevators[key].Aimminglist[0]]+Aimin

        else:
            return step


#for i in range(50):
k = main(2000)
print(k)


