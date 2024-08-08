collection_url = 'https://fda.forbes.com/chart/max/bitcoin'
import requests
import pandas as pd


collections1 = requests.get(collection_url, params = {'load_amount': 10,'offset': 0})

collections1 = collections1.json()


records1 = pd.DataFrame.from_records(collections1)
print(records1)
