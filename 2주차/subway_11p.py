# 유무임 승하차 인원이 가장 많은 역

import csv
file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/2주차/subway.csv', 'r')
data = csv.reader(file)
next(data)

# 리스트를 4개씩 만들기
mx = [-1] * 4
mx_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']
# 값 초기화 확인
print(mx, mx_station, label)

for row in data:
    for i in range (4, 8):
        # 값에 쉼표 지우기
        row[i] = int(row[i].replace(',', ''))

        # row의 값이 -1보다 크면
        if row[i] > mx[i - 4]:
            # row의 값을 각 리스트에 대입(반복해서 가장 큰 수를 찾아낸다)
            mx[i - 4] = row[i]
            mx_station[i - 4] = row[3] + ' ' + row[1]

# i 값을 0부터 3까지 돌릴 때,
for i in range(4):
    print(label[i] + ": " + mx_station[i], mx[i])