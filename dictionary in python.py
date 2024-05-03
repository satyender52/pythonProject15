# Dictionary containing countries and their populations
countries_population = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}

# Function to print all countries and their populations
def print_countries():
    for country, population in countries_population.items():
        print(f"{country.lower()} ==> {population}")

# Function to add a new country and its population
def add_country():
    country = input("Enter the country name: ").capitalize()
    if country in countries_population:
        print("Country already exists in the dataset.")
    else:
        population = int(input("Enter the population in crores: "))
        countries_population[country] = population
        print_countries()

# Function to remove a country
def remove_country():
    country = input("Enter the country name to remove: ").capitalize()
    if country in countries_population:
        del countries_population[country]
        print_countries()
    else:
        print("Country doesn't exist!")

# Function to query population of a country
def query_country():
    country = input("Enter the country name to query: ").capitalize()
    if country in countries_population:
        print(f"Population of {country}: {countries_population[country]} crores")
    else:
        print("Country doesn't exist!")

# Main program
while True:
    action = input("Enter action (print/add/remove/query/exit): ").lower()
    if action == "print":
        print_countries()
    elif action == "add":
        add_country()
    elif action == "remove":
        remove_country()
    elif action == "query":
        query_country()
    elif action == "exit":
        break
    else:
        print("Invalid action!")
