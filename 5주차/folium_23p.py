import folium

seoul_map1 = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map2 = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',  zoom_start=12)
seoul_map3 = folium.Map(location=[37.55, 126.98], titles='Stamen Toner',  zoom_start=15)

seoul_map1.save('c:/python_2_2/seoul1.html')
seoul_map2.save('c:/python_2_2/seoul2.html')
seoul_map3.save('c:/python_2_2/seoul3.html')