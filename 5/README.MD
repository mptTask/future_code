# Лабораторная работа 5: Получение данных о погоде

Этот скрипт на Python использует библиотеку `requests` для получения данных о погоде из API Open Meteo. Он извлекает текущую информацию о погоде, включая температуру и скорость ветра, а также почасовой прогноз на основе предоставленных координат широты и долготы.

## Как использовать

1. Убедитесь, что у вас установлена библиотека `requests`. Вы можете установить ее, выполнив следующую команду:
    ```bash
    pip install requests
    ```

2. Запустите скрипт, указав широту и долготу при запросе.
    ```bash
    python 1.py
    ```

3. Скрипт отобразит текущую информацию о погоде и почасовой прогноз.

## Детали кода

Функция `get_weather` в скрипте отправляет запрос к API Open Meteo с предоставленными широтой и долготой. Затем она обрабатывает ответ, чтобы извлечь и вывести текущие данные о погоде и почасовой прогноз.

## Автор

- **Автор:** Николай Сливинский (Nikolay Slivinskiy)
- **Веб-сайт:** [slivinskiy-group.ru](https://slivinskiy-group.ru)  | [slivinskiy-group.com](https://slivinskiy-group.com)
- **Электронная почта:** [me@slivinskiy-group.com](mailto:me@slivinskiy-group.com)
- **Курс:** Этот код был разработан в рамках курса "Код будущего".

## Лицензия

Этот код является частью курса "Код будущего", и все права принадлежат Николаю Сливинскому.

----

# Lab 5: Weather Data Retrieval

This Python script retrieves weather data using the `requests` library from the Open Meteo API. It fetches current weather information, including temperature and wind speed, as well as an hourly forecast based on the provided latitude and longitude coordinates.

## How to Use

1. Ensure you have the `requests` library installed. You can install it using:
    ```bash
    pip install requests
    ```

2. Run the script by providing the latitude and longitude when prompted.
    ```bash
    python 1.py
    ```

3. The script will display the current weather information and an hourly forecast.

## Code Details

The `get_weather` function in the script sends a request to the Open Meteo API with the provided latitude and longitude. It then processes the response to extract and print the current weather data and an hourly forecast.

## Author

- **Author:** Николай Сливинский (Nikolay Slivinskiy)
- **Website:** [slivinskiy-group.ru](https://slivinskiy-group.ru)  | [slivinskiy-group.com](https://slivinskiy-group.com)
- **Email:** [me@slivinskiy-group.com](mailto:me@slivinskiy-group.com)
- **Course:** This code was developed as part of the "Code of the Future" course.

## License

This code is part of the "Code of the Future" course, and all rights belong to Nikolay Slivinskiy.
