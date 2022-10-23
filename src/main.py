from flask import Flask, render_template, request
import requests, database, config

app = Flask(__name__)

nftAddress = ""

responce = ""

database.create_table()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/address", methods=["POST"])
def get_address():
    nftAddress = request.form['paste-address']
    price = requests.get(url="https://solana-gateway.moralis.io/account/mainnet/"+nftAddress+"/balance", headers=config.headers).json()
    responce = requests.get(url="https://solana-gateway.moralis.io/nft/mainnet/"+nftAddress+"/metadata", headers=config.headers).json()
    if database.check_if_exists(nftAddress):
        value = database.get_value(nftAddress)
        return render_template("index.html", mint=value[0][0], name=value[0][1], standard=value[0][2], solana=value[0][3])
    else:
        database.insert_value(responce['mint'],responce['name'],responce['standard'],price['solana'])
        value = database.get_value(nftAddress)
        return render_template("index.html", mint=value[0][0], name=value[0][1], standard=value[0][2], solana=value[0][3])


@app.route("/in")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)



