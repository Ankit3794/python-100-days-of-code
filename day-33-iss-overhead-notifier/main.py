import requests
import datetime as dt
import time
import pytz as pt

MY_LOCATION = {
    "lat": -4.022505,
    "lng": 33.571365,
    "formatted": 0
}

SUNRISE_URL = "https://api.sunrise-sunset.org/json"
ISS_API = "http://api.open-notify.org/iss-now.json"


def get_sunrise_sunset_time():
    """
    Get Sunrise time for MY_LOCATION
    :return: Hour, Minute in tuple
    """
    response = requests.get(SUNRISE_URL, params=MY_LOCATION)
    response.raise_for_status()
    data = response.json()
    sunrise_dt = dt.datetime.fromisoformat(data["results"]["sunrise"])
    sunset_dt = dt.datetime.fromisoformat(data["results"]["sunset"])
    sunrise_dt = sunrise_dt.astimezone(pt.timezone('Asia/Kolkata'))
    sunset_dt = sunset_dt.astimezone(pt.timezone('Asia/Kolkata'))
    return sunrise_dt.time(), sunset_dt.time()


def get_current_iss_position():
    """
    Gets current ISS Position
    :return: latitude, longitude value in tuple
    """
    response = requests.get(ISS_API)
    response.raise_for_status()
    data = response.json()
    iss_position = data.get("iss_position")
    return float(iss_position.get("latitude")), float(iss_position.get("longitude"))


def check_iss_is_near_me():
    """
    Checks current ISS position is near to my location based on abs difference of latitude and longitude < 2.0
    :return: True or False
    """
    current_iss_position = get_current_iss_position()
    return abs(current_iss_position[0] - MY_LOCATION.get("lat")) < 2.0 and abs(
        current_iss_position[1] - MY_LOCATION.get("lng")) < 2.0


def check_is_at_night():
    """
    Checks current time is night based on sunrise-sunset time for MY_LOCATION
    :return:
    """
    sunrise_time, sunset_time = get_sunrise_sunset_time()
    current_time = dt.datetime.now()
    return sunset_time < current_time


if __name__ == "__main__":
    while True:
        if check_iss_is_near_me() and check_is_at_night():
            print("Send Email")
        else:
            print(f"Current ISS Position {get_current_iss_position()}")
            print("Waiting for 20 seconds and trying again")
            time.sleep(20)
