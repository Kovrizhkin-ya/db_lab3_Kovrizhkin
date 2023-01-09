import json
import psycopg2

username = 'Kovrizhkin'
password = 'SQLKPIMoyParol'
database = 'World_population_data'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:

    cur = conn.cursor()
    
    for table in ('country', 'population','statistic'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('Kovrizhkin03_DB.json', 'w') as outf:
    json.dump(data, outf, default = str, indent=4)
