import sys
import os
import argparse
from src.extract.ingest_csv_data import _get_engine, _import_sql_folder
from src.utils.get_config import _get_config


def main(args=None):
    """
    Ingest csv data from specific folder and import to MS SQL Server
    Parameters
    ----------
    args : [str]: command line parameter list
    """

    # get arguments
    parser = argparse.ArgumentParser(description='Ingest csv folder')
    parser.add_argument("folder_path", type=str)
    parser.add_argument("db_name", type=str)
    parser.add_argument("schema_name", type=str)
    args = parser.parse_args()
    print(args)

    # find src root path
    src_root = os.path.dirname(os.path.abspath(__file__))
    # get configs from ingest_config.json
    config = _get_config(src_root + '/src/config/ingest_config.json')
    print(config["HOST"])
    engine = _get_engine(config["HOST"], args.db_name)

    try:
        _import_sql_folder(folder_path=args.folder_path, engine=engine, target_schema=args.schema_name)
        print("Ingest successfully!")
    except Exception as e:
        print(f"Failed to connect with database: {e}")


if __name__ == '__main__':
    sys.exit(main())
