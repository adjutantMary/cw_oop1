from path import VACANCIES_PER_PAGE
from src.work_with_api import CheckAPI


def get_search(json_keeper):
    '''
    Реализация поиска вакансий на сайте и запись результатов в JSON
    '''

    search_string = input('Введите запрос для поиска вакансии: ')
    count_vacancies = input(f'Введите количество вакансий, которое вам необходимо получить (не более {VACANCIES_PER_PAGE}')

    try:
        count_vacancies = int(count_vacancies)
        if count_vacancies <= 0 or count_vacancies > VACANCIES_PER_PAGE:
            count_vacancies = VACANCIES_PER_PAGE
    except ValueError:
        count_vacancies = VACANCIES_PER_PAGE


    vacancies_list = (CheckAPI(vacancy_in_page=count_vacancies)).get_vacancy(search_string)
    if not vacancies_list:
        print('К сожалению, по вашему запросу ничего не найдено')
        return 0
    print(f'Найдено {len(vacancies_list)} вакансий\n')
    json_keeper.vacancies_to_json(vacancies_list)


def make_top_of_vacancies(vacancies_list, handler):
    '''
    Функция возвращает топ N вакансий по зарплате (N запрашивать у пользователя)
    :param vacancies_list:список полученных вакансий
    :param handler:экземпляр класса UserMethods
    :return:список вакансий или пустой список
    '''

    while True:
        user_input = int(input(f'\nВведите количество вакансий, который вы хотите вывести в топ'))
        if user_input == 0 or '':
            print(f'Число должно быть больше 0 и меньше {len(vacancies_list)}')
        else:
            try:
                if 0 < user_input < len(vacancies_list):
                    sorted_vacancies = handler.sort_by_salary()[:user_input]
                else:
                    sorted_vacancies = handler.sort_by_salary()
                lower_limit = sorted_vacancies[-1]
                highest_limit = sorted_vacancies[0]

                print(f'Диапазон зарплат от {lower_limit} до {highest_limit}')

                for vacancy in sorted_vacancies:
                    print(vacancy)

                return sorted_vacancies
            except ValueError:
                print('Введенные данные имеют некорректный формат')

