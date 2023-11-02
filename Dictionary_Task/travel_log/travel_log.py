country = input() # Name of country
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create lists from formatted


travel_log = [
  {
    "country": 'France',
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
  },
  {
    "country": 'Germay',
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"],
  }
]

#TODO- write the function that will allow new contries to be added to the travel_log
def add_new_country(country, visits, list_of_cities):
  new_country = {
    'country' : country,
    'visits' : visits,
    'cities' : list_of_cities
  }
  return travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I' ve been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favorite city was {travel_log[2]['cities'][0]}")