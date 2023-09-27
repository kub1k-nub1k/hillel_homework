import requests
from bs4 import BeautifulSoup
import re
from url import currency_url, population_url  # URL страниц Wiki с информацией о валютах и населении


# Функция для очистки названия страны от лишних символов в тексте статьи на Wiki
def clean_country_name(country_raw):
    return re.sub(r'\[.*\.]', '', country_raw).strip()


# Отправляем GET-запросы для получения HTML-кода страниц
currency_response = requests.get(currency_url)
population_response = requests.get(population_url)

# Создаем словарь для хранения информации о странах, валютах и населении
country_info = {}

# Проверяем успешность запросов
if currency_response.status_code == 200 and population_response.status_code == 200:
    currency_soup = BeautifulSoup(currency_response.text, 'html.parser')
    population_soup = BeautifulSoup(population_response.text, 'html.parser')

    # Ищем таблицы с информацией о валютах
    currency_table = currency_soup.find('table', {'class': 'wikitable'})
    population_table = population_soup.find('table')

    # Парсим таблицу с информацией о валютах
    for row in currency_table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >= 2:
            country = clean_country_name(cells[0].get_text(strip=True))
            currency = cells[1].get_text(strip=True)
            country_info[country.lower()] = {'Валюта': currency}

    # Парсим таблицу с информацией о населении
    for row in population_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) >= 3:
            country_raw = columns[1].text.strip()
            population = columns[2].text.strip()
            country = clean_country_name(country_raw)
            if country.lower() in country_info:
                country_info[country.lower()]['Население'] = population

    # Запрашиваем у пользователя название страны и приводим его к нижнему регистру
    country_search = input("Введите название страны, чтобы получить информацию: ").lower()

    # Выводим информацию о стране, валюте и населении
    if country_search in country_info:
        info = country_info[country_search]
        country_name = country_search.capitalize()  # Преобразуем первую букву в верхний регистр
        print(f"Страна: {country_name}")
        print(f"Валюта: {info.get('Валюта', 'Информация отсутствует')}")
        print(f"Население: {info.get('Население', 'Информация отсутствует')}")
    else:
        print("Информация о стране не найдена.")
else:
    print("Ошибка при получении страниц")
