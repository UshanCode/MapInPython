import folium

location1=input("Enter the location1")
location2=input("Enter the location2")
map = folium.Map(location=[location1, location2],zoom_start=15)
folium.CircleMarker(location=[location1, location2],redius=50,popup="anyplace").add_to(map)
folium.Marker([location1, location2],popup= "unkown place").add_to(map)


map.save("map.html")