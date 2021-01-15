#!/usr/bin/python3
import requests
import datetime
import webbrowser
import os
import settings
from random import randint

# Define NEO URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# Import NASA API from dotenv
NASACREDS = os.getenv("NASA_API")


def mars_rover():
    nasarover = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
    rovers = {
        "curiosity": ['fhaz', 'rhaz', 'mast', 'chemcam', 'mahli', 'mardi', 'navcam'],
        "opportunity": ['fhaz', 'rhaz', 'navcam', 'pancam', 'minites'],
        "spirit": ['fhaz', 'rhaz', 'navcam', 'pancam', 'minites']
    }
    rover_names = list(rovers.keys())
    solday = randint(-1, 5000)

    def get_all_pics():
        for rover in rovers:
            roverreq = requests.get(f'{nasarover}{rover}/photos?sol={solday}&api_key={NASACREDS}').json()
            with open("./roverpics.txt", "a") as output:
                output.write(f"Results for sol day {solday}\n-----------------------\n")
                for x in roverreq['photos']:
                    output.write(
                        f"{x['rover']['name']} - {x['camera']['full_name']} - -{x['earth_date']} - {x['img_src']}\n")
        print("Check the file roverpics.txt in the same directory as this program, and enjoy!")

    get_all_pics()


def show_apod(date):
    """
    Fetches a single picture from the NASA APOD and opens in default browser
    :param date: API specific formatted date, YYYY-MM-DD
    :return: N/A
    """
    nasaapod = "https://api.nasa.gov/planetary/apod?"

    # grab picture from birthday last year
    last_year_bday = find_recent_bday(date)

    # Call the webservice with our key
    apod = requests.get(f'{nasaapod}date={last_year_bday}&api_key={NASACREDS}').json()

    # Display picture in default browser
    input("\nPress Enter to open the NASA Picture of the Day from YOUR birthday, last year!")
    webbrowser.open(apod["url"])


def find_recent_bday(date):
    """
    Python 3.6 compliant date calculation from string
    :param date: String formatted as YYYY-MM-DD
    :return: Current year - 1 year, matching MM and DD as parameter
    """
    # TODO: add logic so that is birthday exists in NASA api limits returns that, otherwise returns last years picture
    date_strip = date.split("-")
    # calculate current year - one year as NASA only supports up to the current day, and only as far back at 1985
    recent_byear = (datetime.date.today() - datetime.timedelta(days=365)).strftime("%Y")
    date_strip[0] = str(recent_byear)
    last_year_bday = "-".join(date_strip)
    return last_year_bday


def config_end_day_for_neo(startdate):
    """
    Finds the end date as input + 7 days to adhere to NASA API limitations
    :param startdate: API formatted YYYY-MM-DD
    :return: Startdate + 7 days, formatted YYYY-MM-DD
    """
    # turn input into datetime object, add 7 days to it, and turn into properly formatted enddate (no access to
    # isoformat() and fromisoformat() until python 3.7+
    start_date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
    end = start_date + datetime.timedelta(days=7)
    enddate = end.date().strftime("%Y-%m-%d")
    return enddate


def nasa_neo_request(enddate, startdate):
    """
    Makes a request to NEOW based on user inputted start date and calculated end date
    :param enddate: calculated by
    :param startdate: Start date, user input or otherwise
    :return: neodata JSON object
    """
    # make a request with the request library
    neorequest = requests.get(f'{NEOURL}start_date={startdate}&end_date={enddate}&api_key={NASACREDS}')
    # strip off json attachment from our response
    neodata = neorequest.json()
    print(neodata)
    return neodata


def main():
    """
    Grabs user input for a date, and then provides functions.
    :return: Finished string to display something in tkinter
    """
    # grab start date from input
    startdate = input('Please enter your birthday(YYYY-MM-DD): ')
    # configure end date
    enddate = config_end_day_for_neo(startdate)
    # perform the actual api call
    neowdata = nasa_neo_request(enddate, startdate)

    # type check, uncomment to include and check on object response
    # this can be very helpful if the slicing is failing but looks correct, probably a bad response object
    # print(type(neowdata['near_earth_objects']))
    # print(neowdata)

    # loop over and create a list of the asteroid sizes and hazards in the range
    sizes = []
    hazards = []
    for day in neowdata['near_earth_objects']:
        for x in neowdata['near_earth_objects'][day]:

            sizes.append(x['estimated_diameter']['kilometers']['estimated_diameter_max'])
            if x['is_potentially_hazardous_asteroid']:
                hazards.append(f"{x['name']} on {day}")

    print(f'The biggest NEO was {max(sizes)} in kilometers wide.')
    print(f'{len(hazards)} potentially hazardous asteroids included:\n{hazards}.')
    # call up the apod for a birthday pic
    if input("Would you like to see the Nasa Pic of the Day from last years same day and month? (y/n)").lower() == 'y':
        show_apod(startdate)
    if input("Would you like to have a text file with links to pictures from all three Mars Rovers for a random sol "
             "of their mission? (y/n)").lower() == 'y':
        mars_rover()

    return "Program finished."


if __name__ == "__main__":
    main()
    # marsRover()
