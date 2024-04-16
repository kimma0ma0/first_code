#9.8
'''class Counter:

    def __init__(self,number=0):

        if number>=100 or number<=-1:
            self.__number=0
        else:
            self.__number=number
            
    def inc(self):
        self.__number+=1
        if self.__number >=100:
            self.__number=0

    def dec(self):
        self.__number-=1
        if self.__number <=-1:
            self.__number=0

    def reset(self):
        self.__number=0
        
    def __str__(self):
        return 'C({})'.format(self.__number)


c1=Counter(10)
c1.inc()
print('c1=',c1)

c2=Counter(1)
c2.inc()
c2.dec()
print('c2=',c2)
c2.reset()
print('c2=',c2)'''


#9.9
    
class Counter:
    
    def __init__(self,number=0):
        if number>=100 or number<=-1:
            self.__number=0
        else:
            self.__number=number
        

     def __add__(self,other):       
         result= self.__number+ other.__number
        
         if result>=100:             
             result=0
          return result
            
     def __sub__(self,other):
         result = self.__number-other.__number         
         if result <=-1:                          
             result=0             
          return result            


    def reset(self):
        self.__number=0
        
    def __str__(self):
        return 'C({})'.format(self.__number)


c1= Counter(10)
c2= Counter(20)
c3=c1+c2
c4=c1-c2
print('c3=',c3)
print('c4=',c4)

        
