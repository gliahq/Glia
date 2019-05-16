import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from glia.windows.main import MainWindow


def start(**kwargs):
    app = QApplication(sys.argv)

    # Load Theme
    with open(Path("../resources/themes/dracula.qss")) as qss:
        app_style = qss.read()
    app.setStyleSheet(app_style)

    # Create Main Window
    window = MainWindow()
    window.showMaximized()

    # Run & Exit
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
