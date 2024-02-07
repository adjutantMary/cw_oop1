import os.path

from .vacancy import Vacancy


class UserInteractions(Vacancy):

    '''
    Класс для реализации методов взаимодействия с пользователем
    '''

    def __init__(self, vacancy_info: dict):

        super().__init__(vacancy_info)
        self.vacancy_list = vacancy_info

    @staticmethod
    def get_search_vacancy(list_vacancies: list, keywords: list):
        '''
        Получает вакансии с ключевым словом в описании.
        :param vacancies_info: список вакансий из Vacancy
        :param keyword:ключевые слова
        :return:список вакансий, который соответствует ключевым словам
        '''

        match_vacancies = []

        for vacancy in list_vacancies:
            if isinstance(vacancy, dict):
                vacancy_object = Vacancy(vacancy)
            elif isinstance(vacancy, Vacancy):
                vacancy_object = vacancy
            else:
                raise ValueError('Некорректный формат данных')

            for k, v in vars(vacancy_object).items():
                if any(keyword.lower() in str(v).lower() for keyword in keywords):
                    match_vacancies.append(vacancy_object)
                    break

        return match_vacancies

    def sort_by_salary(self):
        '''
        Проводит сортировку вакансий по зарплате (от большей к меньшей)
        :return: отсортированный список
        '''

        return sorted(self.vacancy_list)

