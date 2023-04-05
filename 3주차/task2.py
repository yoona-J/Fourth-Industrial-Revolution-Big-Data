# 새벽 4시 ~ 다음날 새벽 3시 최대 승차 역 이름 및 승차 인원 출력

import csv

file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/3주차/subwaytime.csv', 'r')
data = csv.reader(file)
# next -> csv 파일의 행을 건너뛴다
next(data)
next(data)

mx = [-1] * 24
mx_station = [''] * 24

for row in data:
    for i in range(4, 52):
        row[i] = row[i].replace(',', '')

    row[4:] = map(int, row[4:])

    for j in range(24):
        num_people = row[j*2 + 4]
        if num_people > mx[j]:
           mx[j] = num_people
           mx_station[j] = row[3]

print(mx_station)
print(mx)