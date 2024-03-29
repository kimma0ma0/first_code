
def area_and_circumference(r):
    fi=3.14
    area=fi*r**2
    circumference=2*fi*r
    return f"넓이:{area}, 둘레:{circumference}"

while True:
         r=int(input('반지름을 입력하시오: '))

         if r<0:
             print('프로그램을 종료합니다.')
             break
         else: 
             print(area_and_circumference(r))
            
               
             
         

