# (c) https://t.me/TeoDar

import requests
import json


# test_account = 'https://solscan.io/account/Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'

# Ввод аккаунта и задание API ссылок
account = 'Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'
url_get_all_tokens = f'https://api.solscan.io/account/tokens?address={account}'
url_get_account = "https://api.solscan.io/account?address="

def get_data():
    # Получить по API все токены на аккаунте в виде json
    response_all_tokens = requests.get(url_get_all_tokens)
    tokens = json.loads(response_all_tokens.text)['data']
    items = {}

    for id, data in enumerate(tokens):
        if 'tokenSymbol' in data:
            if data['tokenSymbol'] == 'MINIROYALE':
                # Получаем аккаунт токена и ссылку на метаданные о нём
                response_token_account = requests.get(url_get_account+data['tokenAddress'])
                account = json.loads(response_token_account.text)
                url_metadata = account['data']['metadata']['data']['uri']
                # Получаем метаданные токена
                response_token_metadata = requests.get(url_metadata)
                metadata = json.loads(response_token_metadata.text)
                # Словарь в который будут складываться данные по токенам
                items[id] = {
                    'Продано': '',
                    'Аренда': '',
                    'Ссылка': f'https://solscan.io/token/{data["tokenAddress"]}',
                    'Изображение': metadata.get('image'),
                    'Имя': metadata.get('name'),
                    'Семейство': metadata.get('collection').get('family'),
                    'Сезон': metadata.get('collection').get('name'),
                    'Тип токена': next((attr['value'] for attr in metadata.get('attributes') if attr['trait_type'] == 'Item Type'), None),
                }
                if id > 10: break
    with open('text.txt', 'w', encoding='utf-8') as file:
        for key, value in items.items():
            file.write(f'{key}, {value}\n')
        
if __name__=='__main__':
    get_data()