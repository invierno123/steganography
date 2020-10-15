from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from 主界面 import *
from 信息隐藏工具 import *
from 隐藏加密 import *
from 隐藏解密 import *
from 视频处理 import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QThread
from PIL import Image

"""
取得一个 PIL 图像并且更改所有值为偶数（使最低有效位为 0）
"""



################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow, Ui_MainWindow,QWidget):
    windowList = []
    sig_1 = pyqtSignal()
    def __init__(self, parent=None,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionabout.triggered.connect(self.on_printAction1_triggered)
        # 创建动作 退出
        self.actionexit.triggered.connect(self.on_printAction2_triggered)


    # 动作一：注销
    def on_printAction1_triggered(self):
        self.close()
        dialog = Dialog(mode=1)
        if  dialog.exec_()==QDialog.Accepted:
            the_window = MainWindow()
            self.windowList.append(the_window)    #这句一定要写，不然无法重新登录
            the_window.show()

    # 动作二：退出
    def on_printAction2_triggered(self):
        self.close()

    # 关闭界面触发事件
    def closeEvent(self, event):
        print(999999999)
        pass

################################################
#######对话框
################################################

class Dialog(QDialog,Ui_Dialog):

    def __init__(self, parent=None,mode=0,*args,**kwargs):

        super().__init__(*args, **kwargs)
        self.mode = mode
        ###### 绑定按钮事件
        ####初始化登录信息

        self.setupUi(self)
        ###### 绑定按钮事件
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)


    ####自动登录
    # 自动登录
    def goto_autologin(self):
        if self.checkBox_autologin.isChecked()==True and self.mode == 0 :
           self.on_pushButton_clicked()
    def on_pushButton_clicked(self):
        # 账号判断
        if self.lineEdit.text() == "":
            return

        # 密码判断
        if self.lineEdit_2.text() == "":
            return

        ####### 保存登录信息

        # 通过验证，关闭对话框并返回1
        self.accept()

    # 保存登录信息

    # 初始化登录信息


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog(mode=0)
    if  dialog.exec_()==QDialog.Accepted:
        the_window = MainWindow()
        child1 = QWidget()
        child2 = QMainWindow()
        child3 = QWidget()
        child1_ui = Ui_Form1()
        child1_ui.setupUi(child1)
        child2_ui = Ui_Form2()
        child2_ui.setupUi(child2)
        child3_ui = Ui_Form3()
        child3_ui.setupUi(child3)
        # 按钮绑定事件
        btn1 = the_window.pushButton
        btn1.clicked.connect(child1.show)
        btn2 = the_window.pushButton_2
        btn2.clicked.connect(child2.show)
        btn3 = the_window.pushButton_3
        btn3.clicked.connect(child3.show)

        the_window.show()
        sys.exit(app.exec_())


