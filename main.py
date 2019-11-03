import sys
import signal
from config import *
from window import Window
from PyQt5.QtWidgets import QApplication


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
