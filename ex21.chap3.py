def is_prime(n):
    if n <= 1:
        print("소수가 아닙니다.")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("소수가 아닙니다.")
                return
        print(n,"은(는) 소수입니다.")

# 사용자로부터 양의 정수를 입력받음
num = int(input("숫자를 입력하세요: "))
is_prime(num)
