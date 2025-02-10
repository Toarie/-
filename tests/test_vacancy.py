import unittest
from src.models.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancy("Python Developer", "http://example.com", "100000", "Описание")
        self.assertEqual(vacancy.title, "Python Developer")

if __name__ == "__main__":
    unittest.main()