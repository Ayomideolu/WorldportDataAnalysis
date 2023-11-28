# World Port Index Data Migration and Analysis
This project involves migrating data from the World Port Index stored in an Access database to a modern relational database management system, specifically PostgreSQL. Additionally, the project includes the creation of data marts by analyzing the World Port Index data. The migration and analysis tasks are accomplished using a Python script (worldport.py) and a utility script (util.py).

## Project Structure
The project is organized as follows:

worldport.py: Python script containing functions for downloading the World Port Index data, connecting to the Access database, converting data to a Pandas DataFrame, exporting data to a CSV file, and loading data into the PostgreSQL database. It also includes functions to answer specific analysis questions outlined in the project requirements.

util.py: Utility script containing a function (get_database_conn) to establish a database connection using credentials from the .env file.

requirements.txt: File listing the dependencies needed to run the program.
## Installation
Before running the project, ensure you have the necessary dependencies installed. You can install them using the following command:

pip install -r requirements.txt
## Usage
Ensure that you have a PostgreSQL database set up with the appropriate credentials. Update the .env file with the database connection details.
Run the worldport.py script to execute the EL (Extract,Load) pipeline. This script performs the following tasks:

--Downloads the World Port Index data from the provided link.
--Connects to the Access database using pyodbc.
--Reads data from the 'wpi' table in the Access database into a Pandas DataFrame.
--Writes the DataFrame to a CSV file (worldport.csv) in the 'raw' folder.
--Loads the data from the CSV file into the PostgreSQL database.

## python worldport.py
After running the script, the PostgreSQL database will be populated with the World Port Index data, and the analysis questions will be answered through data marts.
## Analysis Questions
The worldport.py script includes functions to answer the following analysis questions:

1) 5 Nearest Ports to JURONG ISLAND (country = 'SG', port_name = 'JURONG ISLAND')
   Returns a DataFrame with columns port_name and distance_in_meters.

2) Country with the Largest Number of Ports with a Cargo Wharf
   Returns a DataFrame with columns country and port_count.
3) Nearest Port with Provisions, Water, Fuel Oil, and Diesel to Coordinates (32.610982, -38.706256)
   Returns information about the nearest port with provisions, water, fuel oil, and diesel.
## Acknowledgments
This project is developed by myself for GoFrieghts logistics company. Feel free to reach out for any questions or improvements.