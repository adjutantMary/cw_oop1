import requests
from abc_api import APIWorker

class CheckAPI(APIWorker):
    """Класс для работы с API hh.ru"""

    def __init__(self, area=113, page=0, vacancy_in_page=1):
        self.area = area
        self.page = page
        self.vacancy_in_page = vacancy_in_page

    def get_vacancy(self, vacancy_name: str, api_url="https://api.hh.ru/vacancies"):
        """
        Метод, который получает вакансии по API адресу, в зависимости от названия вакансии
        :param vacancy_name:название вакансии
        :param api_url:адрес API
        :return:
        """
        vacancy_param = {
            "Вакансия": vacancy_name,
            "Область поиска": self.area,
            "Количество вакансий": self.vacancy_in_page,
            "Страница поиска": self.page,
        }
        if api_url is None:
            raise ValueError("ValueError: API не действителен")
        try:
            response = requests.get(api_url, params=vacancy_param, headers={"apikey": api_url})
            if response.status_code == 200:
                all_vacancies = response.json()["items"]
                vacancies_list = self.__class__.digit_vacancies(all_vacancies)
                pass
            else:
                print(f"Ошибка {response.status_code}")
                return []
        except Exception:
            print("В процессе выполнения программы, была допущена ошибка класса Expection")
            return []
        return vacancies_list

    @staticmethod
    def digit_vacancies(vacancies: list) -> list:
        '''
        Оформляет список вакансий
        :param vacancies: список вакансий
        :return: список
        '''

        vacancies_list = []
        for key in vacancies:
            vacancy_name = key.get("name")
            vacancy_area = key.get("area")
            vacancy_url = f'https://hh.ru/vacancy/{key.get("id")}'
            salary = key.get("salary")
            if salary:
                salary_from = salary.get("from")
                salary_to = salary.get("to")
            else:
                salary_from = 0
                salary_to = 0
            currency = key.get("salary")["currency"]
            experience = key.get("experience")
            requirements = key.get("snippet", {}).get("requirements", "")

            info = {
                "name": vacancy_name,
                "area": vacancy_area,
                "url": vacancy_url,
                "from": salary_from,
                "to": salary_to,
                "currency": currency,
                "experience": experience,
                "requirements": requirements,
            }
            vacancies_list.append(info)
        return vacancies_list
