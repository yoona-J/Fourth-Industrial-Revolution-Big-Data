# [과제 1] 퇴근 시간 오후 6 ~ 10시 하차 인원 최대 역 찾기

import csv

file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/3주차/subwaytime.csv', 'r')
data = csv.reader(file)
# next -> csv 파일의 행을 건너뛴다
next(data)
next(data)

mx = [-1] * 5
mx_station = [''] * 5

for row in data:
    for i in range(4, 52):
        row[i] = row[i].replace(',', '')

    row[4:] = map(int, row[4:])

    for j in range(5):
        num_people = row[j*2 + 33]
        if num_people > mx[j]:
           mx[j] = num_people
           mx_station[j] = row[3]

print(mx_station)
print(mx)