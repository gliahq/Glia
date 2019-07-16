import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from glia.definitions import ROOT_DIR
from glia.utils import get_theme_contents
from glia.windows.main import MainWindow


def start(**kwargs):
    app = QApplication(sys.argv)

    # Load Theme
    app.setStyleSheet(get_theme_contents("dracula", "dracula.qss"))

    # Create Main Window
    window = MainWindow()
    window.showMaximized()

    # Run & Exit
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
