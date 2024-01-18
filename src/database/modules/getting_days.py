"""
A module for obtaining days from the database
© Andboogl, 2024
"""


import os
import pickle
from sqlite3 import connect
from .. import config
from ..errors import DayNotFoundError


class GettingDays:
    """
    Class module for obtaining days
    from the database
    """
    def __init__(self) -> None:
        """Initialization"""
        if not os.path.exists(config.DATABASE_FOLDER_PATH):
            os.mkdir(config.DATABASE_FOLDER_PATH)

        self.__db = connect(config.DATABASE_FILE_PATH)
        request = f'CREATE TABLE IF NOT EXISTS {config.DATA_TABLE_NAME}'\
            ' (day PRIMARY KEY, data)'
        self.__db.execute(request)

    @property
    def db(self) -> connect:
        """Get the database object"""
        return self.__db

    def get_day(self, day: str) -> tuple:
        """Get the day by its name"""
        request = f'SELECT * FROM {config.DATA_TABLE_NAME} WHERE day == ?'
        data = (day,)
        result = self.__db.execute(request, data).fetchone()

        if not result:
            raise DayNotFoundError('No day with this name found')

        result = list(result)
        result[1] = pickle.loads(result[1])
        return tuple(result)

    def get_days(self) -> tuple:
        """Get all days"""
        request = f'SELECT * FROM {config.DATA_TABLE_NAME}'
        result = self.__db.execute(request).fetchall()

        # Deciphering days
        result = tuple(map(
            lambda value: (
                value[0],
                pickle.loads(value[1])),
                result))

        return result
