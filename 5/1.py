import requests

def get_weather(api_url, latitude, longitude):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,wind_speed_10m',
        'hourly': 'temperature_2m,relative_humidity_2m,wind_speed_10m'
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        current_data = weather_data.get('current', {})
        current_time = current_data.get('time', '')
        current_temperature = current_data.get('temperature_2m', '')
        current_wind_speed = current_data.get('wind_speed_10m', '')

        print("Текущая погода ({})".format(current_time))
        print("Температура на 2 метрах: {}°C".format(current_temperature))
        print("Скорость ветра на 10 метрах: {} м/с".format(current_wind_speed))
        print("\n")

        hourly_data = weather_data.get('hourly', {})
        hourly_time = hourly_data.get('time', [])
        hourly_temperature = hourly_data.get('temperature_2m', [])
        hourly_relative_humidity = hourly_data.get('relative_humidity_2m', [])
        hourly_wind_speed = hourly_data.get('wind_speed_10m', [])

        print("Почасовой прогноз:")
        for i in range(len(hourly_time)):
            print("Время: {}".format(hourly_time[i]))
            print("Температура на 2 метрах: {}°C".format(hourly_temperature[i]))
            print("Относительная влажность на 2 метрах: {}%".format(hourly_relative_humidity[i]))
            print("Скорость ветра на 10 метрах: {} м/с".format(hourly_wind_speed[i]))
            print("\n")

latitude = input("Введите широту: ")
longitude = input("Введите долготу: ")

api_url = "https://api.open-meteo.com/v1/forecast"

get_weather(api_url, latitude, longitude)
