#########################################################################
# The class to implement all functions for the RF-AMP-RPIInterface 
#
# Created by Roger Kalt <roger.kalt@gmail.com>, 10.02.2020
#########################################################################
import sys
import datetime
import time
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from UI_640x480_ui import *

# =================================
# define the class based on the generated one from .ui file
# =================================
class Ui_MainWindow_Imp(Ui_MainWindow):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # class variables
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # create the object
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        # init the father
        Ui_MainWindow.__init__(self)
        
        

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # init the objects created in the _ui class
    # this should be called after "setupUi" function
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def initGUIObjects(self):
        print("init done")
        
        
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # init the signals and slots
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def initSignalHandlers(self):
        # get commands clicked
        self.pushButton_RFon.clicked.connect                   (self.handler_pushButton_RFon)
        self.pushButton_Reset.clicked.connect                  (self.handler_pushButton_Reset)
 



    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # event handlers
    # ~~~~~~~~~~~~~~~~~~~~~~~~~

    
    # ---------------------
    # RF on button pressed
    # ---------------------
    def handler_pushButton_RFon(self):   
        if self.pushButton_RFon.isChecked():
            self.pushButton_RFon.setText('RF on')
            self.progressBar_RFout_FWD.setValue(2400)
            self.label_RFout_FWD.setText('2.4 kW')
        else:
            self.pushButton_RFon.setText('RF off')
            self.progressBar_RFout_FWD.setValue(0)
            self.label_RFout_FWD.setText('0.0 kW')
    
    # ---------------------
    # Reset button pressed
    # ---------------------
    def handler_pushButton_Reset(self):   
        print("Reset clicked")

# =================================
# startup the main window
# =================================
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    # create the main window and perform any necessary setup
    ui = Ui_MainWindow_Imp()
    ui.setupUi(MainWindow)                           # in the auto-generated class
    ui.initGUIObjects()                              # in the implementation
    ui.initSignalHandlers()    
    
    MainWindow.setWindowFlags(Qt.Window)
    MainWindow.show()
    sys.exit(app.exec_())

