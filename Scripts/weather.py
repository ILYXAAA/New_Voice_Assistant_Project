from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import configparser
import os

def get_weather():
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")

    config_dict = get_default_config()
    config_dict['language'] = config['Settings']['language']
    place = config['Settings']['region']
    country = config['Settings']['country']
    country_and_place = place + ", " + country

    owm = OWM(config['Settings']['pyowm_key'])
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(country_and_place)

    w = observation.weather

    status = w.detailed_status
    temp = w.temperature('celsius')['temp']
    return ("В городе " + str(place) + " сейчас " + str(status) +
          "\nТемпература " + str(
        round(temp)) + " градусов.")
