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
