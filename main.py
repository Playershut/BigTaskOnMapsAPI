import sys

from libr.geocoder import get_coordinates
from libr.mapapi_PG import get_map

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

from UI.map_ui import Ui_MainWindow


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ll_spn = 'll=51.768156,55.0969797&spn=1.5,1.5'
        self.initUi()

    def initUi(self):
        super().setupUi(self)
        self.map_lbl.setPixmap(QPixmap(get_map(self.ll_spn)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    map_win = Map()
    map_win.show()
    sys.exit(app.exec_())
