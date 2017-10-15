from pygeocoder import Geocoder
import pandas as pd
import numpy as np

data = {'Location 1': '40.50257227014022, -74.45252665605645'}

df = pd.DataFrame.from_dict(data, orient='index')

lat = []
lon = []

# For each row in a varible,
for row in df[0]:
    # Try to,
    try:
        # Split the row by comma, convert to float, and append
        # everything before the comma to lat
        lat.append(float(row.split(',')[0]))
        # Split the row by comma, convert to float, and append
        # everything after the comma to lon
        lon.append(float(row.split(',')[1]))
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

# Create two new columns from lat and lon
df['latitude'] = lat
df['longitude'] = lon

results = Geocoder.reverse_geocode(df['latitude'][0], df['longitude'][0])

print results.city, results.state, results.country