import requests
import json

api = "cb88e221-51ee-4694-9f62-c12319dfefea"
url = (
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY="
    + api
)
api_request = requests.get(url)
api = json.loads(api_request.content)

coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_coin": 320,
    },
    {
        "symbol": "ETH",
        "amount_owned": 100,
        "price_coin": 2.25,
    }
]

total_pl = 0

for i in range(5):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_perCoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_coin"]
            total_pl_coin = pl_perCoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin
            #------------------------------------------------------------------------#
            print(api["data"][i]["name"] + '-' + api["data"][i]["symbol"] )
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("# of coins:", coin["amount_owned"])
            print("TotalAmount Paid:", "${0:.2f}".format(total_paid))
            print("Current Value:", "${0:.2f}".format(current_value))
            print("P/L Per Coin:", "${0:.2f}".format(pl_perCoin))
            print("Total P/L with Coin", "${0:.2f}".format(total_pl_coin))

            print("--------------------------------------")
print()
print("Total P/L for Portfolio:", "${0:.2f}".format(total_pl))
