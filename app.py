import apikey
from flask import Flask, render_template
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.key,
}

json = requests.get(url, params=params, headers=headers).json()

print(json['data'][0]['name'])

bitcoin_as_string = json['data'][0]['name']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', bitcoin = bitcoin_as_string )

if __name__ == '__main__':
    app.run(debug=True)
