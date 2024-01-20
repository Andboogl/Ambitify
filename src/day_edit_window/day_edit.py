"""
Day edit window
© Andboogl, 2024
"""


from PyQt6.QtWidgets import QMainWindow
from design import DayEditWindowDesign
from message import MessageShowing
import database
from .button_pressing import DayEditWindowButtonPressing


class DayEditWindow(QMainWindow):
    """Day edit window"""
    def __init__(self, main_window: QMainWindow, day: str) -> None:
        QMainWindow.__init__(self)

        self.__main_window = main_window
        self.__database = database.Database()
        self.__msg_box_showing = MessageShowing(self)
        self.__day = day

        # Upload design
        self.__design = DayEditWindowDesign()
        self.__design.setupUi(self)
        self.setWindowTitle(f'{self.__day} - Ambitify')

        # Buttons pressing
        self.__button_pressing = DayEditWindowButtonPressing(
            self.__design, self.__database,
            self.__day, self.__msg_box_showing,
            self.__main_window, self)

        self.__design.create_task.clicked.connect(self.__button_pressing.add_task)
        self.__design.back.clicked.connect(self.__button_pressing.back)
        self.__design.delete_task.clicked.connect(self.__button_pressing.delete_task)
        self.__design.change_task.clicked.connect(self.__button_pressing.change_task)
        self.__design.tasks.itemSelectionChanged.connect(self.task_selected)

    def task_selected(self) -> None:
        """Task selection handling"""
        selected_tasks = self.__design.tasks.selectedItems()

        if selected_tasks:
            selected_task = selected_tasks[0].text().split('\n')[0]

            task_from_database = self.__database.get_day(self.__day)[1][selected_task]

            comment = task_from_database['comment']
            progress = str(task_from_database['progress'])

            self.__design.task_edit_comment.setText(comment)
            self.__design.task_edit_progress.setText(progress)

            self.__design.create_task_comment.setText(comment)
            self.__design.create_task_name.setText(selected_task)
