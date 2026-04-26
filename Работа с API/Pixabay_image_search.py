import requests

def search_image(query,api_key):
    url = 'https://pixabay.com/api/'
    params = {
        'key' : api_key,
        'q' : query,
        'image_type' : 'photo',
        'per_page' : 5
    }
    response = requests.get(url, params= params)
    if response.status_code != 200:
        print(f'Ошибка: {response.status_code}')
        return None
    data = response.json()
    return data

def display_images(data):
    hits = data.get('hits', [])
    if not hits:
        print('Изображения не найдены.')
        return
    for i, hit in enumerate(hits, 1):
        print(f'{i}. {hit['tags']} - {hit['largeImageURL']}')

def main():
    api_key = input('Введите ваш API-ключ Pixabay: ').strip()
    query = input('Что ищем? (например, "котики"): ')
    data = search_image(query, api_key)
    if data:
        display_images(data)

if __name__ == '__main__':
    main()
