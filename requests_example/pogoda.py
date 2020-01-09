# API: https://www.metaweather.com/api/
# Id lokalizacji: https://www.metaweather.com/api/location/search/?query=london
# Pogoda w lokalizacji: https://www.metaweather.com/api/location/44418/
"""
Napisz program wyswietlajacy pogode dla wskazanej przez
uzytkownika lokalizacji.
Aplikacja ma działąć w trybie tekstowym:
Przykład użycia:
python pogoda.py warsaw
1. Skorzystaj z sys.argv
2. Obsłuż sytuację, gdy ktoś nie poada lokalizacji
3. Użyj namedtuple
4. Utwórz czytelne funckje - get_location_id, get_location_weather, report_weather
5. Zabezpiecz się przed wykonaniem kodu w momencie importu
"""
import requests
# import json  # nie trzeba importowc json-a, ponieważ w requests poprzez responce dostaniemy jsona
import sys
from collections import namedtuple
import tkinter

root = tkinter.Tk()

Weather = namedtuple('Weather', ['location_name', 'the_temp', 'air_pressure' , 'humidity'])
def get_location_id(location_name):
    # location_name = sys.argv[1]
    resp = requests.get (f"https://www.metaweather.com/api/location/search/?query={location_name}")
    return resp.json()[0]['woeid']

def get_location_weather(location_id):
    resp = requests.get (f"https://www.metaweather.com/api/location/{location_id}/")
    location = resp.json()['title']
    curr_date = resp.json()['consolidated_weather'][0]
    weather = Weather(
        location_name=location,
        the_temp=curr_date['the_temp'],
        air_pressure=curr_date['air_pressure'],
        humidity=curr_date['humidity']
    )
    return weather

def weather_report(weather):
    report = f""""Pogoda w {weather.location_name}
temperatura: {weather.the_temp} 
wilgotność: {weather.humidity}
ciśnienie: {weather.air_pressure}
"""
    return report

if __name__ == "__main__":
    try:
        location_name = sys.argv[1]
        location_id = get_location_id(location_name)
        weather = get_location_weather(location_id)
        report = weather_report(weather)
        print(report)
    except IndexError:
        print("Podaj nazwę lokalizacji")

# print(resp.json())
# print(resp.json()[0])
# print(resp.json()[0]['title'])
# # url_lokalizacji = "https://www.metaweather.com/api/"

# a tak wygląda podanie nazwy lokalizacji w linii komend
# (venv3.8) C:\Users\kurs\PycharmProjects\pythonalx>cd requests_example
#
# (venv3.8) C:\Users\kurs\PycharmProjects\pythonalx\requests_example>python pogoda.py warsaw
# "Pogoda w Warsaw
# temperatura: 4.85
# wilgotność: 80
# ciśnienie: 1024.0
#
#
# (venv3.8) C:\Users\kurs\PycharmProjects\pythonalx\requests_example>

