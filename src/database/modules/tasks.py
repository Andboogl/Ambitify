"""
Module for working with daily tasks
© Andboogl, 2024
"""


import pickle
from .getting_days import GettingDays
from .. import config
from ..errors import TaskNotFoundError, TaskExistsError


class Tasks(GettingDays):
    """Class for working with daily tasks"""
    def __load_tasks_to_day(self, day: str, data: dict) -> None:
        """Download daily tasks"""
        request = f'UPDATE {config.DATA_TABLE_NAME} SET data == ? WHERE day == ?'
        request_data = (pickle.dumps(data), day)
        self.db.execute(request, request_data)
        self.db.commit()

    def add_task_to_day(self, day: str, time: str, comment: str) -> None:
        """Add a daily task"""
        # Getting the day
        data = self.get_day(day)[1]

        if data.get(time, None):
            raise TaskExistsError('Task with this name already exists')

        # Loading tasks per day
        data[time] = {}
        data[time]['comment'] = comment
        data[time]['progress'] = 0

        self.__load_tasks_to_day(day, data)

    def change_task_to_day(
            self, day: str, time: str,
            new_time: str=None, new_comment: str=None, new_progress: int=None) -> None:
        """Change the task of the day"""
        # Loading tasks for the specified day
        data: dict = self.get_day(day)[1]

        # Checking for the existence of a job with the same name
        if not data.get(time, None):
            raise TaskNotFoundError('Task with this name not found')

        if new_time:
            if data.get(new_time, None):
                raise TaskExistsError('Task with this name already exists')

            old_data = data.copy()[time]
            data.pop(time)
            data[new_time] = {}
            data[new_time]['comment'] = old_data['comment']
            data[new_time]['progress'] = old_data['progress']
            time = new_time

        if new_comment:
            data[time]['comment'] = new_comment

        if new_progress or new_progress == 0:
            data[time]['progress'] = new_progress

        self.__load_tasks_to_day(day, data)

    def delete_task_from_day(self, day: str, time: str) -> None:
        """Delete task from day"""
        data: dict = self.get_day(day)[1]

        if not data.get(time, None):
            raise TaskNotFoundError('Task with this name not found')

        data.pop(time)
        self.__load_tasks_to_day(day, data)
