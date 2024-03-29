def sum_range(n1,n2):
    total=0
    for i in range(n1,n2+1):
        total+=i
    return total

result1 = sum_range(10,20)
print(f"10에서 20까지의 정수의 합:{result1}")

result2 =sum_range(40,100)
print(f"40에서 100까지의 정수의 합:{result2}")
