import os.path
import json

from abc_json import AddingVacancies
from path import JSON_DATA


class SavingInJSON(AddingVacancies):
    """
    Класс для сохранения информации о вакансиях в JSON-файл
    Также реализация методов для работы с файлом
    """

    def __init__(self, file):
        self.file = os.path.join(JSON_DATA, file)

    def vacancies_to_json(self, vacancies_list):
        """
        Запись вакансий в JSON файл
        :param vacancies_list: список вакансий
        """

        dir_ = os.path.dirname(self.file)

        if not os.path.exists(dir_):
            try:
                os.makedirs(dir_)
            except OSError as os_error:
                print(f"Невозможно создать директорию, произошла ошибка {os_error}")
        try:
            with open(self.file, "w+") as file_:
                json.dump(vacancies_list, file_, ensure_ascii=False, indent=2)
        except Exception as error:
            print(f"Ошибка {error}, связанная с записью файла")

    def load_vacancies(self):
        """
        Считывает данные о вакансиях из сформированного JSON-файла
        """
        try:
            with open(self.file, "r+") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print("Файл не найден")

    def save_salaries(self):
        """
        Сохраняет в JSON файле только вакансии с ненулевой зп
        """

        try:
            info = self.load_vacancies()
            for item in info:
                if item["salary_start"] != 0 or item["salary_end"] != 0:
                    cleared_info = self.vacancies_to_json(item)
                    print(f"Вакансии, в которых указана зарплата: {cleared_info}")
        except FileNotFoundError:
            print("Файл не найден")
