# (c) https://t.me/TeoDar


import requests
import json


# test_account = 'https://solscan.io/account/Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'

# Ввод аккаунта и задание API ссылок
account = 'Epwf6ZXSY55Kwov4bhZmnEhF4BDyqbTUWC7f1oNRCrjt'
url_get_all_tokens = f'https://api.solscan.io/account/tokens?address={account}'
url_get_account = "https://api.solscan.io/account?address="

def get_data(account):
    # Получить по API все токены на аккаунте в виде json
    response_all_tokens = requests.get(url_get_all_tokens)
    tokens = json.loads(response_all_tokens.text)['data']
    print('[INFO]: Токены получены')
    #Макет данных
    items = {
        'Имя':[],
        'Продано':[],
        'Аренда':[],
        'Ссылка':[],
        'Изображение':[],
        'Семейство':[],
        'Сезон':[],
        'Тип токена':[]
    }

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
                items['Продано'].append(''),
                items['Аренда'].append(''),
                items['Ссылка'].append(f'https://solscan.io/token/{data["tokenAddress"]}'),
                items['Изображение'].append(metadata.get('image')),
                items['Имя'].append(metadata.get('name')),
                items['Семейство'].append(metadata.get('collection').get('family')),
                items['Сезон'].append(metadata.get('collection').get('name')),
                items['Тип токена'].append(next((attr['value'] for attr in metadata.get('attributes') if attr['trait_type'] == 'Item Type'), None))
                print(metadata.get('name'))
                if id > 10: break
    return items
        
if __name__=='__main__':
    get_data()