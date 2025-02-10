import unittest
from src.storage.json_saver import JSONSaver
from src.models.vacancy import Vacancy

class TestJSONSaver(unittest.TestCase):
    def test_add_vacancy(self):
        saver = JSONSaver("test_vacancies.json")
        vacancy = Vacancy("Python Developer", "http://example.com", "100000", "Описание")
        saver.add_vacancy(vacancy)
        vacancies = saver.get_vacancies(lambda x: True)
        self.assertEqual(len(vacancies), 1)

if __name__ == "__main__":
    unittest.main()