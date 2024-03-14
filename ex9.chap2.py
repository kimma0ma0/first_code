
print("섭씨\t화씨")

for celsius in range(0, 51, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t{fahrenheit}")
