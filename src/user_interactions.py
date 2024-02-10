import os.path
import csv

from path import USER_DATA
from .vacancy import Vacancy


class UserMethods(Vacancy):

    '''
    Класс для реализации методов взаимодействия с пользователем
    '''

    def __init__(self, vacancy_info: dict):
        '''
        Иниуиализация атрибут класса, записывая туда объект Vacancy
        :param vacancy_info: словарь с вакансиями,который содержится в Vacancy
        '''

        super().__init__(vacancy_info)
        self.vacancy_list = vacancy_info

    @staticmethod
    def get_search_vacancy(list_vacancies: list, keywords: list):
        '''
        Получает вакансии с ключевым словом в описании.
        :param list_vacancies: список вакансий из Vacancy
        :param keywords:ключевые слова
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

        return sorted(self.vacancy_list, key=lambda x: x.get_average_salary(), reverse=True)

    def remove_vacancies_without_salary(self):
        '''
        Возвращает список вакансий, в которых указана зарплата
        :return: list
        '''

        for vacancy in self.vacancy_list:
            if vacancy.get_average_salary() != 0:
                return vacancy

    @staticmethod
    def make_directory(dir_name):
        '''
        Создание директории для пользователя
        :param dir_name:
        '''

        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
            except OSError as e:
                print(f'Ошибка при создании директории {dir_name}: {e}')

    def convert_to_csv(self, filename: str, list_vacancies: list):
        '''
        Конвертирует данные о вакансиях в csv-файл
        :param filename: имя файла
        :param list_vacancies: список вакансий из класса Vacancy
        :return:
        '''

        self.make_directory(USER_DATA)
        filename = filename + '.csv'
        path = os.path.join(USER_DATA, filename)

        names = [
            'vacancy_name', 'vacancy_area', 'vacancy_url',
            '_salary_start', '_salary_end', 'currency',
            'experience', 'requirements'
        ]

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=names)
            writer.writeheader()

            for vacancy in list_vacancies:
                writer.writerow(vars(vacancy))
        print(f'Данные успешно сохранены под именем {filename}')

