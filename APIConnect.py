import requests
import json


api = 'cb88e221-51ee-4694-9f62-c12319dfefea'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD&CMC_PRO_API_KEY=' + api
api_request = requests.get(url)
api = json.loads(api_request.content)
print(api)
