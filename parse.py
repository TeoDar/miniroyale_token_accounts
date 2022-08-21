# (c) https://t.me/TeoDar
import requests
import json

def _get_sample_characters():
    items = {
        'Имя':[],
        'Продано':[],
        'Аренда':[],
        'Ссылка':[],
        'Изображение':[],
        'Семейство':[],
        'Сезон':[],
    }
    return items

def _get_sample_weapons():
    items = {
        'Имя':[],
        'Продано':[],
        'Аренда':[],
        'Ссылка':[],
        'Изображение':[],
        'Семейство':[],
        'Сезон':[],
    }
    return items




def get_data(account):
    url_get_all_tokens = f'https://api.solscan.io/account/tokens?address={account}'
    url_get_account = "https://api.solscan.io/account?address="
    # Получить по API все токены на аккаунте в виде json
    response_all_tokens = requests.get(url_get_all_tokens)
    tokens = json.loads(response_all_tokens.text)['data']
    print('[INFO]: Токены получены')
    #Макет данных
    characters = _get_sample_characters()
    weapons = _get_sample_weapons()

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
                token_type = next((attr['value'] for attr in metadata.get('attributes') if attr['trait_type'] == 'Item Type'), None)
                if token_type == 'Character':
                    characters['Продано'].append(''),
                    characters['Аренда'].append(''),
                    characters['Ссылка'].append(f'https://solscan.io/token/{data["tokenAddress"]}'),
                    characters['Изображение'].append(metadata.get('image')),
                    characters['Имя'].append(metadata.get('name')),
                    characters['Семейство'].append(metadata.get('collection').get('family')),
                    characters['Сезон'].append(metadata.get('collection').get('name')),
                    for attr in metadata.get('attributes'):
                        characters[attr['trait_type']] = attr['value']
                if token_type == 'Weapon':
                    weapons['Продано'].append(''),
                    weapons['Аренда'].append(''),
                    weapons['Ссылка'].append(f'https://solscan.io/token/{data["tokenAddress"]}'),
                    weapons['Изображение'].append(metadata.get('image')),
                    weapons['Имя'].append(metadata.get('name')),
                    weapons['Семейство'].append(metadata.get('collection').get('family')),
                    weapons['Сезон'].append(metadata.get('collection').get('name')),
                    for attr in metadata.get('attributes'):
                        weapons[attr['trait_type']] = attr['value']
                print(token_type, ':   ', metadata.get('name'))
                if id > 10: break
    return characters, weapons
        
if __name__=='__main__':
    get_data()