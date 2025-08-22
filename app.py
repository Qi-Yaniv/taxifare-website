import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import requests

'''
# TaxiFareModel
'''

'''
## Input information
'''


# #default value for tesssssssttt
# pickup_datetime = "2014-07-06 19:18:00"
# pickup_longitude = -74.16595458984376
# pickup_latitude =  -73.99463653564455
# dropoff_longitude =  -73.99463653564455
# dropoff_latitude =  40.82939777183173
# passenger_count = 2

# get pickup date and time
pickup_datetime = st.text_input('Pick up date and time', '2014-07-06 19:18:00') #pickup_datetime: str

#get pick up location
st.write("choose your pickup location") #pickup_longitude: float, pickup_latitude: float
default_pickup_location = [40.7128, -74.0060]
pickup_map = folium.Map(location=default_pickup_location, zoom_start=12)
folium.Marker(default_pickup_location, tooltip="Default location").add_to(pickup_map)
pickup_map_data = st_folium(pickup_map, width=700, height=500)
if pickup_map_data and pickup_map_data["last_clicked"]:
    pickup_latitude = pickup_map_data["last_clicked"]["lat"]
    pickup_longitude = pickup_map_data["last_clicked"]["lng"]
    st.success(f"Pickup location selected: Latitude {pickup_latitude}, Longitude {pickup_longitude}")

#get dropoff location
st.write("choose your dropoff location") #pickup_longitude: float, pickup_latitude: float
default_dropoff_location = [40.8128, -74.0060]
dropoff_map = folium.Map(location=default_dropoff_location, zoom_start=12)
folium.Marker(default_dropoff_location, tooltip="Default location").add_to(dropoff_map)
dropoff_map_data = st_folium(dropoff_map, width=700, height=500)
if dropoff_map_data and dropoff_map_data["last_clicked"]:
    dropoff_latitude = dropoff_map_data["last_clicked"]["lat"]
    dropoff_longitude = dropoff_map_data["last_clicked"]["lng"]
    st.success(f"Dropoff location selected: Latitude {dropoff_latitude}, Longitude {dropoff_longitude}")

#get passenger count
passenger_count = st.text_input('How many passenger', 2) # passenger_count: int


'''
## Retrieve a prediction
'''

#API stuff
url = "https://taxifare.lewagon.ai/predict"

X_pred = pd.DataFrame([{
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
        }])

params = X_pred.iloc[0].to_dict()
response = requests.get(url, params=params)

# fare = response.json().get("fare")
# st.write(f"🤑 Fare: ${fare:.2f}")
fare = response.json()
st.write(fare)
