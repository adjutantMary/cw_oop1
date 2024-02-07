from abc import abstractmethod, ABC


class APIWorker(ABC):

    @abstractmethod
    def get_vacancy(self, vacancy_name):
        '''
        Получает список вакансий по внешнему API
        :param vacancy_name: имя вакансии
        :return: список вакансий
        '''
        pass

    @staticmethod
    @abstractmethod
    def get_digit(vacancies):
        '''
        Оформляет список вакансий
        :param vacancies: список вакансий
        :return: список
        '''

        pass
