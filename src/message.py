"""
Module for displaying messages
© Andboogl, 2024
"""


from PyQt6.QtWidgets import QMessageBox


class MessageShowing:
    """Class for displaying messages"""
    def __init__(self, main_window) -> None:
        self.__main_window = main_window

    def show(self, text) -> None:
        """Show QMessageBox"""
        msg_box = QMessageBox(self.__main_window)
        msg_box.setText(text)
        msg_box.exec()
