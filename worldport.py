import requests
import zipfile
import io
import os
import pandas as pd
import pyodbc
import geopy.distance
import psycopg2
import math
from sqlalchemy import create_engine
from dotenv import  dotenv_values
dotenv_values()
from util import get_database_conn

#Function to download a zip file from a given URL
def download_zip_file(url, destination_folder):
    response = requests.get(url) 
    if response.status_code == 200:
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall(destination_folder)
        print(f"Downloaded and extracted to {destination_folder}")
    else:
        print(f"Failed to download zip file. Status code: {response.status_code}")
zip_url = "https://drive.google.com/uc?export=download&id=1VyCGCAfFuEK7vB1C9Vq8iPdgBdu-LDM4"
project_folder = r"C:\Users\HP\OneDrive\Documents\Worldport_data"
download_zip_file(zip_url, project_folder)

def read_wpi_data(access_file_path, table_name):
    conn_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_file_path}"
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    # Query to select all data from the "Wpi Data" table with double quotes around the table name
    query = f'SELECT * FROM "{table_name}"'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
mdb_file_path = os.path.join(project_folder, "WPI.mdb")
table_name = "Wpi Data"
wpi_data = read_wpi_data(mdb_file_path, table_name)
wpi_data.columns = wpi_data.columns.str.lower() 
wpi_data.to_csv('raw/worldport.csv', index=False)
print('worldport data written successfully to csv file')


def load_worldport_data():
    wpi_data = pd.read_csv('raw/worldport.csv')
    wpi_data.to_sql('wpi_data', con =get_database_conn(), if_exists = 'replace', index = False)
    print('Data loaded successfully to postgres')

load_worldport_data()









