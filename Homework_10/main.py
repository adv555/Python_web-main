from mongo_client import db_connection
from view import main


if __name__ == '__main__':
    if db_connection:
        main()
    else:
        print('No connection to DB')
