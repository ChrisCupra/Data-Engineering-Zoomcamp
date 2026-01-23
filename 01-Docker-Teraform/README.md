# Module 1 Homework Solutions and notes

This document shows how i end up with the answers for homework 1 of Data Engineering Zoomcamp 2026

## Question 1. What's the version of pip in the python:3.13 image?

## How I approached it
I ran the official python:3.13 Docker image and checked the installed pip version
by executing pip directly inside the container.

## Command used
docker run --rm python:3.13 pip --version

## Answer: 24.3.1

## Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

## Answer: I inspected the docker-compose.yaml file and checked that the answer is postgres:5432

## Question 3. For the trips in November 2025, how many trips had a trip_distance of less than or equal to 1 mile?

## Query used: 
    select
	    count(trip_distance)
    from public.green_taxi_data
    where trip_distance <= 1
	    and lpep_pickup_datetime >= '2025-11-01'
	    and lpep_dropoff_datetime < '2025-12-01';

## Answer: 8007

## Question 4. Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles.

## Query used:
select
	max(trip_distance) as max_distance
	,DATE(lpep_pickup_datetime) as pickup_day
from
    public.green_taxi_data
where
	trip_distance < 100
group by
	pickup_day
order by
	max_distance desc
limit 1;

## Answer: 2025-11-14 (88.03 miles)

## Question 5. Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

## Query used:
select
	sum(gtd.total_amount) as total_trips
	,z."Zone"
from
	public.green_taxi_data as gtd
join 
	zones as z
		on gtd."PULocationID" = z."LocationID"
where 
	gtd.lpep_pickup_datetime >= '2025-11-18'
	and gtd.lpep_pickup_datetime < '2025-11-19'
group by
	z."Zone"
order by
	total_trips desc
limit 1;
		
## Answer: East Harlem North (9281.92)

## Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

## Query used:
select
	max(gtd.tip_amount) as largest_tip
	,doz."Zone"
from public.green_taxi_data as gtd
join
	zones as puz
		on gtd."PULocationID" = puz."LocationID"
join 
	zones as doz
		on gtd."DOLocationID" = doz."LocationID"
where puz."Zone" = 'East Harlem North'
	and gtd.lpep_pickup_datetime >= '2025-11-01'
	and gtd.lpep_pickup_datetime < '2025-12-01'
group by doz."Zone"
order by largest_tip desc
limit 1;

## Answer: Yorkville West (81.89 tips)

## Question 7. Which of the following sequences describes the Terraform workflow for: 1) Downloading plugins and setting up backend, 2) Generating and executing changes, 3) Removing all resources?

## Answer: terraform init, terraform apply -auto-approve, terraform destroy
	init:initializes providers and backend
	apply -auto-approve: creates or updates infa
	destroy: removes all resources	