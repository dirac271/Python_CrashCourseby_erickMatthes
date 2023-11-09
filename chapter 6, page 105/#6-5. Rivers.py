#6-5. Rivers:
rivers = {'nile': 'egypt','Ganges':'India','Mississipi River':'United States'}
for river, country in rivers.items():
    print(f"The river {river} through {country}")
print("\nNow the just the countries")
for river in rivers.values():
    print(river.title())
print("\nNow the just the rivers")
for country in rivers.keys():
    print(country.title())