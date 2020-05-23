#########################################################################
# The class to implement all functions for the RF-AMP-RPIInterface 
#
# Created by Roger Kalt <roger.kalt@gmail.com>, 10.02.2020
#########################################################################

from argparse import ArgumentParser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from UI_640x480_ui import *
from Definitions import *
from socket_server import *

from socket import *

# =================================
# define the class based on the generated one from .ui file
# =================================
class Ui_MainWindow_Imp(Ui_MainWindow):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # class variables
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    sum_fault = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # create the object
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        # init the father
        Ui_MainWindow.__init__(self)

        # this will hide the title bar
        #super.MainMindowsetWindowFlag(Qt.FramelessWindowHint)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # init the objects created in the _ui class
    # this should be called after "setupUi" function
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def initGUIObjects(self):
        self.label_Version.setText("Version: " + VERSION_TAG)
        self.label_Status.setText(control_type + " RF Amp Control for " + connect_host)
        self.label_Amplifier_Hostname.setText("Amplifier hostname: " + connect_host + " | " + gethostbyname(connect_host) )

        self.frame_SumFault_statecontrol.setVisible(False)
        self.label_FaultDetected.setVisible(False)
        self.pushButton_PTT.setVisible(False)

        self.comboBox_BandSelect.addItem("Band 1")
        self.comboBox_BandSelect.addItem("Band 2")
        self.comboBox_BandSelect.addItem("Band 3")
        self.comboBox_BandSelect.addItem("Band 4")
        self.comboBox_BandSelect.addItem("Band 5")
        self.comboBox_BandSelect.addItem("Band 6")

        self.comboBox_AntennaSelect.addItem("Antenna 1")
        self.comboBox_AntennaSelect.addItem("Antenna 2")
        self.comboBox_AntennaSelect.addItem("Antenna 3")
        self.comboBox_AntennaSelect.addItem("Antenna 4")

        # initialize to defaults
        self.handler_comboBox_AntennaSelect()
        self.handler_comboBox_BandSelect()

        print("init done")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # init the signals and slots
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    def initSignalHandlers(self, cwmode):
        # get commands clicked
        self.pushButton_OP.clicked.connect(self.handler_pushButton_OP)

        # PTT needs the mouse press and release events to select the correct command
        if cwmode == True:
            #print("CW mode is activated. cwmode=" + str(cwmode))
            self.pushButton_PTT.clicked.connect(self.handler_pushButton_PTT_cw_mode)
        else:
            #print("Normal PTT mode is activated, cwmode=" + str(cwmode))
            self.pushButton_PTT.mousePressEvent = self.handler_pushButton_PTT_press
            self.pushButton_PTT.mouseReleaseEvent = self.handler_pushButton_PTT_release


        self.pushButton_Reset.clicked.connect(self.handler_pushButton_Reset)

        # event on fault state changed
        #self.frame_SumFault_AmpController.paintEvent = self.handler_fault_state_changed

        self.pushButton_emulateFault.clicked.connect(self.handler_emulateFault)

        self.comboBox_AntennaSelect.currentIndexChanged.connect(self.handler_comboBox_AntennaSelect)
        self.comboBox_BandSelect.currentIndexChanged.connect(self.handler_comboBox_BandSelect)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # event handlers
    # ~~~~~~~~~~~~~~~~~~~~~~~~~

    # ---------------------
    # Fault
    # ---------------------
    def handler_emulateFault(self):
        print("fault triggered")
        self.sum_fault = 1
        self.frame_SumFault_header.setStyleSheet("background-color: red")
        self.frame_SumFault_statecontrol.setStyleSheet("background-color: red")
        self.frame_SumFault_statecontrol.setVisible(True)
        self.label_FaultDetected.setVisible(True)
        self.pushButton_PTT.setVisible(False)

    def handler_fault_state_changed(self, event):
        if self.sum_fault == 1:
            self.pushButton_PTT.setVisible(False)
        else:
            self.pushButton_PTT.setVisible(True)

    # ---------------------
    # Operation state button
    # ---------------------
    def handler_pushButton_OP(self):
        if self.pushButton_OP.isChecked():
            self.pushButton_OP.setText('OP')
            self.pushButton_PTT.setVisible(True)
            self.comboBox_BandSelect.setEnabled(False)
            self.comboBox_AntennaSelect.setEnabled(False)
        else:
            self.pushButton_OP.setText('STBY')
            self.pushButton_PTT.setVisible(False)
            self.comboBox_BandSelect.setEnabled(True)
            self.comboBox_AntennaSelect.setEnabled(True)

    # ---------------------
    # PTT button
    # ---------------------
    def handler_pushButton_PTT_cw_mode(self):
        if self.pushButton_PTT.isChecked():
            self.pushButton_PTT.setText('ON-AIR')
        else:
            self.pushButton_PTT.setText('PTT')

    def handler_pushButton_PTT_press(self, event):
        self.pushButton_PTT.setText('ON-AIR')

    def handler_pushButton_PTT_release(self, event):
        self.pushButton_PTT.setText('PTT')

    # ---------------------
    # Reset button pressed
    # ---------------------
    def handler_pushButton_Reset(self):
        print("Reset clicked")
        self.sum_fault = 0
        self.frame_SumFault_header.setStyleSheet("background-color: ")
        self.frame_SumFault_statecontrol.setStyleSheet("background-color:")
        self.frame_SumFault_statecontrol.setVisible(False)
        self.label_FaultDetected.setVisible(False)
        self.handler_pushButton_OP()

    # ---------------------
    # Band select changed
    # ---------------------
    def handler_comboBox_BandSelect(self):
        print("Band changed to " + str(self.comboBox_BandSelect.currentText()))

    # ---------------------
    # Antenna select changed
    # ---------------------
    def handler_comboBox_AntennaSelect(self):
        print("Antenna changed to " + str(self.comboBox_AntennaSelect.currentText() ))

# =================================
# startup the main window
# =================================
if __name__ == "__main__":
    import sys
    import socket

    # parse command line argument
    parser = ArgumentParser()
    parser.add_argument("--connect", dest="connect_host",
                        help="UI can connect to localhost (default) or a remote host. The localhost default is typically the UI which is physically connected via GPIO to the amplifier controller.",
                        default="localhost",
                        required=False)
    parser.add_argument("--cwmode", dest="cwmode",
                        help="If the amplifier shall operate in CW mode, then use this optional argument.",
                        default="False",
                        required=False,
                        action='store_true')
    parser.set_defaults(cwmode=False)
    args = parser.parse_args()

    if args.connect_host == "localhost":
        connect_host = socket.gethostname()
        control_type = "LOCAL"

        # if local then start the socket server
        #server = RFAMPServer()


    else:
        connect_host = args.connect_host
        control_type = "REMOTE"

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow_Imp()
    ui.setupUi(MainWindow)  # in the auto-generated class
    ui.initGUIObjects()
    ui.initSignalHandlers(args.cwmode)

    MainWindow.show()

    sys.exit(app.exec_())

    server.shutdown()
    server.server_close()