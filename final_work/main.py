import argparse
import requests
from bs4 import BeautifulSoup
import re


def clean_country_name(country_raw):
    return re.sub(r'\[.*\]', '', country_raw).strip()


def get_country_info(country_search):
    currency_url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D1%85_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82"
    population_url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E"

    currency_response = requests.get(currency_url)
    population_response = requests.get(population_url)

    country_info = {}

    if currency_response.status_code == 200 and population_response.status_code == 200:
        currency_soup = BeautifulSoup(currency_response.text, 'html.parser')
        population_soup = BeautifulSoup(population_response.text, 'html.parser')

        currency_table = currency_soup.find('table', {'class': 'wikitable'})
        population_table = population_soup.find('table')

        for row in currency_table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) >= 2:
                country = clean_country_name(cells[0].get_text(strip=True))
                currency = cells[1].get_text(strip=True)
                country_info[country.lower()] = {'Валюта': currency}

        for row in population_table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 3:
                country_raw = columns[1].text.strip()
                population = columns[2].text.strip()
                country = clean_country_name(country_raw)
                if country.lower() in country_info:
                    country_info[country.lower()]['Население'] = population

        country_search = country_search.lower()

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Получение информации о стране")
    parser.add_argument("country_search", type=str, help="Название страны для поиска информации")

    args = parser.parse_args()
    get_country_info(args.country_search)
