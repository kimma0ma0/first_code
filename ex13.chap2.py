#2.12 그냥풀어봄
#radius=11
# PI=3.141592
#circum=2*PI*radius
#area=PI*radius*radius
#print(f'원의 반지름=11, 원의 둘레={circum}, 원의면적={area}')

r= int(input('원의 반지름을 입력하세요:'))
PI=3.141592
circum=2*PI*r
area=PI*r*r

print(f'원의 둘레={circum}, 원의 면적={area}')
