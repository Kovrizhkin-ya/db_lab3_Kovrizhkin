DO $$
	DECLARE
		countries_id country.country_id%TYPE;
		countries_name country.country_name%TYPE;
		countries_code country.country_code%TYPE;
		countries_area country.country_area%TYPE;
		countries_land_area_km country.country_land_area_km%TYPE;
		
	BEGIN
	
		countries_id := 4;
		countries_name := 'Country';
		countries_code := 'C';
		FOR counter IN 1..4
			LOOP
				INSERT INTO country(country_id, country_name, country_code, country_area, country_land_area_km) 
				VALUES (counter + countries_id, countries_name || counter + countries_id, countries_code || counter + countries_id, counter + countries_id * 15, counter + countries_id * 10);
			END LOOP;
	END;
$$