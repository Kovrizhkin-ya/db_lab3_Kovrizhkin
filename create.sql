CREATE TABLE country (
	country_id INTEGER NOT NULL, 
	country_name VARCHAR(50) NOT NULL,
	country_code VARCHAR(3) NOT NULL,
	country_area FLOAT NOT NULL,
	country_land_area_km FLOAT NOT NULL
);

CREATE TABLE population (
	country_id INTEGER NOT NULL, 
	population_id INTEGER NOT NULL, 
	population INTEGER NOT NULL, 
	population_year INTEGER NOT NULL
); 

CREATE TABLE statistic (
	statistic_id INTEGER NOT NULL, 
	country_id INTEGER NOT NULL,
	growth_rate DECIMAL NOT NULL,
	world_percentage DECIMAL NOT NULL,
	density DECIMAL NOT NULL
);

ALTER TABLE country ADD CONSTRAINT PK_country_id
PRIMARY KEY(country_id);

ALTER TABLE population ADD CONSTRAINT PK_population_id
PRIMARY KEY(population_id);

ALTER TABLE statistic ADD CONSTRAINT PK_statistic_id
PRIMARY KEY(statistic_id);

ALTER TABLE population ADD CONSTRAINT FK_population_country
FOREIGN KEY(country_id) REFERENCES country(country_id);

ALTER TABLE statistic ADD CONSTRAINT FK_statistic_country
FOREIGN KEY(country_id) REFERENCES country(country_id);