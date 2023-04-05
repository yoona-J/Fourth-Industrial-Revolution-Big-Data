# 유임승차 비율이 가장 높은 역 찾기

import csv
file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/2주차/subway.csv', 'r')
data = csv.reader(file)
next(data)

mx = -1
# 비율 설정(%)
rate = 0.0
# 역 이름
mx_station = ''

# 반복문
for row in data:
    # 4에서 7까지의 수를 i라는 변수에 대입할 때
    for i in range(4, 8):

        # row 4부터 7까지 쉼표 삭제
        row[i] = int(row[i].replace(',', ''))

    # 만약 유임승차 + 무임승차 값이 0이면 계산하지 말고 다음 줄로 넘기기
    if row[4] + row[6] == 0:
        continue

    # 유임승차 / 유임승차 + 무임승차 => 승차인원 대비 유임승차 비율이 가장 높은 곳을 파악하기 위함
    rate = row[4] / (row[4] + row[6])

    # rate 값이 mx보다 크면 rate값을 mx에 대입한다.
    if rate > mx:
        mx = rate
        # 역 이름 + 호선 명으로 mx_station 값에 대입
        mx_station = row[3] + ' ' + row[1]

#mx*100으로 정수를 나타낸 후 소숫점 뒷자리가 2자리 이상이면 반올림(round)해주기
print(mx_station, round(mx*100, 2))