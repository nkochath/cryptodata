import requests
import utils
crypto = {}

page = requests.get('https://coinmarketcap.com/')
f = open('cryptoPage.html', 'w', encoding='utf-8')
f.write(page.text)
f.close()

f = open('cryptoPage.html', 'r', encoding='utf-8')
line = f.readline()

while line:
    utils.extractData(line, crypto)
    line = f.readline()

f.close()


