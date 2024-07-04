# PreProd Corp repo on DIY_Postgres basics

This repo demonstrates how to load and export data from Postgres database

File info:

1. loadpostgres.py : used to load data into postgres sql
2. ingest.py: used to export data from postgres sql
3. carsdata.csv: Masterdata used to load data into sql
4. Ingest folder: receives the csv file when exported from postgres

Libraries to install to connect Postgres with python:

psycopg2-binary

Steps to run the repo:

1) install postgres db 

Installation links :

Mac OS: 

a) brew install postgresql
b) brew services start postgresql@14 ( 14 can be replaced by your required version)

Windows:

https://www.enterprisedb.com/docs/supported-open-source/postgresql/installing/windows/

Linux:

https://ubuntu.com/server/docs/install-and-configure-postgresql


2) load the csv data using step 1
3) export csv data using step 2






