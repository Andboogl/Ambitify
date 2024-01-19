"""
Calendar menu
© Andboogl, 2024
"""


from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QFont
from day_edit_window import DayEditWindow
import database


class CalendarMenu:
    """Calendar menu"""
    def __init__(self, main_window, design, db, msg_box_showing):
        self.__design = design
        self.__database = db
        self.__msg_box_showing = msg_box_showing
        self.__main_window = main_window

    def day_selected(self) -> None:
        """Day selection handling"""
        selected_days = self.__design.days.selectedItems()

        if selected_days:
            selected_day = selected_days[0].text()

            self.__design.rename_day_name.setText(selected_day)
            self.__design.new_day_name.setText(selected_day)

    def delete_day(self) -> None:
        """Delete selected day"""
        selected_days = self.__design.days.selectedItems()

        if selected_days:
            selected_day = selected_days[0].text()
            self.__database.delete_day(selected_day)
            self.load_days()

    def rename_day(self) -> None:
        """Rename selected day"""
        selected_days = self.__design.days.selectedItems()
        new_name = self.__design.rename_day_name.text()

        if selected_days:
            selected_day = selected_days[0].text()

            if new_name.strip():
                try:
                    self.__database.rename_day(selected_day, new_name)
                    self.load_days()

                except database.errors.DayExistsError:
                    self.__msg_box_showing.show('День с таким імʼям вже існує')

            else:
                self.__msg_box_showing.show('Введіть нову назву для дня')

    def create_new_day(self) -> None:
        """Add new day to database"""
        day_name = self.__design.new_day_name.text()

        if day_name.strip():
            try:
                self.__database.add_new_day(day_name)
                self.load_days()

            except database.errors.DayExistsError:
                self.__msg_box_showing.show('День с таким імʼям вже існує')

        else:
            self.__msg_box_showing.show('Введіть імʼя дня для його створення')

    def open_day(self) -> None:
        """Open the selected day"""
        selected_days = self.__design.days.selectedItems()

        if selected_days:
            selected_day = selected_days[0].text()
            self.__day_edit_window = DayEditWindow(self.__main_window, selected_day)
            self.__day_edit_window.show()

    def load_days(self) -> None:
        """Load data from the database"""
        self.__design.days.clear()
        days = self.__database.get_days()

        for day in days:
            item = QListWidgetItem()
            item.setText(day[0])

            font = QFont()
            font.setBold(True)
            font.setPointSize(30)

            item.setFont(font)
            self.__design.days.addItem(item)
