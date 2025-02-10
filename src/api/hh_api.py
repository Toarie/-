import requests
from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        """Абстрактный метод для получения вакансий по ключевому слову."""
        pass

class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        """
        Получает вакансии с hh.ru по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :return: Список вакансий в формате JSON.
        """
        params = {'text': keyword, 'per_page': 100}  # Параметры запроса
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            print("Данные успешно получены с hh.ru")  # Отладочное сообщение
            return response.json()['items']
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API hh.ru: {e}")  # Логирование ошибки
            return []  # Возвращаем пустой список в случае ошибки

