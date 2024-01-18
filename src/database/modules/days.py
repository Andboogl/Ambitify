"""
Module for working with days
© Andboogl, 2024
"""


import pickle
from .getting_days import GettingDays
from .. import errors
from .. import config


class Days(GettingDays):
    """Class for working with days"""
    def add_new_day(self, day: str) -> None:
        """Add a new day to the database"""
        try:
            self.get_day(day)
            raise errors.DayExistsError(
                'A day with this name has already been created')

        except errors.DayNotFoundError:
            request = f'INSERT INTO {config.DATA_TABLE_NAME} values (?, ?)'
            data = (day, pickle.dumps({}))

            self.db.execute(request, data)
            self.db.commit()

    def rename_day(self, day: str, new_name: str) -> None:
        """Rename the day"""
        if self.get_day(day)[0].lower() == new_name.lower():
            raise errors.DayExistsError(
                'A day with this name has already been created')

        request = f'UPDATE {config.DATA_TABLE_NAME} SET day == ? WHERE day == ?'
        data = (new_name, day)
        self.db.execute(request, data)
        self.db.commit()

    def delete_day(self, day: str) -> None:
        """Delete day"""
        self.get_day(day)
        request = f'DELETE FROM {config.DATA_TABLE_NAME} WHERE day == ?'
        data = (day,)
        self.db.execute(request, data)
        self.db.commit()
