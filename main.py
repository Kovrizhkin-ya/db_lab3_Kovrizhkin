import psycopg2
import matplotlib.pyplot as plt

username = 'Kovrizhkin'
password = 'SQLKPIMoyParol'
database = 'World_population_data'
host = 'localhost'
port = '5432'

query_1 = '''
    DROP VIEW IF EXISTS AreaOfCountries;
    CREATE VIEW AreaOfCountries AS
    Select country_name, country_area from country
    order by country_area desc;
    SELECT * FROM AreaOfCountries;
'''

query_2 = '''
    DROP VIEW IF EXISTS CountryPopulationByYear;
    CREATE VIEW CountryPopulationByYear AS
    Select country_name, population from population
    INNER JOIN country ON population.country_id = country.country_id
    WHERE population_year = '2021';
    SELECT * FROM CountryPopulationByYear;
    '''

query_3 = '''
    DROP VIEW IF EXISTS WorldPercentageOfPopulationByCountry;
    CREATE VIEW WorldPercentageOfPopulationByCountry AS
    Select country_name, world_percentage from statistic
    INNER JOIN country ON statistic.country_id = country.country_id;
    SELECT * FROM WorldPercentageOfPopulationByCountry;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    
    countries = []
    area = []

    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        countries.append(row[0])
        area.append(row[1])
    
    x_range = range(len(countries))
 
    bar_ax.bar(x_range, area, label='Area of countries')
    bar_ax.set_title('Area of countries')
    bar_ax.set_xlabel('Countries')
    bar_ax.set_ylabel('Area')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(countries)

    countries = []
    population = []

    cur = conn.cursor()
    cur.execute(query_2)
    for row in cur:
        countries.append(row[0]) 
        population.append(row[1])
    
    pie_ax.pie(population, labels=countries, autopct='%1.1f%%')
    pie_ax.set_title("Country population by year(2021)")

    countries = []
    world_percentage = []

    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur:
        countries.append(row[0])
        world_percentage.append(row[1])
    
    graph_ax.plot(countries, world_percentage, marker='o')
    graph_ax.set_xlabel('Countries')
    graph_ax.set_ylabel('World percentage')
    graph_ax.set_title('World percentage of population by country')

    for y, g_r in zip(countries, world_percentage):
        graph_ax.annotate(g_r, xy=(y, g_r), xytext=(7, 2), textcoords='offset points')
                   
plt.show()
