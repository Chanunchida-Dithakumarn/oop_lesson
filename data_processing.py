import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for name in self.table_database:
            if name == table_name:
                return name


class Table:
    def __init__(self, table_name='', table=None):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self,aggregation_key, aggregation_function):
        _list = []
        for item in self.table:
            _list.append(float(item[aggregation_key]))
        return aggregation_function(_list)

    def __str__(self):
        return f"Table: {self.table_name}, {len(self.table)}"


# Let's write code to
_cities = Table("Cities", cities)
_countries = Table("Countries", countries)

table_db = TableDB()
table_db.insert(_cities)
table_db.insert(_countries)

italy_cities = Table("Cities in Italy", _cities.filter(lambda x: x['country'] == 'Italy'))
sweden_cities = Table("Cities in Sweden", _cities.filter(lambda x: x['country'] == 'Sweden'))

table_db.insert(italy_cities)
table_db.insert(sweden_cities)

# - print the average temperature for all the cities in Italy
avg_temp_italy = italy_cities.aggregate('temperature', lambda x: sum(x) / len(x))
print(f"The average temperature of all the cities in Italy:\n{avg_temp_italy}\n")

# - print the average temperature for all the cities in Sweden
avg_temp_sweden = sweden_cities.aggregate('temperature', lambda x: sum(x) / len(x))
print(f"The average temperature of all the cities in Sweden:\n{avg_temp_sweden}\n")

# - print the min temperature for all the cities in Italy
min_temp_italy = italy_cities.aggregate('temperature', lambda x: min(x))
print(f"The min temperature of all the cities in Italy:\n{min_temp_italy}\n")

# - print the max temperature for all the cities in Sweden
min_temp_sweden = sweden_cities.aggregate('temperature', lambda x: min(x))
print(f"The max temperature for all the cities in Sweden:\n{min_temp_sweden}\n")
