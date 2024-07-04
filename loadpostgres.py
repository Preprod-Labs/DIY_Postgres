# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Harish S
        # Role: Architect
        # Code ownership rights: Harish S
    # Version:
        # Version: V 1.0 (July 1)
            # Developer: Harish S
     
    # Description: This code enables loading of data in to postgres
    
# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Python 3.10.13 -> pip install 
        #psycopg2-binary 2.9.9 -> pip install psycopg2-binary 
        #Pandas 2.2.1 -> pip install Pandas==2.2.1

# Import Libraries

import pandas as pd #data manipulation library
import psycopg2 #driver library from python 
from sqlalchemy import create_engine

# Load the data
path=input("Enter the path of csv:")
df = pd.read_csv(path+'carsdata.csv')  # Adjust the path to your CSV file

# Define database connection parameters
db_name =input("enter database_name:") #enter database name
db_user = input("enter username: ") #enter username
db_password =input("enter password: ") # password for the user entered
db_host = "localhost"
db_port = "5432"  # defaults to 5432 for PostgreSQL

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
cur = conn.cursor()

# Define SQL statement
sql = """
INSERT INTO CarData (Car_Make,Country,Country_Code)
VALUES (%s,%s,%s)
"""

# Iterate through each row in the CSV data
for row in df.to_records(index=False):  # Assuming using pandas
    cur.execute(sql, row)

# Commit the changes to the database
conn.commit()

# Close the connection
cur.close()
conn.close()

print("CSV data imported successfully!")
