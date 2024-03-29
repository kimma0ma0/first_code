nums=list(map(float,input("숫자입력하세요:").split()))

def my_sort(*nums):
    nums=list(nums)
    nums.sort()
    for num in nums:
        return nums
print(my_sort(*nums))
