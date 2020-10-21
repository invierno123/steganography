from 视频处理 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 800)
        MainWindow.setStyleSheet("background-image:url(\"D:350.jfif\")")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 991, 91))
        self.label.setStyleSheet("font: 75 22pt \"Arial\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 210, 431, 100))
        self.pushButton.setStyleSheet("color:rgb(0, 0, 0);background-image:url(\"D:18.jpg\");\n"
"font: 75 20pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 431, 100))
        self.pushButton_2.setStyleSheet("color:rgb(0, 0, 0);background-image:url(\"D:18.jpg\");\n"
"font: 75 20pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 520, 431, 100))
        self.pushButton_3.setStyleSheet("color:rgb(0, 0, 0);background-image:url(\"D:18.jpg\");\n"
"font: 75 20pt \"Arial\";")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 30))
        self.menubar.setObjectName("menubar")
        self.menuxuanxiang = QtWidgets.QMenu(self.menubar)
        self.menuxuanxiang.setObjectName("menuxuanxiang")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuxuanxiang.addAction(self.actionabout)
        self.menuxuanxiang.addAction(self.actionhelp)
        self.menuxuanxiang.addAction(self.actionexit)
        self.menubar.addAction(self.menuxuanxiang.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                          welcome to use!"))
        self.pushButton.setText(_translate("MainWindow", "图片处理"))
        self.pushButton_2.setText(_translate("MainWindow", "音频处理"))
        self.pushButton_3.setText(_translate("MainWindow", "视频处理"))
        self.menuxuanxiang.setTitle(_translate("MainWindow", "选项"))
        self.actionabout.setText(_translate("MainWindow", "注销"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
        self.actionexit.setText(_translate("MainWindow", "退出"))