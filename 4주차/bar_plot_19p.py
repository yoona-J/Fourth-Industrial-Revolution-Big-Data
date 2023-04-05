import pandas as pd
import matplotlib.pyplot as plt
# critical error만 나타나도록
import warnings
warnings.simplefilter("ignore")

# excel 데이터를 데이터프레임으로 변환
# excel이나 csv로 읽을 때는 어디가 header인지 명시 필요
file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/inoutpeople.xlsx'
df = pd.read_excel(file_path, engine='openpyxl', header=0)

# 병합된 줄(NaN)을 해당 열의 앞 데이터로 채운다.
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')

# true인 부분만 df_seoul로 저장한다. (서울에서 다른 지역으로 전출하는 데이터) -> boolean indexing
df_seoul = df[mask]

# axis=1 : 열 / axis=0 : 행
# 전출지별 열을 없앤다
df_seoul = df_seoul.drop(['전출지별'], axis=1)

# inplace=True 가 없으면 해당 줄에서만 적용되고 다음 줄에서는 적용되지 않기 때문에 꼭 넣어준다.
# inplace를 사용하지 않을 거라면 변수로 설정해서 넣어준다.
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)

# 전입지로 인덱스 변경
df_seoul.set_index('전입지', inplace=True)

# 한글 폰트
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/NGULIM.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 2010~2017년도 까지의 데이터만 리스트화
col_years = list(map(str, range(2010, 2018)))

# 서울에서 '충청남도', '경상북도', '강원도', '전라남도' 로 이동한 인구 데이터
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# 2010-2017 이동 인구 수를 합해 변수에 대입 (axis=0 : 열, axis=1 : 행)
sumbyconti = df_4.sum(axis = 1)
# print(sumbyconti)

# 가장 큰 값부터 정렬(sort)
df_total = sumbyconti.sort_values(ascending=True)

# 수평 막대그래프 그리기
plt.style.use('ggplot')
df_total.plot(kind='barh', color='cornflowerblue', width=0.5, figsize=(10, 5))
plt.title('서울 -> 타시도 인구 이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')
plt.show()