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
      self.printables = {'temps_stuff':["temp", "temp_min", "temp_max"], "wind_speed":"speed", "weather_description":"description"}

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
      
      #print(coordinates) #print statement to view the response object from the coordinates custom _gets method call. In debugging this is a good place to put a breakpoint to observe the response/script behaviour

      latitude = coordinates['lat'] # incorrect JSON key, expected lat
      longitude = coordinates['lon'] # incorrect JSON key, expected lon

      return latitude, longitude

  def string_printer(self, payload: dict): 
     """
     Requires: 
      1) daily weather response object parsed via response.json(). Expects type dictionary.
      2) self.printables: iterable list of keys for the response object in `payload`
     Modifies: parseses, formats, joins, and prints a list of values that are returned from the openweather api
     Returns: formatted payload arrary that is finally joined as a string showing the requested key and its associated value.
      ex: "..., temp 53.78 degrees farenheight, ..."
     """
     
     printed = []
    # Lambda used due to low use 'throwaway' function
    # Chooses string to decorate units with based on the unit specification passed in with the `--units` flag.
    # Returns a dict that contains the unit description strings for both tempurature and speed. 
    # !!! MUST ACCESS THE DICT AT THE CORRECT INDEX FOR THE DECORATOR TYPE !!!  

     unit_str = lambda : {'standard': {'temp' :'kelvin', 'speed' : 'm/s'},
                             'imperial': {'temp' :'farenheight', 'speed' : 'mph'}, 
                             'metric': {'temp' :'celsius', 'speed' : 'm/s'}
                             }.get(str(self.args.units.lower()))

     #tempurature access and formatting.
     temps_stuff = self.printables['temps_stuff']
     printed +=  [f"""{printable}: {payload['main'][str(printable)]} degrees {unit_str()['temp']}""" for printable in temps_stuff]
        
     
    #weather description accessing and formatting
     weather_descr_key = str(self.printables['weather_description'])
     printed.append(f"{weather_descr_key}: {payload['weather'][0][weather_descr_key]}" )

    #wind speed description accessing and formatting

     wind_spd_key = str(self.printables['wind_speed'])
     printed.append(f"wind {wind_spd_key}: {payload['wind'][wind_spd_key]} {unit_str()['speed']}" )

    #join print payload list and print
     print(", ".join(printed))


  def get_daily_weather(self, latitude: str, longitude: str):

    #modify weather URL to include units argument in URL. Instead of passing units as an argument, I should've referenced the self.args object to eliminate duplicated code.
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units={self.args.units}&appid={self.api_key}"
    response = self._get(weather_url)
    #call string printer method to print
    self.string_printer(response.json())

if __name__ == "__main__":

  if not API_KEY:
    print("API key does not exist for open weather")
    sys.exit(1)

  parser = argparse.ArgumentParser(description= 'Generates current weather data')
  parser.add_argument('--zip', type=str, help="enter zipcode for weather data", required=True)
  parser.add_argument('--country', '-c', type=str, default='US', help="enter country abbreviation")
  
  #add CLI flags for units resource as requested in step 2
  parser.add_argument('--units', type=str, default='standard', help="enter units options:[standard, metric, imperial]")
  args = parser.parse_args()

  weather = Weather(args)
  latitude, longitude = weather._get_coord()
  weather.get_daily_weather(latitude, longitude)
