cities=[{"name":"kathmandu","population":1000000},
    {"name":"pokhara","population":500000},
    {"name":"biratnagar","population":300000},
    {"name":"butwal","population":200000},
    {"name":"birgunj","population":150000},
    ]
 
def is_large_city(population):
    return population > 500000 
def get_population_category(population):
    if population> 900000:
        return "mega"
    elif population > 500000 :
        return "large"
    elif population > 200000:
        return "medium"
    else:
        return "small"

def find_largest_city(cities):
    largest_city= None
    for city in cities:
        if largest_city is None or city["population"] > largest_city["population"]:
            largest_city = city
    return largest_city

largest_city = find_largest_city(cities)
for c in cities:
    category = get_population_category(c["population"])
    print(f"{c['name']}: {category} city")
    if is_large_city(c["population"]):
        print(f"{c['name']}: Large city")
    else:
        print(f"{c['name']}: Small city")
print(f"The largest city is {largest_city['name']} with a population of {largest_city['population']}.") 

