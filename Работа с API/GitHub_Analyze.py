import requests

def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    repos = []
    page = 1
    while True:
        response = requests.get(url, params={'per_page': 100, 'page': page})
        if response.status_code == 403:
            raise Exception('Превышен лимит запросов к API GitHub.')
        if response.status_code != 200:
            raise Exception(f'Ошибка при получении данных: {response.status_code}')
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def analyze_repos(repos):
    total_repos = len(repos)
    total_stars = 0
    most_starred_repo = {'name' : None, 'stars' : -1}
    language_count = {}

    for repo in repos:
        stars = repo.get('stargazers_count', 0)
        total_stars += stars

        if stars > most_starred_repo['stars']:
            most_starred_repo = {'name' : repo.get('name'), 'stars' : stars}

        language = repo.get('language')
        if language:
            language_count[language] = language_count.get(language, 0) + 1

    if language_count:
        top_language = max(language_count, key=language_count.get)
    else:
        top_language = None
    return {
        'total_repos' : total_repos,
        'total_stars' : total_stars,
        'most_starred_repo' : most_starred_repo,
        'top_language' : top_language,
        'language_count' : language_count
    }
def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    try:
        repos = get_repos(username)
        if not repos:
            print(f'Пользователь {username} не имеет публичных репозиториев.')
            return
        stats = analyze_repos(repos)

        print(f'\nАналитика профиля GitHub: {username}')
        print("----------------------------------")
        print(f"- Количество публичных репозиториев: {stats['total_repos']}")
        print(f"- Общее количество звёзд: {stats['total_stars']}")
        print(
            f"- Самый популярный репозиторий: {stats['most_starred_repo']['name']} (⭐ {stats['most_starred_repo']['stars']})")
        if stats['top_language']:
            print(f"- Топ языков программирования:\n")
            for language, count in stats['language_count'].items():
                print(f"  - {language}: {count} репозиториев")
        else:
            print("- Языки программирования не обнаружены.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
