# Nft-Aggregator
Simple NFT aggregator build with Python, PostgreSQL and Solana API.

### Table of contents

- [Description](#Description)
- [Usage](#Usage)
- [Examples](#Examples)
- [References](#References)
- [License](#License)

## Description

Simple NFT Aggregator to collect data about NFT 
and store it inside a database.

## Usage

You simply enter a NFT address into submit box and get data about that
NFT from a database if record exists. If not record gets created and then returned
to user

![expl1](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/images/expl1.png)

![expl2](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/images/exp2.png)

#### Installation

1. Get a free Moralis API key [here](https://moralis.io/?utm_source=gads&utm_campaign=17592653460&utm_medium=143799510688&network=g&device=c&gclid=CjwKCAjwzNOaBhAcEiwAD7Tb6OuqOkFkRey8hzsv3Ahz_WVNreZKFDurSUVYoJGjAq_jsZIIMwhDSxoCS3AQAvD_BwE)
2. Clone the repo 
``` ter
git clone https://github.com/KfcEnjoyer/Nft-Aggregator.git
 ```
3. Install python packages 
```
pip install flask psycopg2 requests
```
4. Enter your API key in `config.py`
```python
headers = {
    "accept": "application/json",
    "X-API-Key": "Your API key"
}
```
5. Configure your Database in database.py
```python
connection = psycopg2.connect(database='your_db_name',
                                  host='your_host',
                                  user='your_username',
                                  password='your_password')
```
___
[Back to the top](#Nft-Aggregator)

## Examples
![image1](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/images/submit-box.png)

Paste the NFT address

![image2](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/images/database.png)

add to DB

![image3](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/images/result.png)

get the result
___
[Back to the top](#Nft-Aggregator)

## References
- [psycopg2](https://pypi.org/project/psycopg2/)
- [flask](https://flask.palletsprojects.com/en/2.2.x/) and Lecture 6 
___
[Back to the top](#Nft-Aggregator)

## License
- [License](https://github.com/KfcEnjoyer/Nft-Aggregator/blob/main/LICENSE)
___
[Back to the top](#Nft-Aggregator)