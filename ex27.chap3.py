#암스트롱 수 구하기..

amstrong=[]

for i in range(100,1000):
    x = i//100
    y = (i%100)//10
    z = i%10

    sum1=x*100 + y*10 +z
    sum2=x**3 + y**3 + z**3

    if sum1==sum2:
        amstrong.append(i)
        
print(amstrong)
