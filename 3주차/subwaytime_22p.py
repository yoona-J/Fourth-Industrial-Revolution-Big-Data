# 밤 11시 가장 많이 타는 역은?
# 승차 시각과 인덱스 간의 패턴 : 인덱스 = 4 + (승차 시각 - 4) * 2

import csv

file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/3주차/subwaytime.csv', 'r')
data = csv.reader(file)
# next -> csv 파일의 행을 건너뛴다
next(data)
next(data)

mx = -1
mx_station = ''
t = 23 # 밤 11시

for row in data:
    for i in range(4, 52):
        row[i] = row[i].replace(',', '')

    row[4:] = map(int, row[4:])

    mx_people = row[4+(t-4)*2]

    if mx_people > mx:
        mx = mx_people
        mx_station = row[3] + row[1]

print(mx_station, mx)