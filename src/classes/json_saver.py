import json

from src.abstract_classes.saver import Saver
from src.classes.vacancy import Vacancy
from src.utils.utils import get_list_vacancies_from_json_file


class JSONSaver(Saver):
    """Класс для представления сохранения данных в JSON-файл"""
    path = 'vacancies.json'

    def write_vacancies(self, vacancies_list):
        """Записывает список вакансий в JSON-файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.get_dict_from_vacancies_list(vacancies_list), file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_dict_from_vacancies_list(vacancies_list):
        """Возвращает список вакансий для записи в JSON-файл"""
        vacancies_dict = [{'vacancies': []}]

        for item in vacancies_list:
            vacancies_dict[0]['vacancies'].append({
                'id': item.id_vacancy,
                'name_vacancy': item.name_vacancy,
                'url_vacancy': item.url_vacancy,
                'salary_vacancy_from': item.salary_vacancy_from,
                'salary_vacancy_to': item.salary_vacancy_to,
                'currency': item.currency,
                'requirements_vacancy': item.requirements_vacancy
            })

        return vacancies_dict

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию в JSON-файл"""
        vacancies_from_json_file = get_list_vacancies_from_json_file()
        vacancies_from_json_file.append(vacancy)
        self.write_vacancies(vacancies_from_json_file)

    def get_vacancies_by_salary(self, salary):
        """Возвращает список вакансий, зарплата которых равна salary"""
        vacancies_from_json_file = get_list_vacancies_from_json_file()
        found_vacancies_by_salary = []

        for vacancy in vacancies_from_json_file:
            if salary == vacancy.salary_vacancy_to or salary == vacancy.salary_vacancy_from:
                found_vacancies_by_salary.append(vacancy)

        return found_vacancies_by_salary

    def delete_vacancy(self, id_):
        """Удаляет вакансию из JSON-файла по id"""
        vacancies_from_json_file = get_list_vacancies_from_json_file()
        index = None

        for i, vacancy in enumerate(vacancies_from_json_file):
            if id_ == vacancy.id_vacancy:
                index = i
                break

        vacancies_from_json_file.pop(index)
        self.write_vacancies(vacancies_from_json_file)
