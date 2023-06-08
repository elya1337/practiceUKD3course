import requests

def get_weather(city, date):
    api_key = '343bf79230eb53c516054d1fb8c30975'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&dt={date}&appid={api_key}&lang=uk'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = int(temperature_kelvin - 273.15)  #Convert from Kelvin to degrees Celsius (as an integer)
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f'Weather in {city} on date {date}:')
        print(f'Temperature: {temperature_celsius}°C')
        print(f'Humidity: {humidity}%')
        print(f'Detail: {description}')
    else:
        print('Failed to get weather.')

# Asking the user about the place and date
city = input('Enter the city name: ')
date = input('Enter date - dd.mm.yy: ')

get_weather(city, date)
