def filter_vacancies(vacancies, filter_words):
    return [v for v in vacancies if any(word in v.description for word in filter_words)]

def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True)

def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]