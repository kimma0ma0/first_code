winning_numbers=[2, 3, 9]

#복권 번호 입력받기
a,b,c=map(int,input('세 복권번호를 입력하시오:').split())

#입력된 복권 번호 출력
print(f'세 복권번호를 입력하시오: {a}, {b}, {c}

#당첨 여부 확인
matching_count=0
if a in winning_numbers:
    matching_count +=1
if b in winning_numbers:
    matching_count +=1
if c in winning_numbers:
    matching_count +=1

#당첨 금액 계산 및 출력

if matching_count ==3:
    print('상금 1억 원')
elif matching_count==2:
    print('상금 1천만 원')
elif matching_count==1:
    print('상금 1만원')
else:
    print('다음 기회에...')
    
