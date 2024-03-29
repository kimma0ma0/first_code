#정육면체
s=int(input('모서리의 길이:'))
def cube(s):
    v=s**3
    return v
print('모서리의 길이가',s,'인 정육면체 부피는', cube(s))


#직육면체
w,h,l=map(int,input('가로, 세로, 높이:').split())
def rectangular_prism(w,h,l):
    v=l*w*h
    return v
print('가로,세로,길이가 각각',w,',',h,',',l,'인 직육면체부 피는',rectangular_prism(w,h,l))

#원뿔

r,h=map(int,input('원뿔의 반지름, 원뿔의 높이:').split())
def cone(r,h):
    pi=3.14
    v=(1/3)*pi*(r**2)*h
    return v
print('반지름과 높이가 각각',r,h,'인 직육면체의 부피는',cone(r,h))

#구
r=int(input('구의 반지름:'))
def sphere(r):
    v=(4/3)*3.14*(r**3)
    return v
print('반지름이',r,'인 구의 부피는',sphere(r))

#원기둥
r,h=map(int,input('원기둥의 반지름, 원기둥의 높이:').split())
def cylinder(r,h):
    v=3.14*(r**2)*h
    return v
print('반지름과 높이가 각각',r,h,'인 원기둥의 부피는',cylinder(r,h))
