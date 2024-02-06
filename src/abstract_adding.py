from abc import abstractmethod, ABC


class AddingVacancies(ABC):

    @abstractmethod
    def add_vacancy(self, vacancies_list):
        '''
        Добавление вакансии в JSON-файл
        :param vacancies_list: список вакансий
        '''
        pass

    @abstractmethod
    def load_data(self):
        '''
        Получение данных из файла по указанным критериям
        '''
        pass

    @abstractmethod
    def delete_vacancies_datas(self):
        '''
        Удаление информации о вакансиях
        '''
        pass
