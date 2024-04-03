x_list=list(map(float,input("10개의 수를 입력하세요:" ).split()))

total=sum(x_list)
mean=total/10
variance=0
for i in x_list:
    variance+=(i-mean)**2    

variance/=10
std_deviation= variance**0.5

print('합:',total)
print('평균:',mean)
print('표준편차:',std_deviation)


#어렵군요..
