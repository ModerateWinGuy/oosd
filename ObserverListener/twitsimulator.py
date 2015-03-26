import sys
import twit
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "dashboard.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DashApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.twit1 = twit.Twit(self.list_main_twit)
        self.twit2 = twit.Twit(self.list_follower1)
        self.twit3 = twit.Twit(self.list_follower2)

        self.twit1.add_observer(self.twit2)
        self.twit1.add_observer(self.twit3)

        self.button_post.clicked.connect(self.post_status)

    def post_status(self):
        self.twit1.post_update(self.status_enter.text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())