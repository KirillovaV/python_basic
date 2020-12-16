"""
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name: str, surname: str, year: int, city: str, email: str, tel_num: str) -> str:
    """
    Принимает данные пользователя в виде оотдельных параметров и выводит одной строкой
    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param tel_num: str
    :return: str
    """
    return f"Пользователь {name} {surname}, {year} года рождения, " \
           f"город проживания: {city}, email: {email}, телефон: {tel_num}"


print(user_data(name="Иван", surname="Пупкин", year=1990,
                city="Псков", email="pupkin@email.ru", tel_num="123456789"))


def user_data_1(**kwargs: dict) -> str:
    """
    Принимает данные пользователя в виде словаря и выводит одной строкой
    :param kwargs:
    :return: str
    """
    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    year = kwargs.get('year of birth', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    tel = kwargs.get('tel', '')

    return f"Пользователь {name} {surname}, {year} года рождения, " \
           f"город проживания: {city}, email: {email}, телефон: {tel}"


user_dict = {
    'name': "Иван",
    'surname': "Пупкин",
    'year of birth': 1990,
    'city': "Псков",
    'email': "pupkin@email.ru",
    'tel': "123456789",
}

print(user_data_1(**user_dict))
