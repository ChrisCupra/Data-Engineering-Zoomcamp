# Module 2 Homework Solutions and notes

This document shows how i end up with the answers for homework 2 of Data Engineering Zoomcamp 2026 Workflow Orchestartion with Kestra and Docker

## Question 1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

## Answer: 128.3

## How I approached it:
    In the Kestra UI after the upload you can see the preview of the size but first you have to disable any purge_files from the flow.

## Question 2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

## Answer: green_tripdata_2020-04.csv

## Question 3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

## Answer: 24,648,499

## Query used:
    select count(*) 
    from de-zoomcamp-2026-******.zoomcamp.yellow_tripdata
    where extract(year from tpep_pickup_datetime) = 2020;

## Question 4. Question 4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

## Answer: 1,734,051

## Query used: 
    select count(*) 
    from de-zoomcamp-2026-******.zoomcamp.green_tripdata
    where extract(year from lpep_pickup_datetime) = 2020;

## Question 5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file? (1 point)

## Answer: 1,925,152

## Query used:
    select count(*)
    from de-zoomcamp-2026-******.zoomcamp.yellow_tripdata_2021_03

## Question 6. Question 6. How would you configure the timezone to New York in a Schedule trigger?

## Answer: Add a timezone property set to America/New_York in the Schedule trigger configuration
