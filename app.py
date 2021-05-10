import apikey
from flask import Flask, render_template, request
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.key,
}

json = requests.get(url, params=params, headers=headers).json()

# print(json['data'])

bitcoin_as_string = json['data'][0]['name']

app = Flask(__name__)

@app.route('/')
def index():
    if request.args.get('name'):
      
      for crypto in json['data']:
        if crypto['name'] == request.args.get('name'):
          return render_template('details.html', crypto = crypto)
    return render_template('index.html', bitcoin = bitcoin_as_string, cryptos = json['data'] )

@app.route('/<name>')
def name(name):
  return name
  

if __name__ == '__main__':
    app.run(debug=True)
