"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [9.0, 8.0, 6.0, 5.0, 4.0, 10.4, 12.9]
city_population = {
    "Riga": 3423234,
    "Daugavpils": 1212,
    "Koknese": 9009,
    "Tukums": 478745,
    "Vircava": 6,
}

# TODO: Compute aggregates
average_temperature = sum(temperatures)/len(temperatures)
largest_city = max(city_population, key=city_population.__getitem__)
largest_population = city_population[largest_city]
smallest_city = min(city_population, key=city_population.__getitem__)
smallest_population = city_population[smallest_city]
total_population = sum(city_population.values())

# TODO: Print results
print("--------Temperatures--------")
print("____________________________")
print(f"Average temperature: {average_temperature:.1f} °C")
print("____________________________")
print("-------City population------")
print("____________________________")
print("Largest city:", largest_city, "-", largest_population)
print("Smallest city:", smallest_city, "-", smallest_population)
print("Total population:", total_population)
print("____________________________")
