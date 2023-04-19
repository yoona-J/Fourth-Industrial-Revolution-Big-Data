import folium

seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',  zoom_start=12)

folium.Marker([37.5586056, 127.0489194], popup="한양여자대학교", tooltip="한양여자대학교").add_to(seoul_map)

seoul_map.save('c:/python_2_2/hyw.html')