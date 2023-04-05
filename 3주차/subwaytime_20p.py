import csv
import matplotlib.pyplot as plt

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

    # 10, 12, 14열의 값만 가져와서 더한 후 대입한다
    result.append(sum(row[10: 15: 2]))

# 작은 값 정렬
result.sort()
plt.figure(figsize=(10, 5))
# bar: 막대그래프 표현
plt.bar(range(len(result)), result)
plt.show()