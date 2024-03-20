#직접 해보기...
def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def find_amicable_numbers(limit):
    amicable_pairs = []
    for num1 in range(1, limit):
        num2 = sum_of_divisors(num1)
        if num1 != num2 and num2 < limit and sum_of_divisors(num2) == num1:
            amicable_pairs.append((num1, num2))
    return amicable_pairs

limit = 20000
amicable_numbers = find_amicable_numbers(limit)
print("친화수:")
for pair in amicable_numbers:
    print(f"{pair[0]}의 친화수 {pair[1]}")
