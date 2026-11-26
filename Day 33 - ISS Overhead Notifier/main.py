import requests
from datetime import datetime, timezone, timedelta
import smtplib
import time

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your_app_password"

MY_LAT = -23.11482
MY_LONG = -46.58598

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5):
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.fromisoformat(data["results"]["sunrise"])
    sunset = datetime.fromisoformat(data["results"]["sunset"])

    local_timezone = timezone(timedelta(hours=-3))
    time_now = datetime.now(local_timezone)
    sunrise = sunrise.astimezone(local_timezone)
    sunset = sunset.astimezone(local_timezone)

    return time_now <= sunrise or time_now >= sunset


while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up!\n\nThe ISS is above you in the sky!"
            )