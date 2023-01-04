from PyQt5 import QtWidgets
from ui.mainwindow import Ui_CryptoWindow
from database.dbhandler import DbHandler
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ApplicationWindow, self).__init__()

        self.db_handler = DbHandler()

        self.ui = Ui_CryptoWindow()
        self.ui.setupUi(self)
        
        sc = self.ui.graph
        exchange_rates = self.get_points()
        sc.axes.plot(exchange_rates[0],exchange_rates[1])
        self.setCentralWidget(sc)
        self.show()

    def get_points(self):
        exchange_rates = self.db_handler.get_all_rates()
        return exchange_rates

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()