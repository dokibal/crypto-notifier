from PyQt5 import QtWidgets
from ui.mainwindow import Ui_CryptoWindow
from database.dbhandler import DbHandler
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ApplicationWindow, self).__init__()

        self.db_handler = DbHandler()
        self.db_handler.connect()

        self.ui = Ui_CryptoWindow()
        self.ui.setupUi(self)
        
        sc = self.ui.graph
        prices = self.get_points()

        print(prices)
        sc.axes.plot(prices[0],prices[1])
        self.setCentralWidget(sc)
        self.show()

    def get_points(self):
        prices = self.db_handler.get_all_prices()
        return prices

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()