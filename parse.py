# (c) Никулин Федор Николаевич 

import requests
import json

test_account = 'https://solscan.io/account/Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt#tokenAccounts'


# account = 'Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'
# url_items = f'https://api.solscan.io/account/tokens?address={account}&price=1&cluster='
# response_items = requests.get(url_items)
# data = json.loads(response_items.text())
data = json.loads(open(r'miniroyale_token_accounts\src\token-accounts.txt').read())
first = data['data']
print(first)
#item_token = '8s9zgZtAi2x5EbtVavNX3MJcUkXzVZ2NZxcH8P2EVmWX'
#tokent_data_url = f'https://api.solscan.io/account?address={item_token}&cluster='
