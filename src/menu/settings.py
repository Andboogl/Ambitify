"""
Settings menu
© Andboogl, 2024
"""


import os
import shutil
from PyQt6.QtWidgets import QFileDialog, QMessageBox


class SettingsMenu:
    """Settings menu"""
    def __init__(self, main_window, design, settings, msg_box_showing) -> None:
        self.__main_window = main_window
        self.__design = design
        self.__settings = settings
        self.__msg_box_showing = msg_box_showing

    def chose_database_folder_path(self) -> None:
        """Choose a folder to save the database"""
        folder = QFileDialog.getExistingDirectory(self.__main_window, 'Виберіть папку', '/')

        # If the user did not press the Cancel button
        if folder:
            self.__design.database_path.setText(folder)

    def save_settings(self) -> None:
        """Save user settings"""
        database_folder_path = self.__design.database_path.text()

        if database_folder_path:

            # Note: this string can be deleted
            self.__design.database_path.setText(database_folder_path)

            # Copying the database to a folder selected by the user
            try:
                dst = os.path.join(
                        database_folder_path,
                        'schedule.db')

                if os.path.exists(dst):
                    os.remove(dst)

                shutil.copy(
                    os.path.join(
                        self.__settings.get_settings()['database_folder_path'],
                        'schedule.db'), dst)

                self.__settings.load_settings(
                    {'database_folder_path': database_folder_path})


            except Exception as error:
                self.__msg_box_showing.show(
                    f'Виникла помилка {error} під час копіювання бази данних.'\
                    ' Можливо, вибрана директорія є системною.')

            self.__msg_box_showing.show(
                'Для того щоб ваші зміни у базу данних зберігалися потім,'\
                ' программа вимкнется. Знову відкрийте її після вимкленя')
            exit(0)

        else:
            self.__msg_box_showing.show('Виберіть папку')
