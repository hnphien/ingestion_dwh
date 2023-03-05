import os
import sqlalchemy as sa
import pandas as pd


def _get_engine(host: str, database_name: str):
    # Connect to the database using Windows authentication
    DRIVER = "driver=ODBC+Driver+17+for+SQL+Server"
    engine = sa.create_engine(f"mssql+pyodbc://{host}/{database_name}?trusted_connection=yes&{DRIVER}")
    return engine


def _import_sql_folder(folder_path: str, engine, target_schema: str) -> None:
    """
    This is or importing each file in a folder to SQL Database.
    Parameters
    ----------
    folder_path : str
    engine : db engine
    """
    # Loop over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Load the data from the file into a Pandas dataframe
            df = pd.read_csv(file_path)
            base, ext = os.path.splitext(filename)
            # Write the data to the database
            df.to_sql(base, engine, schema=target_schema, if_exists='replace', index=False)
