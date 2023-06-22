from src.abstract_classes.api import API
from src.utils.utils import load_json_from_url


class SuperJobAPI(API):
    """Класс для работы с API SuperJob"""

    def __init__(self):
        self.key_word = ""
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': 'v3.r.137612813.bd5818c72723a8576cec4f28cee7b996be96cd78.7d049a14ddfd03cf4a4b956ff827cb09e699baef',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def get_vacancies(self, key_word: str) -> list:
        """ Возвращает список вакансий, содержащих ключевое слово """
        vacancies: list = []

        params = {
            'keyword': key_word,
            'town': 'Москва',
            'count': 100,
        }

        vacancies_list = load_json_from_url(self.url, self.headers, params)

        for data_from_page in vacancies_list:
            for item in data_from_page['objects']:
                vacancies.append(item)

        return vacancies
