#!/usr/bin/python3
import requests
import json
import webbrowser
from random import randint
from datetime import date
import os
import settings, urllib.request

NASAAPI = "https://api.nasa.gov/planetary/apod?"

## Import NASA API from dotenv
NASACREDS = os.getenv("NASA_API")

def getRandomDate():
    days30 = [4, 6, 9, 11]
    days31 = [1,3,5,7,8,10,12]
    month = randint(1,12)
    if month in days30:
        day = randint(1,30)
    elif month in days31:
        day = randint(1,31)
    else:
        day = randind(1,28)
    year = randint(1996, 2020)
    datestring = f'{str(year)}-{str(month)}-{str(day)}'
    return datestring

def main():
    """
    Fetches a single picture from the NASA APOD and opens in default browser
    :param date: API specific formatted date, YYYY-MM-DD
    :return: N/A
    """
    NASAAPOD = "https://api.nasa.gov/planetary/apod?"

    ## grab picture from birthday last year
    randomDay = getRandomDate()

    ## Call the webservice with our key
    apod = requests.get(f'{NASAAPOD}date={randomDay}&api_key={NASACREDS}').json()
    print(apod['url'])

    ## Display picture in default browser
    # input("\nPress Enter to open the NASA Picture of the Day from YOUR birthday, last year!")
    # webbrowser.open(apod["url"])

    return urllib.request.urlopen(apod['url']).read()


if __name__ == "__main__":
    main()
