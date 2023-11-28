import psycopg2
from sqlalchemy import create_engine
from dotenv import  dotenv_values
dotenv_values()

def get_database_conn():
    # Get database credentials from environment variable
    config = (dotenv_values('.env'))
    db_user_name = config.get('DB_USER_NAME')
    db_password =config.get('DB_PASSWORD')
    host = config.get('HOST')
    port = config.get('PORT')
    db_name =config.get('DB_NAME')
    conn = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    return conn

conn = get_database_conn()
