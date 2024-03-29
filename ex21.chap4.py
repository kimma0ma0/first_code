def birth_num(front_six):
    year=int(front_six[:2])
    if year>=50:
        year+=1900
    else:
            year+=2000
    month = int(front_six[2:4])
    day=int(front_six[4:6])

    return f"{year}년 {month}월 {day}일"

front_six=input('주민등록번호 첫 6숫자 형식 입력:')
print(birth_num(front_six))
