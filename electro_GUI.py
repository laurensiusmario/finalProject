from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import cv2
import sys
#import RPi.GPIO as GPIO
import time

DURATION_INT = 0

LED = 16
relay_pin = 11

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED, GPIO.OUT)
#GPIO.setup(relay_pin, GPIO.OUT)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.spinBox_time = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_time.setGeometry(QtCore.QRect(20, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinBox_time.setFont(font)
        self.spinBox_time.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.spinBox_time.setObjectName("spinBox_time")
        
        self.button_electro_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_electro_start.setGeometry(QtCore.QRect(20, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_electro_start.setFont(font)
        self.button_electro_start.setObjectName("button_electro_start")
        
        self.label_duration = QtWidgets.QLabel(self.centralwidget)
        self.label_duration.setGeometry(QtCore.QRect(20, 100, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_duration.setFont(font)
        self.label_duration.setObjectName("label_duration")
        self.label_electro = QtWidgets.QLabel(self.centralwidget)
        self.label_electro.setGeometry(QtCore.QRect(20, 20, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_electro.setFont(font)
        self.label_electro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_electro.setObjectName("label_electro")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 250, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        
        self.lcdNumber_countdown = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_countdown.setGeometry(QtCore.QRect(20, 190, 111, 41))
        self.lcdNumber_countdown.setObjectName("lcdNumber_countdown")
        
        self.label_countdown = QtWidgets.QLabel(self.centralwidget)
        self.label_countdown.setGeometry(QtCore.QRect(20, 170, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_countdown.setFont(font)
        self.label_countdown.setObjectName("label_countdown")
        
        self.button_image_on = QtWidgets.QPushButton(self.centralwidget)
        self.button_image_on.setGeometry(QtCore.QRect(20, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_image_on.setFont(font)
        self.button_image_on.setObjectName("button_image_on")
        
        self.button_image_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_image_new.setGeometry(QtCore.QRect(20, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_image_new.setFont(font)
        self.button_image_new.setObjectName("button_image_new")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 10, 20, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label_imageresult = QtWidgets.QLabel(self.centralwidget)
        self.label_imageresult.setGeometry(QtCore.QRect(150, 10, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_imageresult.setFont(font)
        self.label_imageresult.setObjectName("label_imageresult")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 20, 421))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 420, 131, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        
        self.frame_img = QtWidgets.QFrame(self.centralwidget)
        self.frame_img.setGeometry(QtCore.QRect(150, 40, 640, 440))
        self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img.setObjectName("frame_img")
        
        self.label_img = QtWidgets.QLabel(self.frame_img)
        self.label_img.setGeometry(QtCore.QRect(10, 50, 640, 295))
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        
        self.label_led = QtWidgets.QLabel(self.centralwidget)
        self.label_led.setGeometry(QtCore.QRect(20, 350, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_led.setFont(font)
        self.label_led.setAlignment(QtCore.Qt.AlignCenter)
        self.label_led.setObjectName("label_led")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connect LED to button
        #self.button_image_on.clicked.connect(self.LED) 

        #set camera
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.button_image_new.clicked.connect(self.controlTimer) 

        #set countdown timer
        self.timer_start()
        self.button_electro_start.clicked.connect(self.getDuration)       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spinBox_time.setStatusTip(_translate("MainWindow", "Choose electrophoresis duration"))
        self.button_electro_start.setStatusTip(_translate("MainWindow", "Click to start electrophoresis process"))
        self.button_electro_start.setText(_translate("MainWindow", "Start"))
        self.label_duration.setText(_translate("MainWindow", "Duration"))
        self.label_electro.setText(_translate("MainWindow", "ELECTROPHORESIS"))
        self.label_image.setText(_translate("MainWindow", "IMAGE"))
        self.label_countdown.setText(_translate("MainWindow", "Countdown"))
        self.button_image_on.setStatusTip(_translate("MainWindow", "Click to turn blue LED on"))
        self.button_image_on.setText(_translate("MainWindow", "ON"))
        self.button_image_new.setStatusTip(_translate("MainWindow", "Click to show or capture image"))
        self.button_image_new.setText(_translate("MainWindow", "New Image"))
        self.label_imageresult.setText(_translate("MainWindow", "Image Result"))
        self.label_led.setText(_translate("MainWindow", "LED"))
        self.label_img.setText(_translate("MainWindow", " "))
        

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_img.setPixmap(QPixmap.fromImage(qImg))
        
    #LED
    #def LED(self):
    #    if GPIO.input(LED):
    #            GPIO.output(LED, False)
    #            self.button_image_on.setText("ON") 
    #    else:
    #            GPIO.output(LED, True)
    #            self.button_image_on.setText("OFF")
    

    #Relay
    #def Relay(self, time_input):
    #    if GPIO.input(relay_pin):
    #            if (time_input==0):
    #                    GPIO.output(relay_pin, False)
    #                    self.button_electro_start.setText("Start") 
    #    else:
    #            GPIO.output(relay_pin, True)
    #            self.button_electro_start.setText("Restart")

    # start/stop timer            
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.button_image_new.setText("Capture")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.button_image_new.setText("New Image")

    def timer_start(self):
        self.time_left_int = DURATION_INT
        self.prev_time = DURATION_INT

        #run timer for 1000ms, saat timeout, nilai time_left_in dikurang 1
        self.my_qtimer = QtCore.QTimer()
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        #self.update_gui()

    def timer_timeout(self):
        self.prev_time = self.time_left_int
        self.time_left_int -= 1

        self.update_gui()

    #update tulisan LCDnumer
    def update_gui(self):
        if (self.time_left_int > 0):
            menit = str(self.time_left_int // 60)
            if ((self.time_left_int % 60)<10):
                detik = "0" + str(self.time_left_int % 60)
            else :
                detik = str(self.time_left_int % 60)
            self.lcdNumber_countdown.display(menit + ":" + detik)
        else:
            self.lcdNumber_countdown.display("0:00")
            if (self.prev_time>0):
                    pass
                    #self.Relay(self.time_left_int)

    #get duration value from spinbox
    def getDuration(self):
        global value
        
        value = self.spinBox_time.value()
        self.time_left_int = value * 60
        if(value>0):
            pass
                #self.Relay(self.time_left_int)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #app.exec()
    #GPIO.output(relay_pin, False)
    sys.exit(app.exec_())
