import requests
import numpy as np

data = np.random.random((100, 2))*100
url = 'https://rajsahu.app.modelbit.com/v1/DecisionTreeRegression/latest'
for each in data:
    query = {"data" : list(each)}
    r = requests.post(url, json=query)
    value = r.json()['data']
    print(f'For T23_834Ghz: {each[0]:.2f} and T30GHz: {each[1]:.2f}\tRaintime is {value}min')