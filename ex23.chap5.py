#23-(1)
person1 =['온달', 20, 1, 180.0, 100.0]
person3 =['평강',22, 0, 169.0, 60.0]
person4 =['혁거세', 40, 1, 150 ,50]

person_list=[person1, person3, person4]

def how_many_persons():
    n_person = len(person_list)
    print(str(n_person) +'명의 정보가 담겨 있습니다.')
how_many_persons()


#23-(2)
person1 =['온달', 20, 1, 180.0, 100.0]
person2 =['이사부',25, 1, 170.0, 70.0]
person3 =['평강',22, 0, 169.0, 60.0]
person4 =['혁거세', 40, 1, 150 ,50]
person_list=[person1, person3, person4]

def compute_average_age(person_list):
    total_age=0
    for person in person_list:
        total_age += person[1]
    return total_age/len(person_list)

average_age = compute_average_age(person_list)
print("평균 나이는"+ str(average_age)+"세입니다.")

#23-(3)
person1 =['온달', 20, 1, 180.0, 100.0]
person2 =['이사부',25, 1, 170.0, 70.0]
person3 =['평강',22, 0, 169.0, 60.0]
person4 =['혁거세', 40, 1, 150 ,50]
person_list=[person1, person3, person4]


