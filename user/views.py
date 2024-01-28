from django.shortcuts import render,redirect
import random
from .models import Add_property
import requests

import folium



def user_dashboard(request):
    value = "0x888asdfasdf8aa"
    if(value == None):
        return redirect('/register')
    param = {}
   
    data = Add_property.objects.filter(wallet_address=value).values()
    ct =  data.count()
    ct_pd =  0
    ct_app=  0
    ct_rj= 0
    for i in range(ct):
        print(data[i]['status'])
        if(str(data[i]['status']).lower()=='rejected'):
            ct_rj = ct_rj+1
        if(str(data[i]['status']).lower()=='pending'):
            ct_pd = ct_pd+1
        if(str(data[i]['status']).lower()=='approved'):
            ct_app = ct_app+1

    param['ctt'] = ct
    param['ct_pd'] = ct_pd
    param['ct_ap'] = ct_app
    param['ct_rj'] = ct_rj
  
    return render(request,'dashboard.html',param)


def add_data_land(request):
    
    if(request.method=="POST"):
        
        random_number = random.randint(10000000, 99999999)
        add_data = Add_property()
        add_data.wallet_address = "0x888asdfasdf8aa"
        add_data.lat = request.POST.get('latitude')
        add_data.long = request.POST.get('longitude')
        add_data.property_id = random_number
        add_data.survey_no = request.POST.get('surveyNumber')
        add_data.status = "pending"
        add_data.Total_Owners = request.POST.get('totalowners')
        add_data.document = request.FILES['Document']
        print('worked')
        add_data.save()
        return redirect('/user')
        
    return render(request,'add_land.html')



def all_land_data(request):
    value = "0x888asdfasdf8aa"
    data = Add_property.objects.filter(wallet_address=value)
    details = []
    if(data.exists()):
        data = data.values()
        for i in data:
            details.append(i)
    
    param = {
        'data':details
    }
    print(param)

    return render(request,'all_lands.html',param)

def review(request):
    return render(request,'review.html')

def wallet(request):
    return render(request,'user_wallet.html')


def land_aminities(request):

    api_key = "AIzaSyBug3gBE8wZoZqLxAZHCyVl8GNo2Gm0ARw"
    location = "23.0225,72.5714"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=5000&key={api_key}"
    response = requests.get(url)
    data = response.json()

    # Check for errors
    if data["status"] == "OK":
        amenities = data["results"]

        # Create a Folium map centered at the initial location
        map_center = [float(location.split(',')[0]), float(location.split(',')[1])]
        mymap = folium.Map(location=map_center, zoom_start=12)

        # Add markers for each amenity obtained from the API
        for amenity in amenities:
            name = amenity.get("name", "N/A")
            address = amenity.get("vicinity", "N/A")
            latitude = amenity["geometry"]["location"]["lat"]
            longitude = amenity["geometry"]["location"]["lng"]
            
            # Add markers for each amenity
            folium.Marker(
                location=[latitude, longitude],
                popup=f"Name: {name}<br>Address: {address}",
                icon=folium.Icon(color="blue")
            ).add_to(mymap)

        # Save the map to an HTML file
        mymap.save("template/map_with_markers.html")
    else:
        print(f"Error: {data['status']}")

    
    return render(request,'map_with_markers.html')
