class Vacancy:
    """Класс для представления вакансий"""

    def __init__(self, id_vacancy, name_vacancy, url_vacancy, salary_vacancy_from, salary_vacancy_to, currency,
                 requirements_vacancy):
        # id вакансии
        self.id_vacancy = id_vacancy
        # название вакансии
        self.name_vacancy = name_vacancy
        # ссылка на вакансию
        self.url_vacancy = url_vacancy
        # зарплата минимальная
        self.__salary_vacancy_from = salary_vacancy_from
        # зарплата максимальная
        self.__salary_vacancy_to = salary_vacancy_to
        # валюта
        self.currency = currency
        # требования
        self.requirements_vacancy = requirements_vacancy

    @property
    def salary_vacancy_from(self):
        """Возвращает минимальную зарплату"""
        return self.__salary_vacancy_from

    @property
    def salary_vacancy_to(self):
        """Возвращает максимальную зарплату"""
        return self.__salary_vacancy_to

    def salary_for_comparison(self):
        """Возвращает зарплату для сравнения"""
        if self.__salary_vacancy_to:
            salary = int(self.__salary_vacancy_to)
        elif self.__salary_vacancy_from:
            salary = int(self.__salary_vacancy_from)
        else:
            salary = 0

        return salary

    def __gt__(self, other):
        return self.salary_for_comparison() > other.salary_for_comparison()

    def __ge__(self, other):
        return self.salary_for_comparison() >= other.salary_for_comparison()

    def __repr__(self):
        return f"{__class__.__name__}(" \
               f"'{self.id_vacancy}'" \
               f"'{self.name_vacancy}'," \
               f"'{self.url_vacancy}'," \
               f"{self.__salary_vacancy_from}," \
               f"{self.__salary_vacancy_to}," \
               f"{self.currency}," \
               f"'{self.requirements_vacancy}'"

    def __str__(self):
        return f"Название вакансии: '{self.name_vacancy}'," \
               f"Ссылка на вакансию: '{self.url_vacancy}'," \
               f"Зарплата от: {self.__salary_vacancy_from}," \
               f"Зарплата до: {self.__salary_vacancy_to}," \
               f"Валюта: {self.currency}," \
               f"Описание вакансии с требованиями: '{self.requirements_vacancy}'"
