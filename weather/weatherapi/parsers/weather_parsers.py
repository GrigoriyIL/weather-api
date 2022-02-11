from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup as BS

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}


class GismeteoWeather():
    def __init__(self, location="weather-kyiv-4944", days=3):
        self._location = location
        self._link = f"https://www.gismeteo.ua/{location}/"
        self._days = days if days < 10 else 9
        self._day_link = {
            0: f"{self._link}now/",
            1: f"{self._link}tomorrow/",
        }

    def _form_model_data(self, **kwargs):
        """
        Form data for django model
        """
        print(kwargs)
        model_data = {
            "location": self._location,
            "weather": kwargs.get("weather"),
            "date": kwargs.get("date"),
            "temperature": kwargs.get("temperature"),
            "weather_feel": kwargs.get("weather_feel"),
            "parse_date": kwargs.get("parse_date")

        }
        return model_data
        
    
    def _parse_now(self, day, now_html):
        """
        Parse page for endpoint /now/
        """
        html = BS(now_html, "lxml")

        weather_block = html.find('a', class_="weathertab weathertab-block tooltip")
        weather = weather_block.get("data-text")
        date = datetime.now().strftime("%Y-%m-%d")
        temperature = weather_block.find("div", class_="weather").find("span", class_="unit unit_temperature_c").text
        weather_feel = "".join(weather_block.find("div", class_="weather-feel").get_text("|").split("|")[:2])
        parse_date = datetime.today()

        return self._form_model_data(weather=weather, date=date, temperature=temperature, weather_feel=weather_feel, parse_date=parse_date)
    
    def _parse_day(self, day, html):
        """
        Parse page for endpoint /tommorow/ and /<int:day>-day/
        """
        html = BS(html, "lxml")

        parse_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        weather_block = html.find('a', class_="weathertab weathertab-block tooltip")
        weather = weather_block.get("data-text")
        date = (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
        temperature = "/".join([temperature.get_text() for temperature in weather_block.find_all("span", class_="unit unit_temperature_c")])
        weather_feel = "Неизвестно"

        return self._form_model_data(weather=weather, date=date, temperature=temperature, weather_feel=weather_feel, parse_date=parse_date)


    def _get_html(self):
        """
        Get html docs for parser
        """
        html_docs = []
        for day in range(self._days):
            link = self._day_link.get(day, f"{self._link}{day+1}-day/")
            try:
                link_response = requests.get(link, headers=headers)
                html_docs.append((day, link_response.content))
            except:
                continue

        return html_docs

    def get_weather(self):
        html_docs = self._get_html()
        model_data = []
        for html in html_docs:
            if html[0] == 0:
                try:
                    model_data.append(self._parse_now(*html))
                except:
                    continue
            else:
                try:
                    model_data.append(self._parse_day(*html))
                except:
                    continue

        return model_data