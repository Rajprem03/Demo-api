import requests


def get_weather(city):
    url = "https://api.weather.com/weather"

    response = requests.get(
        url,
        params={
            "city": city
        }
    )

    data = response.json()

    return data


def display_weather(city):
    weather = get_weather(city)

    temperature = weather.get("temperature")
    humidity = weather.get("humidity")

    print("City:", city)
    print("Temperature:", temperature)
    print("Humidity:", humidity)


if __name__ == "__main__":
    display_weather("Raipur")