"""
Database settings
© Andboogl, 2024
"""


import os
from settings import Settings


__settings = Settings()

DATA_TABLE_NAME = 'schedule'
DATABASE_FOLDER_PATH = __settings.get_settings()['database_folder_path']
DATABASE_FILE_PATH = os.path.join(DATABASE_FOLDER_PATH, 'schedule.db')
