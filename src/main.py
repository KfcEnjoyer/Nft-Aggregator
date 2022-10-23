from flask import Flask, render_template, request
import requests
import database
import config

app = Flask(__name__)


database.create_table()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/address", methods=["POST"])
def get_address():
    nft_address = request.form['paste-address']
    price = requests.get(url="https://solana-gateway.moralis.io/account/mainnet/"+nft_address+"/balance", headers=config.headers).json()
    response = requests.get(url="https://solana-gateway.moralis.io/nft/mainnet/"+nft_address+"/metadata", headers=config.headers).json()
    if database.check_if_exists(nft_address):
        value = database.get_value(nft_address)
        return render_template("index.html", mint=value[0][0], name=value[0][1], standard=value[0][2], solana=value[0][3])
    else:
        database.insert_value(response['mint'], response['name'], response['standard'], price['solana'])
        value = database.get_value(nft_address)
        return render_template("index.html", mint=value[0][0], name=value[0][1], standard=value[0][2], solana=value[0][3])


if __name__ == "__main__":
    app.run(debug=True)
