from path import VACANCIES_PER_PAGE
from src.work_with_api import CheckAPI


def get_search(json_keeper):
    '''
    Реализация поиска вакансий на сайте и запись результатов в JSON
    '''

    search_string = input('Введите запрос для поиска вакансии: ')
    count_vacancies = input(f'Введите количество вакансий, которое вам необходимо получить (не более {VACANCIES_PER_PAGE})')

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

def outputting_vacancies(handler, top_vacancies):
    '''
    Вывод вакансий по полученным данным
    :param handler: экземпляр класса UserMethods
    :param top_vacancies: список вакансий, полученный после сортировки в топе
    '''

    user_keywords = input('Введите ключевые слова через пробел').split()

    if user_keywords:
        user_keywords = handler.get_search_vacancy(top_vacancies, user_keywords)

        if user_keywords:
            print()
            print(f'По вашему запросу подходят {len(user_keywords)} вакансий')
            while True:
                user_choice = input('Выберите действие:\n'
                                    '0 - выйти,\n'
                                    '1 - показать все вакансии\n'
                                    '2 - сохранить вакансии ')
                if user_choice == '0':
                    print('Всего хорошего!')
                    exit(0)
                elif user_choice == '1':
                    for vacancy in top_vacancies:
                        print(vacancy)
                    break
                elif user_choice == '2':
                    pass
                    break
                else:
                    print('Некорректный ввод')
        else:
            print('Нет вакансий, которые бы соответствовали заданным критериям')
    else:
        print('Ключевые слова не были введены. Сохранить список вакансий?\n')

        while True:
            user_choice = input(input('Выберите действие:\n'
                                    '0 - выйти,\n'
                                    '1 - записать топ вакансий'))
            if user_choice == '0':
                print('Всего хорошего')
                break
            elif user_choice == '1':
                pass
            else:
                print('Неккоректный ввод')

def save_data_to_csv(handler, vacancies_list):
    '''
    Сохраняет информацию о вакансиях в csv - файл
    :param handler: экземпляр класса UserMethods
    :param vacancies_list: список вакансий
    '''

    while True:
        filename = input('Введите имя файла:\n')

        if filename == '':
            filename = 'vacancies'

        handler.convert_to_csv(filename, vacancies_list)
        break

