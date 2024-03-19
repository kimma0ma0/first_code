a,b= map(int,input('두 정수를 입력하시오:').split())
if a-b>0 : 
    print(f'{a},{b}')
else:
    print(f'{b},{a}')





#여러 값을 입력받을 때는 split() 함수를 사용하여 값을 분리해야 합니다
# 또한, 입력된 값을 두 개의 변수에 할당하기 위해 map() 함수를 사용해야 합니다.
