import os
import pandas as pd
import requests
import datetime 

os.makedirs('data', exist_ok=True)
os.makedirs('data/archive', exist_ok=True)
os.makedirs('data/live', exist_ok=True)
url = "https://tfswildfires.com/public/api/incidents"

r = requests.get(url)
# print(r.json())
fires_dataset = []

for fire in r.json()['features']:
    print('---')
    print(fire['properties'])
    lat = fire["geometry"]["coordinates"][1]
    lng = fire["geometry"]["coordinates"][0]
    fire["properties"]["lat"] = lat
    fire["properties"]["lng"] = lng
    fires_dataset.append(fire['properties'])

df = pd.DataFrame(fires_dataset)

df.to_csv(f"data/archive/{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}.csv", index=False)
df.to_csv(f"data/live/most_recent.csv", index=False)