import requests
import json
from time import sleep

from src.classes.vacancy import Vacancy

# путь к файлу JSON
path = 'vacancies.json'


def load_json_from_url(url, *args) -> list:
    """Возвращает данные, полученные из url по заданным параметрам"""
    items: list = []

    for i in range(1):  # 5
        if len(args) == 1:
            args[0]['page'] = i
            response = requests.get(url, params=args[0])
        elif len(args) == 2:
            args[1]['page'] = i
            response = requests.get(url, headers=args[0], params=args[1])
        else:
            return []

        if response.status_code != 200:
            raise ConnectionError('Невозможно подключиться!')

        data = response.content.decode()
        response.close()
        data = json.loads(data)
        items.append(data)

    sleep(0.5)
    return items


def get_list_vacancies_from_hh(hh_vacancies) -> list:
    """Возвращает список экземпляров вакансий полученных с сайта hh.ru"""
    vacancy_list = []
    for item in hh_vacancies:
        id_ = item['id']
        name = item['name']
        url = item['alternate_url']
        salary_keys = []
        if not item['salary'] is None:
            salary_keys = list(item['salary'].keys())
        salary_from = item['salary']['from'] if 'from' in salary_keys else None
        salary_to = item['salary']['to'] if 'to' in salary_keys else None
        currency = item['salary']['currency'] if 'currency' in salary_keys else None
        requirement = item['description'] + str(item['key_skills'])
        vacancy = Vacancy(id_, name, url, salary_from, salary_to, currency, requirement)
        vacancy_list.append(vacancy)

    return vacancy_list


def get_list_vacancies_from_superjob(superjob_vacancies) -> list:
    """Возвращает список экземпляров вакансий полученных с сайта superjob.ru"""
    vacancy_list = []

    for j in superjob_vacancies:
        id_ = j['id']
        name = j['profession']
        url = j['link']
        salary_from = j['payment_from'] if j['payment_from'] else None
        salary_to = j['payment_to'] if j['payment_to'] else None
        currency = j['currency'] if j['currency'] else None
        requirement = j['vacancyRichText']
        vacancy = Vacancy(id_, name, url, salary_from, salary_to, currency, requirement)
        vacancy_list.append(vacancy)

    return vacancy_list


def get_list_vacancies_from_json_file() -> list:
    """Загружает вакансии из JSON-файла и возвращает из в списке"""
    list_vacancies_from_json_file = []
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data[0]['vacancies']:
            vacancy = Vacancy(item['id'],
                              item['name_vacancy'],
                              item['url_vacancy'],
                              item['salary_vacancy_from'],
                              item['salary_vacancy_to'],
                              item['currency'],
                              item['requirements_vacancy'])
            list_vacancies_from_json_file.append(vacancy)
    return list_vacancies_from_json_file


def filter_vacancies(entered_keywords: set) -> list:
    """Возвращает список вакансий, требования которых содержит ключевые слова из entered_keywords """
    filtered_vacancies = []
    list_vacancies = get_list_vacancies_from_json_file()
    for vacancy in list_vacancies:
        requirements = vacancy.requirements_vacancy.lower()
        if all(x in requirements for x in entered_keywords):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def sort_vacancies(list_vacancies) -> list:
    """Возвращает отсортированный по возрастанию список вакансий"""
    sorted_list = sorted(list_vacancies)
    return sorted_list


def get_top_vacancies(list_vacancies, top_n) -> list:
    """Возвращает N-ное кол-во вакансий или все, если top_n = 0"""
    if top_n:
        top_n = int(top_n)
        return list_vacancies[-top_n:]
    else:
        return list_vacancies


def find_hh_vacancies(hh_api, name_vacancy):
    """Возвращает список данных вакансий, полученный с сайта hh.ru"""
    hh_vacancies = hh_api.get_vacancies(name_vacancy)
    list_vacancies_from_hh = get_list_vacancies_from_hh(hh_vacancies)
    return list_vacancies_from_hh


def find_sj_vacancies(superjob_api, name_vacancy):
    """Возвращает список данных вакансий, полученный с сайта superjob.ru"""
    superjob_vacancies = superjob_api.get_vacancies(name_vacancy)
    list_vacancies_from_sj = get_list_vacancies_from_superjob(superjob_vacancies)
    return list_vacancies_from_sj
