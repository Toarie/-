class Vacancy:
    __slots__ = ['title', 'link', 'salary', 'description']

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary):
        if salary is None:
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    @staticmethod
    def cast_to_object_list(vacancies):
        return [Vacancy(v['name'], v['alternate_url'], v.get('salary'), v['snippet']['requirement']) for v in vacancies]