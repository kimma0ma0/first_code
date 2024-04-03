#animal리스트 만들기
animals =['dog', 'cat', 'tiger', 'lion']

#한칸씩 왼쪽으로 이동시키고 개가 맨 오른쪽
removed_element = animals.pop(0)
animals.append(removed_element)
print('animals=',animals)

#for-in반복문

list1='I love'
print('animals =',animals)
for i in animals:
    print(list1,'',i,'.')
    
