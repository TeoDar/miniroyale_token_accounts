# (c) https://t.me/TeoDar

import requests
import json

# test_account = 'https://solscan.io/account/Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'

# Ввод аккаунта и задание API ссылок
account = 'Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'
url_get_all_tokens = f'https://api.solscan.io/account/tokens?address={account}'
url_get_account = "https://api.solscan.io/account?address="

# Получить по API все токены на аккаунте в виде json
response_all_tokens = requests.get(url_get_all_tokens)
tokens = json.loads(response_all_tokens.text())

items = {} # Словарь в который будут складываться данные по токенам

for id, token in enumerate(tokens):
    if 'tokenSymbol' in token:
        if token['tokenSymbol'] == 'MINIROYALE':
            response_all_tokens = requests.get(url_get_all_tokens)
            tokens = json.loads(response_all_tokens.text())