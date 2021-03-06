#!/usr/bin/python3
import requests
from random import randint
import os
import settings
import urllib.request

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# Import NASA API from dotenv
NASACREDS = os.getenv("NASA_API")


def get_random_date():
    """
    Generate a random date in the YYYY-MM-DD formate that NASA apis need, and in the
    range that is supported (mostly)
    :return: datestring
    """
    days30 = [4, 6, 9, 11]
    days31 = [1, 3, 5, 7, 8, 10, 12]
    month = randint(1, 12)
    if month in days30:
        day = randint(1, 30)
    elif month in days31:
        day = randint(1, 31)
    else:
        day = randint(1, 28)
    year = randint(1996, 2020)
    datestring = f'{str(year)}-{str(month)}-{str(day)}'
    return datestring


def main():
    """
    Fetches a single picture from the NASA APOD and opens in default browser
    :return: raw url binary data for use by tkinter
    """
    nasaapod = "https://api.nasa.gov/planetary/apod?"

    # grab picture from birthday last year
    random_day = get_random_date()

    # Call the webservice with our key
    apod = requests.get(f'{nasaapod}date={random_day}&api_key={NASACREDS}').json()
    print(apod['url'])

    # Display picture in default browser
    # input("\nPress Enter to open the NASA Picture of the Day from YOUR birthday, last year!")
    # webbrowser.open(apod["url"])

    return urllib.request.urlopen(apod['url']).read()


if __name__ == "__main__":
    main()
