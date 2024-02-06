import requests


def get_vacancy(api_url="https://api.hh.ru/vacancies"):
    """
    Метод, который получает вакансии по API адресу, в зависимости от названия вакансии
    :param vacancy_name:название вакансии
    :param api_url:адрес API
    :return:
    """
    # vacancy_vision = {
    #     'Вакансия': vacancy_name,
    #     'Область поиска': self.area,
    #     'Количество вакансий': self.vacancy_in_page,
    #     'Страница поиска': self.page
    # }
    if api_url is None:
        raise ValueError("ValueError: API не действителен")
    try:
        response = requests.get(api_url, headers={"apikey": api_url})
        if response.status_code == 200:
            return response.json()

    except ValueError:
        print("Чето не то")


print(get_vacancy())
