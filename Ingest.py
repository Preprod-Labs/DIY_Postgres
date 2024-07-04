# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Harish S
        # Role: Architect
        # Code ownership rights: Harish S
    # Version:
        # Version: V 1.0 (July 1)
            # Developer: Harish S
     
    # Description: This code enables CRUD operations in REDIS to store csv data
    
# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Python 3.10.13 -> pip install 
        #psycopg2-binary 2.9.9 -> pip install psycopg2-binary 
        #Pandas 2.2.1 -> pip install Pandas==2.2.1

# Import Libraries

import pandas as pd
from sqlalchemy import create_engine

# Load the data
path=input("Enter the path to save csv:")

# PostgreSQL connection details
db_username = input('enter username:') #username created in postgres
db_password = input('enter password:') #password provided in postgres
db_host = "localhost"#localhost
db_port = "5432"
db_name = input('enter database name:') # our selected database name
db_table =input('Enter the table name:') # our selected table name 

# Create the connection
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Read data from the PostgreSQL table into a pandas DataFrame
df = pd.read_sql(f'SELECT * FROM {db_table}', engine)

# Export the DataFrame to a CSV file
df.to_csv(path+'Ingestpgres.csv', index=False)

print("Data exported successfully.")
