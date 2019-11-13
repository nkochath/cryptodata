import json

def extractData(line, crypto):
    if '>' in line:
        closingTag = line.index('>') + 1

    if "currency-name-container" in line:
        crypto['name'] = line[closingTag: -5]

    elif 'class="price"' in line:
        crypto['price'] = line[closingTag: -5]

    elif '$' in line and ',' in line and '(' not in line and '<' not in line:
        crypto['marketCap'] = line.strip()

    elif 'class="volume"' in line:
        crypto['volume24h'] = line[closingTag: -5]

    elif 'data-supply-container' in line:
        crypto['circSupply'] = line[closingTag: -8]

    elif '<span class="hidden-xs">' in line:
        crypto['ticker'] = line[closingTag: -8]

    elif '<td class="no-wrap percent-change' in line:
        crypto['percentChange24'] = line[closingTag: -6]
        writeCrypto(crypto)


def writeCrypto(crypto):
    fileName = 'CryptoData/' + crypto['name']
    text = json.dumps(crypto, indent=4)
    f = open(fileName, 'w')
    f.write(text)