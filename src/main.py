"""
Ambitify is a free and open-source planner
You can modify this code and add new features
© Andboogl, 2024
"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from app import MainWindow


def main() -> None:
    """The function runs the program"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
