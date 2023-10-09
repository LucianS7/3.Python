import requests
import sys

def main():
    city_name = input ("City:")
    api_key = input ("API_key:")
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
        r = response.json()
        temperature_in_city = float(r["main"]["temp"])
        print(f"Current temperature: {temperature_in_city}\u2103")
    except requests.RequestException:
        sys.exit("Request Exception")


if __name__ == "__main__":
    main()
