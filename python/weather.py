#!/usr/bin/python
import argparse
import os
import sys
from typing import Tuple

import requests


API_KEY = os.getenv('OW_API')

class Weather:

  def __init__(self, args) -> None:
      self.args = args
      self.api_key = API_KEY
      self.session = self._session()

      # Retrieve latitute and longitude
      latitude, longitude = self._get_coord()
      self.latitude = latitude
      self.longitude = longitude

  def _session(self) -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session

  def _get(self, url: str) -> requests.Response:
        response = self.session.get(url)
        response.raise_for_status()
        return response

  def _get_coord(self) -> Tuple[str,str]:
      latitude = ""
      longitude = ""
      coordinates_url= f"http://api.openweathermap.org/geo/1.0/zip?zip={self.args.zip},{self.args.country}&appid={self.api_key}"

      response = self._get(coordinates_url)
      coordinates = response.json()

      latitude = coordinates['ltu']
      longitude = coordinates['lgn']

      return latitude, longitude

  def get_daily_weather(self):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"
    self.get(weather_url)

if __name__ == "__main__":

  if not API_KEY:
    print("API key does not exist for open weather")
    sys.exit(1)

  parser = argparse.ArgumentParser(description= 'Generates current weather data')
  parser.add_argument('--zip', type=str, help="enter zipcode for weather data", required=True)
  parser.add_argument('--country', '-c', type=str, default='US', help="enter country abbreviation")
  args = parser.parse_args()

  weather = Weather(args)
  weather.get_daily_weather()
