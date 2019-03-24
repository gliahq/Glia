import sys

from PyQt5.QtWidgets import QApplication

from glia.windows.main import MainWindow


def start(**kwargs):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
