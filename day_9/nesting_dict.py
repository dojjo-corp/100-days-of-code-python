# Nesting dictionary in a dictionary
travel_log = [ 
        {
            "country": "France", 
            "total_visits": 12,
            "cities_visited":  ["Paris", "Lille", "Dijon"], 
        },
        {
            "country": "Germany", 
            "total_visits": 5,
            "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        }
    ]
# Don't change the code above

# function to add new countries to travel_log
def add_new_country(nation, visits, cities):
    travel_log.append(
            {
        "country": nation,
        "total visits": visits, 
        "cities_visited": cities,
        }
            )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
