# 사용자로부터 정수 입력 받기
num = int(input("정수를 입력하시오: "))

# 입력받은 정수를 2진수로 변환하여 출력
binary_num = bin(num)
print(f"{num}의 2진수 값:", binary_num)

# 비트단위 부정 값 출력
bitwise_not = ~num
print(f"{num}의 2진수 값에 대한 비트단위 부정값:", bin(bitwise_not))
