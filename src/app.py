"""
The module is responsible for
the main program window
© Andboogl, 2024
"""


from json.decoder import JSONDecodeError
from PyQt6.QtWidgets import QMainWindow
from design import MainWindowDesign
from message import MessageShowing
from settings import Settings
from const import SETTINGS_FILE_PATH
import database
import menu


class MainWindow(QMainWindow):
    """Main program window"""
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Upload design
        self.__design = MainWindowDesign()
        self.__design.setupUi(self)

        self.__settings = Settings()
        self.__database = database.Database()
        self.__msg_box_showing = MessageShowing(self)
        self.switching_menu = menu.SwitchingMenu(self.__design)
        self.__calendar_menu = menu.CalendarMenu(
            self,
            self.__design, self.__database,
            self.__msg_box_showing)

        self.__settings_menu = menu.SettingsMenu(
            self, self.__design,
            self.__settings,
            self.__msg_box_showing)

        # Menu switching
        self.__design.home.clicked.connect(self.switching_menu.main_menu)
        self.__design.calendar.clicked.connect(self.switching_menu.calendar_menu)
        self.__design.settings.clicked.connect(self.switching_menu.settings_menu)

        self.switching_menu.main_menu()

        # Button pressing
        self.__design.source_code.clicked.connect(lambda: self.__design.tabShow.setCurrentIndex(3))
        self.__design.back.clicked.connect(lambda: self.__design.tabShow.setCurrentIndex(2))
        self.__design.calendar_2.clicked.connect(self.switching_menu.calendar_menu)
        self.__design.settings_2.clicked.connect(self.switching_menu.settings_menu)
        self.__design.create_new_day.clicked.connect(self.__calendar_menu.create_new_day)
        self.__design.delete_day.clicked.connect(self.__calendar_menu.delete_day)
        self.__design.chose.clicked.connect(self.__settings_menu.chose_database_folder_path)
        self.__design.save_settings.clicked.connect(self.__settings_menu.save_settings)
        self.__design.open_day.clicked.connect(self.__calendar_menu.open_day)
        self.__design.rename_day.clicked.connect(self.__calendar_menu.rename_day)
        self.__design.days.itemSelectionChanged.connect(self.__calendar_menu.day_selected)

        self.__calendar_menu.load_days()

        # Loading settings
        try:
            database_path = self.__settings.get_settings()
            self.__design.database_path.setText(database_path['database_folder_path'])

        except JSONDecodeError:
            self.__msg_box_showing.show(
                'Виникла помилка під час завантаження ваших налаштуваннь.'\
                f' Оновіть їх чи видаліть файл за шляхом {SETTINGS_FILE_PATH}')
