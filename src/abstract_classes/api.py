from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный метод для API"""
    @abstractmethod
    def get_vacancies(self, key_word) -> list:
        pass
