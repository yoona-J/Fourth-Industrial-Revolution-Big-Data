from folium.map import Marker
import folium
import pandas as pd

df = pd.read_excel('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/5주차/university_position_seoul.xlsx')
df.set_index('name', inplace=True)

seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',  zoom_start=12)

for name, lat, lng in zip(df.index, df.latitude, df.longitude):
    folium.CircleMarker([lat, lng],
                        radius=10,
                        color='brown',
                        fill=True,
                        fill_color='coral',
                        fill_opacity=0.7,
                        popup=name
    ).add_to(seoul_map)

seoul_map.save('c:/python_2_2/seoul_univ.html')
