m,n=map(int,input("숫자를 입력하시오:").split())

def max2(m, n):
    if m>n:
        return m
    else:
        return n
def min2(m, n):
    if m>n:
        return n
    else:
        return m

print(m,'과', n,'중 큰 수는 :', max2(m, n))
print(m,'과', n,'중 작은 수는 :',min2(m, n))
#김예진은 천재.
