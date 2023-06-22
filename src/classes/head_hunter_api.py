import requests

from src.abstract_classes.api import API
from time import sleep

from src.utils.utils import load_json_from_url


class HeadHunterAPI(API):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.key_word = ""
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, key_word: str) -> list:
        """ Возвращает список вакансий, содержащих ключевое слово """
        vacancies: list = []
        text = 'NAME:' + key_word

        params = {
            'text': text,
            'area': 1,
            'per_page': 50
        }

        vacancies_list = load_json_from_url(self.url, params)

        for data_from_page in vacancies_list:
            for item in data_from_page['items']:
                url = item['url']
                more_data_from_vacancies = self.get_more_info_vacancy_from_json(url)
                vacancies.append(more_data_from_vacancies)

        return vacancies

    @staticmethod
    def get_more_info_vacancy_from_json(url):
        """Возвращает расширенную информацию о вакансии по url"""
        response = requests.get(url)
        data = response.json()
        response.close()
        sleep(0.5)
        return data
