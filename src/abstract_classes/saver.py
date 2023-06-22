from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный метод для saver"""

    @abstractmethod
    def write_vacancies(self, vacancies_list):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, id_):
        pass
