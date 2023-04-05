# 모든 지하철역에서 시간대별 승하차 인원을 모두 더하면

import csv
import matplotlib.pyplot as plt

file = open('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/3주차/subwaytime.csv', 'r')
data = csv.reader(file)
# next -> csv 파일의 행을 건너뛴다
next(data)
next(data)

s_in = [0] * 24
s_out = [0] * 24

for row in data:
    for i in range(4, 52):
        row[i] = row[i].replace(',', '')

    row[4:] = map(int, row[4:])

    for j in range(24):
        s_in[j] += row[4 + j * 2]
        s_out[j] += row[5 + j * 2]

# for k in range(24):
#     print(s_in[k], s_out[k])

# 꺾은 선 그래프(plot)
plt.title('# of passengers getting IN and OUT by time')
plt.plot(s_in, label='IN')
plt.plot(s_out, label='OUT')
plt.xticks(range(24), range(4, 28))
plt.legend()
plt.show()