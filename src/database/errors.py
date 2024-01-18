"""
Database errors
© Andboogl, 2024
"""


class DayNotFoundError(Exception):
    """
    Error when the day could
    not be found in the database
    """


class DayExistsError(Exception):
    """
    Error when a day with the
    same name already exists
    """


class TaskNotFoundError(Exception):
    """
    Error when the task of
    the day is not found
    """


class TaskExistsError(Exception):
    """
    Error when a task with the
    same name already exists
    """
