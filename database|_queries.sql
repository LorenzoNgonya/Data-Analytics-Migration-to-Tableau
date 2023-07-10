-- Create table flights for the databse along with a PK and column types
CREATE TABLE flights (
	id serial PRIMARY KEY,
	Year smallint,
	MONTH smallint,
	DayofMonth smallint,
	DayOfWeek smallint,
	DepTime numeric,
	CRSDepTime bigint,
	ArrTime numeric,
	CRSArrTime smallint,
	UniqueCarrier varchar,
	FlightNum smallint,
	ActualElapsedTime numeric,
	CRSElapsedTime numeric,
	ArrDelay numeric,
	DepDelay numeric,
	Origin varchar,
	Dest varchar, 
	Distance numeric,
	Cancelled smallint,
	Diverted smallint,
	TailNum varchar,
	AirTime numeric,
	TaxiIn numeric,
	TaxiOut numeric
);

-- Exploring the flights table.

-- Selecting all columns and checking the first 100 records in the table.
SELECT *
FROM flights
LIMIT 100;

--Counting the number of records
SELECT COUNT(*)
FROM flights;

--Which year had the most number of total inbound and outbound flights?
SELECT year, COUNT(id) as total_flights
FROM flights
WHERE cancelled != 1
GROUP BY year
ORDER BY total_flights DESC;
--It's 1995

--Which country is the most popular destination for flights?
SELECT dest, COUNT(id) as total_flights
FROM flights
WHERE cancelled != 1
GROUP BY dest
ORDER BY total_flights DESC;
--It's ORD
