"""
Day edit window button pressing
© Andboogl, 2024
"""


from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QFont
import database


class DayEditWindowButtonPressing:
    """Day edit window button pressing"""
    def __init__(self, design, db, day,
                 msg_box_showing, main_window,
                 parent_window) -> None:
        self.__design = design
        self.__database = db
        self.__day = day
        self.__msg_box_showing = msg_box_showing
        self.__main_window = main_window
        self.__parent_window = parent_window
        self.load_tasks()

    def delete_task(self) -> None:
        """Delete task"""
        selected_tasks = self.__design.tasks.selectedItems()

        if selected_tasks:
            selected_task = selected_tasks[0].text().split('\n')[0]

            self.__database.delete_task_from_day(self.__day, selected_task)
            self.load_tasks()

    def change_task(self) -> None:
        """Change task"""
        selected_tasks = self.__design.tasks.selectedItems()

        if selected_tasks:
            selected_task = selected_tasks[0].text().split('\n')[0]

            edit_task_name = self.__design.task_edit_name.text()
            edit_task_comment = self.__design.task_edit_comment.text()
            edit_task_progress = self.__design.task_edit_progress.text()

            if edit_task_name.strip():
                if edit_task_name != selected_task:
                    try:
                        self.__database.change_task_to_day(
                            self.__day, selected_task, new_time=edit_task_name)
                        selected_task = edit_task_name

                    except database.errors.TaskExistsError:
                        self.__msg_box_showing.show('Завдання з таким імʼям вже існує')

            if edit_task_comment.strip():
                self.__database.change_task_to_day(
                    self.__day, selected_task, new_comment=edit_task_comment)

            if edit_task_progress.strip():
                try:
                    edit_task_progress = int(edit_task_progress)
                    self.__database.change_task_to_day(
                        self.__day, selected_task,
                        new_progress=edit_task_progress)

                except ValueError:
                    self.__msg_box_showing.show('Прогресс повинен бути цілим числом')

            self.load_tasks()

    def back(self) -> None:
        """Return to main window"""
        self.__parent_window.close()
        self.__main_window.show()

    def add_task(self) -> None:
        """Add task to day"""
        task_name = self.__design.create_task_name.text()
        task_comment = self.__design.create_task_comment.text()

        if task_name.strip():
            try:
                self.__database.add_task_to_day(self.__day, task_name, task_comment)
                self.load_tasks()

            except database.errors.TaskExistsError:
                self.__msg_box_showing.show('Задача с таким імʼям вже існує')

        else:
            self.__msg_box_showing.show('Введіть імʼя дня')

    def load_tasks(self) -> None:
        """Upload tasks to the task list"""
        self.__design.tasks.clear()
        tasks = self.__database.get_day(self.__day)[1]

        for task in tasks.keys():
            item = QListWidgetItem()
            font = QFont()
            font.setBold(True)
            font.setPointSize(25)
            item.setText(
                f'{task}\n{tasks[task]['comment']}\n'\
                f'Прогресс: {tasks[task]['progress']}%')
            item.setFont(font)
            self.__design.tasks.addItem(item)
