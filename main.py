import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)


parameters = {
    "lat": 40.266310,
    "lng": -76.766160,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sundata = response.json()

sunrise = sundata['results']['sunrise']
sunset = sundata['results']['sunset']

time_now = datetime.now()

print(time_now)
