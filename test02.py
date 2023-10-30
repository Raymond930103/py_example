import requests , pprint
url= "https://earthquake.usgs.gov/earthquake/feed/v1.0/summary/2.5_week.geo.json"
data = requests.get(url).json()
pprint.pprint(data)
