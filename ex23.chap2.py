n=int(input('세 자리 정수를 입력하세오:'))
hundreds = n//100
print("백의 자리:", hundreds)
tens =(n//10)%10
print("십의 자리:", tens)
ones =n%10
print("일의 자리:", ones)
