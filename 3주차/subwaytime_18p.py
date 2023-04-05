# 출근 시간 (아침 7시) 사람들이 가장 많이 타고 내리는 역은 어디일까?

import csv

file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/3주차/subwaytime.csv', 'r')
data = csv.reader(file)
# next -> csv 파일의 행을 건너뛴다
next(data)
next(data)
result = []

for row in data:

    for i in range(4, 52):
        row[i] = row[i].replace(',', '')

    row[4:] = map(int, row[4:])

    # 모든 역의 7시 승차 데이터를 저장함
    result.append(row[10])

# result 변수의 길이
print(len(result))
print(result)

# pow => 제곱하는 함수

