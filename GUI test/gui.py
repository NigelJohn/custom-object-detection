from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 532)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Horizontal layout 1 which contains video label
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget) 
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Label where video will display 
        self.VideoFeedLabel = QtWidgets.QLabel(self.horizontalLayoutWidget) 
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.horizontalLayout.addWidget(self.VideoFeedLabel)

        #horizontal layout 2 which contains both buttons
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 390, 751, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Save button (not connected to any function for now)
        self.SaveBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SaveBtn.setObjectName("SaveBtn")
        self.horizontalLayout_2.addWidget(self.SaveBtn)

        #Cancel button stops the video (connected to cancelfeed function)
        self.CancelBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.CancelFeed)
        self.horizontalLayout_2.addWidget(self.CancelBtn)
        
        #Function which converts video input into pqt5 format to display
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.CancelBtn.setText(_translate("MainWindow", "Cancel"))

    def ImageUpdateSlot(self, Image):
        self.VideoFeedLabel.setPixmap(QPixmap.fromImage(Image))
    
    def CancelFeed(self):
        self.Worker1.stop()

    #def SaveFeed(self):
        
#video capturing function
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(751, 371, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
