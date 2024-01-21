"""
Settings menu
© Andboogl, 2024
"""


import os
import shutil
from PyQt6.QtWidgets import QFileDialog


class SettingsMenu:
    """Settings menu"""
    def __init__(self, main_window, design, settings, msg_box_showing) -> None:
        self.__main_window = main_window
        self.__design = design
        self.__settings = settings
        self.__msg_box_showing = msg_box_showing

    def chose_database_folder_path(self) -> None:
        """Choose a folder to save the database"""
        folder: str = QFileDialog.getExistingDirectory(self.__main_window, 'Виберіть папку', '/')

        # If the user did not press the Cancel button
        if folder:
            self.__design.database_path.setText(folder)

    def save_settings(self) -> None:
        """Save user settings"""
        database_folder_path: str = self.__design.database_path.text()

        if database_folder_path.strip():
            if self.__settings.get_settings()['database_folder_path'] != database_folder_path:
                # Copying the database to a folder selected by the user
                try:
                    src: str = os.path.join(
                        self.__settings.get_settings()['database_folder_path'],
                        'schedule.db')

                    dst: str = os.path.join(database_folder_path, 'schedule.db')

                    try:
                        if os.path.exists(dst):
                            os.remove(dst)

                    except PermissionError:
                        self.__msg_box_showing.show(
                            f'Для копіювання бази данних видаліть файл за шляхом {dst}')

                    else:
                        shutil.copy(src, dst)

                        # Saving new database path
                        self.__settings.load_settings({'database_folder_path': database_folder_path})

                        self.__msg_box_showing.show(
                            'Для того щоб ви могли знову працювати '\
                            'з базою данних, треба перезавантажити программу')
                        exit(0)

                except Exception:
                    self.__msg_box_showing.show(
                        'Виникла помилка під час копіювання бази данних. '\
                        'Можливо, вибрана директорія є системною')

            else:
                self.__msg_box_showing.show('Ця папка вже є папкою бази данних')


        else:
            self.__msg_box_showing.show('Виберіть папку')
