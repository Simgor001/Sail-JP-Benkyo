import sys
import core
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/logo/icon.png'))
    # if sys.platform.startswith('win'):
    #    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    #        "Sail Word Card")
    app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)
    benkyo = core.core()
    benkyo.show()

    sys.exit(app.exec())
