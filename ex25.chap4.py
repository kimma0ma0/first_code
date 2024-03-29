s1 = 'Kang Young Min'
s2 = 'Kang Young-Min'
s3 = 'Park Dong Min'
s4 = 'Park Dong-Yun'

def upper_no_bin(s):
    processed_string = s.replace(' ','').replace('-','')
    return processed_string.upper()

print(s1,'(은)는',upper_no_bin(s1),'(으)로 수정됨')
print(s2,'(은)는',upper_no_bin(s2),'(으)로 수정됨')
print(s3,'(은)는',upper_no_bin(s3),'(으)로 수정됨')
print(s4,'(은)는',upper_no_bin(s4),'(으)로 수정됨')

count_N1=upper_no_bin(s1).count('N')
count_N2=upper_no_bin(s2).count('N')
count_N3=upper_no_bin(s3).count('N')
count_N4=upper_no_bin(s4).count('N')
print(upper_no_bin(s1),':',count_N1,'개의 N이 나타남')
print(upper_no_bin(s2),':',count_N2,'개의 N이 나타남')
print(upper_no_bin(s3),':',count_N3,'개의 N이 나타남')
print(upper_no_bin(s4),':',count_N4,'개의 N이 나타남')





