high= 30
climb_distance= 7
down=5

real_climbed=0
days=0

while True:
    days=days+1
    real_climbed+=climb_distance
    print('day:',days, '달팽이의 위치:',real_climbed,'미터')
    if real_climbed > high:
        break
    real_climbed-=down
print('우물을 탈출하는 데 걸린 날은',days,'입니다.')
