import requests, pprint
url_weather = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-23BD3471-C59A-4CD3-985D-89335C21D36D&format=JSON&locationName=%E9%9B%B2%E6%9E%97%E7%B8%A3"

data_weather = requests.get(url_weather).json()
pprint.pprint(data_weather["records"]["location"][0]["weatherElement"][1]["time"])
pop = data_weather["records"]["location"][0]["weatherElement"][1]["time"]
for p in pop:
  print("time:" , p["startTime"], "-", p["endTime"])
  print("rain?" , p["parameter"]["parameterName"] +"%")