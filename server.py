# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import sys, requests

gol_cookies = ''


class Ui_MainWindow(object):
    def __init__(self):
        self.jxy_get_header = {
            "Accept": "text/html, application/xhtml+xml, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "Connection": "Keep-Alive",
            "Host": "www.juxiangyou.com",
            "Referer": "http://www.juxiangyou.com/",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64;Trident/5.0)"
        }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 331, 401))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-image: url(:/newPrefix/images/juxiangyou.png);")
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.jxy_lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.jxy_lineEdit_name.setObjectName("jxy_lineEdit_name")
        self.gridLayout.addWidget(self.jxy_lineEdit_name, 0, 1, 1, 1)
        self.jxy_pb = QtWidgets.QPushButton(self.widget)
        self.jxy_pb.setObjectName("jxy_pb")
        self.gridLayout.addWidget(self.jxy_pb, 0, 2, 3, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.jxy_lineEdit_pwd = QtWidgets.QLineEdit(self.widget)
        self.jxy_lineEdit_pwd.setObjectName("jxy_lineEdit_pwd")
        self.gridLayout.addWidget(self.jxy_lineEdit_pwd, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.jxy_dt_list = QtWidgets.QListWidget(self.widget)
        self.jxy_dt_list.setObjectName("jxy_dt_list")
        self.gridLayout.addWidget(self.jxy_dt_list, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-image: url(:/newPrefix/images/lezhuan.png);")
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lz_lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lz_lineEdit_name.setObjectName("lz_lineEdit_name")
        self.gridLayout_2.addWidget(self.lz_lineEdit_name, 0, 1, 1, 1)
        self.lz_pB = QtWidgets.QPushButton(self.layoutWidget)
        self.lz_pB.setObjectName("lz_pB")
        self.gridLayout_2.addWidget(self.lz_pB, 0, 2, 3, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lz_lineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.lz_lineEdit_pwd.setObjectName("lz_lineEdit_pwd")
        self.gridLayout_2.addWidget(self.lz_lineEdit_pwd, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.lz_dt_list = QtWidgets.QListWidget(self.layoutWidget)
        self.lz_dt_list.setObjectName("lz_dt_list")
        self.gridLayout_2.addWidget(self.lz_dt_list, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("background-image: url(:/newPrefix/images/youzhuan.png);")
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.yz_lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.yz_lineEdit_name.setObjectName("yz_lineEdit_name")
        self.gridLayout_3.addWidget(self.yz_lineEdit_name, 0, 1, 1, 1)
        self.yz_pB = QtWidgets.QPushButton(self.layoutWidget_2)
        self.yz_pB.setObjectName("yz_pB")
        self.gridLayout_3.addWidget(self.yz_pB, 0, 2, 3, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.yz_lineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.yz_lineEdit_pwd.setObjectName("yz_lineEdit_pwd")
        self.gridLayout_3.addWidget(self.yz_lineEdit_pwd, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_3.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.yz_dt_list = QtWidgets.QListWidget(self.layoutWidget_2)
        self.yz_dt_list.setObjectName("yz_dt_list")
        self.gridLayout_3.addWidget(self.yz_dt_list, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("background-image: url(:/newPrefix/images/ttz.png);")
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.ttz_lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.ttz_lineEdit_name.setObjectName("ttz_lineEdit_name")
        self.gridLayout_4.addWidget(self.ttz_lineEdit_name, 0, 1, 1, 1)
        self.ttz_pB = QtWidgets.QPushButton(self.layoutWidget_3)
        self.ttz_pB.setObjectName("ttz_pB")
        self.gridLayout_4.addWidget(self.ttz_pB, 0, 2, 3, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.ttz_lineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.ttz_lineEdit_pwd.setObjectName("ttz_lineEdit_pwd")
        self.gridLayout_4.addWidget(self.ttz_lineEdit_pwd, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.ttz_dt_list = QtWidgets.QListWidget(self.layoutWidget_3)
        self.ttz_dt_list.setObjectName("ttz_dt_list")
        self.gridLayout_4.addWidget(self.ttz_dt_list, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setStyleSheet("background-image: url(:/newPrefix/images/pceggs.png);")
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.eg_lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.eg_lineEdit_name.setObjectName("eg_lineEdit_name")
        self.gridLayout_5.addWidget(self.eg_lineEdit_name, 0, 1, 1, 1)
        self.eg_pB = QtWidgets.QPushButton(self.layoutWidget_4)
        self.eg_pB.setObjectName("eg_pB")
        self.gridLayout_5.addWidget(self.eg_pB, 0, 2, 3, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.eg_lineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.eg_lineEdit_pwd.setObjectName("eg_lineEdit_pwd")
        self.gridLayout_5.addWidget(self.eg_lineEdit_pwd, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_5.addWidget(self.lineEdit_15, 2, 1, 1, 1)
        self.eg_dt_list = QtWidgets.QListWidget(self.layoutWidget_4)
        self.eg_dt_list.setObjectName("eg_dt_list")
        self.gridLayout_5.addWidget(self.eg_dt_list, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_5, "")
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.jxy_pb.setText(_translate("MainWindow", "登录"))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "聚享游"))
        self.label_4.setText(_translate("MainWindow", "用户名："))
        self.lz_pB.setText(_translate("MainWindow", "登录"))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "乐赚"))
        self.label_7.setText(_translate("MainWindow", "用户名："))
        self.yz_pB.setText(_translate("MainWindow", "登录"))
        self.label_8.setText(_translate("MainWindow", "密码："))
        self.label_9.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "有赚"))
        self.label_10.setText(_translate("MainWindow", "用户名："))
        self.ttz_pB.setText(_translate("MainWindow", "登录"))
        self.label_11.setText(_translate("MainWindow", "密码："))
        self.label_12.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "天天钻"))
        self.label_13.setText(_translate("MainWindow", "用户名："))
        self.eg_pB.setText(_translate("MainWindow", "登录"))
        self.label_14.setText(_translate("MainWindow", "密码："))
        self.label_15.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Pceggs"))


class submit(QThread):
    def __init__(self):
        # 创建一个网站表示，根据不同的表示多线程运行的代码不同
        self.siteflag = 0
        pass

    def jxy_submit(self):
        self.siteflag = 1
        pass

    def lezhuan_submit(self):
        self.siteflag = 2
        pass

    def youzhuan_submit(self):
        self.siteflag = 3
        pass

    def ttz_submit(self):
        self.siteflag = 4
        pass

    def pceggs_submit(self):
        pass

    def run(self):
        global gol_cookies
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
