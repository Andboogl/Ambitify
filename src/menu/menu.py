"""
Module for menu switching
© Andboogl, 2024
"""


from . import menu_styles


class SwitchingMenu:
    """Class for menu switching"""
    def __init__(self, design) -> None:
        self.__main_window_design = design
        self.__current_button = self.__main_window_design.home

    def main_menu(self) -> None:
        """Go to main menu"""
        self.__current_button.setStyleSheet(menu_styles.NORMAL_BTN_STYLE)
        self.__main_window_design.tabShow.setCurrentIndex(0)
        self.__main_window_design.home.setStyleSheet(menu_styles.CHECKED_BTN_STYLE)
        self.__current_button = self.__main_window_design.home

    def calendar_menu(self) -> None:
        """Go to calendar menu"""
        self.__current_button.setStyleSheet(menu_styles.NORMAL_BTN_STYLE)
        self.__main_window_design.tabShow.setCurrentIndex(1)
        self.__main_window_design.calendar.setStyleSheet(menu_styles.CHECKED_BTN_STYLE)
        self.__current_button = self.__main_window_design.calendar

    def settings_menu(self) -> None:
        """Go to settings menu"""
        self.__current_button.setStyleSheet(menu_styles.NORMAL_BTN_STYLE)
        self.__main_window_design.tabShow.setCurrentIndex(2)
        self.__main_window_design.settings.setStyleSheet(menu_styles.CHECKED_BTN_STYLE)
        self.__current_button = self.__main_window_design.settings
