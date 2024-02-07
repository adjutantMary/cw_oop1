class Vacancy:
    """
    Класс для работы с вакансиями.
    Класс поддерживает методы сравнения вакансий
    """

    def __init__(self, vacancy_info: dict):
        self.vacancy_name = vacancy_info.get("name")
        self.vacancy_area = vacancy_info.get("area")
        self.vacancy_url = vacancy_info.get("url")
        self.salary_start = vacancy_info.get("from")
        self.salary_end = vacancy_info.get("to")
        self.currency = vacancy_info.get("currency")
        self.experience = vacancy_info.get("experience", "Не указано")
        self.requirements = vacancy_info.get("requirements", "Не указано")

    def get_average_salary(self):
        """Метод для определения средней зарплаты одной вакансии"""
        avg_salary = (self.salary_start - self.salary_end) / 2
        return avg_salary

    def __sub__(self, other):
        """Разница между зарплатами двух разных вакансий"""
        if isinstance(other, Vacancy):
            return self.get_average_salary() - other.get_average_salary()

    def get_validate_data(self):
        """Метод для валидации зарплаты.
        Способом валидации является проверка, указана зарплата или нет"""
        if self.get_average_salary() == 0 or None:
            return "Зарплата не указана"
        elif self.salary_start == self.salary_end:
            return f"{self.salary_start}"
        return f"Зарплата от {self.salary_start} до {self.salary_end}"

    # Геттеры и сеттеры для установки и изменения значений зарплаты

    @property
    def salary_start(self):
        return self._salary_start

    @salary_start.setter
    def salary_start(self, value):
        self._salary_start = value

    @property
    def salary_end(self):
        return self._salary_end

    @salary_end.setter
    def salary_end(self, value):
        self._salary_end = value
