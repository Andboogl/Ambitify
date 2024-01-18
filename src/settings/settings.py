"""
Module for working with program settings
© Andboogl, 2024
"""


import os
import json
from const import SETTINGS_FOLDER_PATH, SETTINGS_FILE_PATH


class Settings:
    """Class for working with program settings"""
    def __create_settings_folder(self) -> None:
        """Create a program settings folder"""
        if not os.path.exists(SETTINGS_FOLDER_PATH):
            os.makedirs(SETTINGS_FOLDER_PATH)

    def load_settings(self, settings: dict) -> None:
        """Load settings to file"""
        self.__create_settings_folder()
        open_format = 'w' if os.path.exists(SETTINGS_FILE_PATH) else 'a'

        with open(SETTINGS_FILE_PATH, open_format, encoding='utf-8') as file:
            json.dump(settings, file)

    def get_settings(self) -> dict:
        """Get settings from settings file"""
        if os.path.exists(SETTINGS_FILE_PATH):
            with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as file:
                return json.load(file)

        else:
            return {
                'database_folder_path': os.path.join(
                    os.path.expanduser('~'),
                    '.ambitify')}
