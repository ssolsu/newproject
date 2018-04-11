# -*- coding: utf-8 -*-

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import requests, time, random, json, re
from bs4 import BeautifulSoup
import p_mysql, traceback, configparser

fpath = os.getcwd()
sys.path.append(fpath)
gol_cookies = ''
moni = 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 111))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(12, 24, 911, 73))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.user_info = QtWidgets.QLabel(self.widget)
        self.user_info.setObjectName("user_info")
        self.gridLayout.addWidget(self.user_info, 0, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout.addWidget(self.lineEdit_pwd, 0, 4, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 5, 1, 1)
        self.submit_Button = QtWidgets.QPushButton(self.widget)
        self.submit_Button.setObjectName("submit_Button")
        self.submit_Button.clicked.connect(self.down_submit_data)
        self.gridLayout.addWidget(self.submit_Button, 1, 1, 1, 5)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 380, 651, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 631, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(8)
        column_name = [
            '期数',
            '时间',
            '开奖号码',
            '开奖结果',
        ]
        self.tableWidget.setHorizontalHeaderLabels(column_name)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        # ----
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(670, 380, 281, 311))
        self.groupBox_5.setObjectName("groupBox_5")
        self.dt_listview = QtWidgets.QListWidget(self.groupBox_5)
        self.dt_listview.setObjectName('dt_listview')
        self.dt_listview.setGeometry((QtCore.QRect(20, 20, 241, 281)))

        # ---
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 941, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 911, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dq_qishu = QtWidgets.QLabel(self.layoutWidget)
        self.dq_qishu.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.dq_qishu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dq_qishu.setAlignment(QtCore.Qt.AlignCenter)
        self.dq_qishu.setObjectName("dq_qishu")
        self.gridLayout_2.addWidget(self.dq_qishu, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 2, 1, 1)
        self.dq_jine = QtWidgets.QLabel(self.layoutWidget)
        self.dq_jine.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.dq_jine.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dq_jine.setAlignment(QtCore.Qt.AlignCenter)
        self.dq_jine.setObjectName("dq_jine")
        self.gridLayout_2.addWidget(self.dq_jine, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.dq_jishu = QtWidgets.QLabel(self.layoutWidget)
        self.dq_jishu.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.dq_jishu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dq_jishu.setAlignment(QtCore.Qt.AlignCenter)
        self.dq_jishu.setObjectName("dq_jishu")
        self.gridLayout_2.addWidget(self.dq_jishu, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 6, 1, 1)
        self.lxcw = QtWidgets.QLabel(self.layoutWidget)
        self.lxcw.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.lxcw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lxcw.setAlignment(QtCore.Qt.AlignCenter)
        self.lxcw.setObjectName("lxcw")
        self.gridLayout_2.addWidget(self.lxcw, 0, 7, 1, 1)
        self.lable11 = QtWidgets.QLabel(self.layoutWidget)
        self.lable11.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.lable11.setTextFormat(QtCore.Qt.AutoText)
        self.lable11.setAlignment(QtCore.Qt.AlignCenter)
        self.lable11.setObjectName("lable11")
        self.gridLayout_2.addWidget(self.lable11, 1, 0, 1, 1)
        self.shouyi = QtWidgets.QLabel(self.layoutWidget)
        self.shouyi.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.shouyi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shouyi.setAlignment(QtCore.Qt.AlignCenter)
        self.shouyi.setObjectName("shouyi")
        self.gridLayout_2.addWidget(self.shouyi, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 1, 2, 1, 1)
        self.dq_moshi = QtWidgets.QLabel(self.layoutWidget)
        self.dq_moshi.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.dq_moshi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dq_moshi.setAlignment(QtCore.Qt.AlignCenter)
        self.dq_moshi.setObjectName("dq_moshi")
        self.gridLayout_2.addWidget(self.dq_moshi, 1, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 4, 1, 1)
        self.dq_daxiao = QtWidgets.QLabel(self.layoutWidget)
        self.dq_daxiao.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.dq_daxiao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dq_daxiao.setAlignment(QtCore.Qt.AlignCenter)
        self.dq_daxiao.setObjectName("dq_daxiao")
        self.gridLayout_2.addWidget(self.dq_daxiao, 1, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 6, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 250, 941, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 911, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 4, 1, 1)
        self.sq_jishu = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_jishu.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_jishu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_jishu.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_jishu.setObjectName("sq_jishu")
        self.gridLayout_3.addWidget(self.sq_jishu, 0, 5, 1, 1)
        self.sq_jine = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_jine.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_jine.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_jine.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_jine.setObjectName("sq_jine")
        self.gridLayout_3.addWidget(self.sq_jine, 0, 3, 1, 1)
        self.sq_qishu = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_qishu.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_qishu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_qishu.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_qishu.setObjectName("sq_qishu")
        self.gridLayout_3.addWidget(self.sq_qishu, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_26.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 0, 2, 1, 1)
        self.sq_jieguo = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_jieguo.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_jieguo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_jieguo.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_jieguo.setObjectName("sq_jieguo")
        self.gridLayout_3.addWidget(self.sq_jieguo, 1, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_28.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_28.setTextFormat(QtCore.Qt.AutoText)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 2, 1, 1)
        self.sq_daxiao = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_daxiao.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_daxiao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_daxiao.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_daxiao.setObjectName("sq_daxiao")
        self.gridLayout_3.addWidget(self.sq_daxiao, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_30.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_30.setTextFormat(QtCore.Qt.AutoText)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 4, 1, 1)
        self.sq_moshi = QtWidgets.QLabel(self.layoutWidget_2)
        self.sq_moshi.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.sq_moshi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sq_moshi.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_moshi.setObjectName("sq_moshi")
        self.gridLayout_3.addWidget(self.sq_moshi, 1, 5, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "登录区域"))
        self.label.setText(_translate("MainWindow", "Sumbit Name:"))
        self.label_2.setText(_translate("MainWindow", "PassWord:"))
        self.checkBox.setText(_translate("MainWindow", "真实"))
        self.submit_Button.setText(_translate("MainWindow", "Submit"))
        self.groupBox_2.setTitle(_translate("MainWindow", "表格显示"))
        self.groupBox_5.setTitle(_translate("MainWindow", "动态显示"))
        self.groupBox_3.setTitle(_translate("MainWindow", "当前期显示"))
        self.dq_qishu.setText(_translate("MainWindow", ""))
        self.label_22.setText(_translate("MainWindow", "投注金额："))
        self.dq_jine.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "投注计次："))
        self.dq_jishu.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "连续错误："))
        self.lxcw.setText(_translate("MainWindow", ""))
        self.lable11.setText(_translate("MainWindow", "当前收益："))
        self.shouyi.setText(_translate("MainWindow", ""))
        self.label_24.setText(_translate("MainWindow", "投注模式："))
        self.dq_moshi.setText(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", "投注大小："))
        self.dq_daxiao.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", "刷新倒计时："))
        self.label_3.setText(_translate("MainWindow", "当前期数："))
        self.groupBox_4.setTitle(_translate("MainWindow", "上期结果显示"))
        self.label_16.setText(_translate("MainWindow", "上期结果："))
        self.label_12.setText(_translate("MainWindow", "投注基数："))
        self.sq_jishu.setText(_translate("MainWindow", ""))
        self.sq_jine.setText(_translate("MainWindow", ""))
        self.sq_qishu.setText(_translate("MainWindow", ""))
        self.label_26.setText(_translate("MainWindow", "投注金额："))
        self.sq_jieguo.setText(_translate("MainWindow", ""))
        self.label_28.setText(_translate("MainWindow", "是否正确："))
        self.sq_daxiao.setText(_translate("MainWindow", ""))
        self.label_30.setText(_translate("MainWindow", "投注模式："))
        self.sq_moshi.setText(_translate("MainWindow", ""))
        self.label_18.setText(_translate("MainWindow", "上期期数："))

    def down_submit_data(self):
        self.t1 = init_data()
        self.t1.up_submit_info.connect(self.up_submit_jm)
        self.t1.up_dt_info.connect(self.up_dt_listview)
        self.t1.up_lcd_num.connect(self.up_lcd_num)
        self.t1.up_curinfo.connect(self.up_curr_info)
        self.t1.up_lastinfo.connect(self.up_lastvote_info)
        self.t1.up_statusinfo.connect(self.up_status_info)
        self.t1.up_table_info.connect(self.up_table_info)
        self.t1.jieshou(self.lineEdit_name.text().strip(), self.lineEdit_pwd.text().strip(), '')
        self.t1.start()
        pass

    def up_submit_jm(self, data):
        if data == '登录成功':
            self.submit_Button.setText(data)
            c_time = time.strftime('%m-%d %H:%M', time.localtime(time.time()))
            self.user_info.setText("登录时间:" + c_time)
            self.submit_Button.setEnabled(False)
        else:
            self.submit_Button.setText(data)

    def up_dt_listview(self, data):
        self.dt_listview.addItem(data)

    def up_lcd_num(self, data):
        self.lcdNumber.display(data)

    def up_curr_info(self, data):
        self.dq_qishu.setText(str(data[0]))
        self.dq_jine.setText(str(data[1]))
        self.dq_jishu.setText(str(data[2]))
        self.lxcw.setText(str(data[3]))
        self.shouyi.setText(str(data[4]))
        if data[5] == 0:
            x = '真实'
        else:
            x = '模拟'
        self.dq_moshi.setText(str(x))
        self.dq_daxiao.setText(str(data[6]))

    def up_lastvote_info(self, data):
        self.sq_qishu.setText(str(data[0]))
        self.sq_jine.setText(str(data[1]))
        self.sq_jishu.setText(str(data[2]))
        self.sq_jieguo.setText(str(data[3]))
        self.sq_daxiao.setText(str(data[4]))
        self.sq_moshi.setText(str(data[5]))
        pass

    def up_table_info(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        soup=BeautifulSoup(data,'lxml')
        for y in soup.find_all('tr'):
            if str(y).find('已结束') > 0:
                dqhs = self.tableWidget.rowCount()
                self.tableWidget.insertRow(dqhs)
                res = y.find_all('td')
                period = res[0].text
                vote_time = res[1].text
                jcjg = re.findall(r'\d+', str(res[2].find_all('img')[-1]))[0]
                self.tableWidget.setItem(dqhs, 0, QtWidgets.QTableWidgetItem(period))
                self.tableWidget.setItem(dqhs, 1, QtWidgets.QTableWidgetItem(vote_time))
                self.tableWidget.setItem(dqhs, 2, QtWidgets.QTableWidgetItem(str(jcjg)))
        pass

    def up_status_info(self, data):
        self.statusbar.showMessage(data)
        pass


class init_data(QThread):
    """更新数据类"""
    up_submit_info = pyqtSignal(str)
    up_dt_info = pyqtSignal(str)
    up_lcd_num = pyqtSignal(int)
    up_curinfo = pyqtSignal(tuple)
    up_lastinfo = pyqtSignal(tuple)
    up_statusinfo = pyqtSignal(str)
    up_table_info=pyqtSignal(str)

    def jieshou(self, name, password, vali):
        self.var1 = name
        self.var2 = password
        self.var3 = vali

    def remaxwrong(self):
        maxdb = p_mysql.MySQL()
        sql = 'select * from le_js28 order by period DESC  limit 300'
        result_list = maxdb.query(sql)
        xwrong = 0
        retperiod = 0
        for index, x in enumerate(result_list[:-5]):
            # 当前期结果为
            current_result = x[2]
            current_period = x[0]
            s1 = int(result_list[index + 1][2])
            s2 = int(result_list[index + 2][2])
            s3 = int(result_list[index + 3][2])
            s4 = int(result_list[index + 4][2])
            s5 = int(result_list[index + 5][2])
            # print(current_period, s1, s2, s3, s4, s5)
            if s1 < 14:
                vode_dx = 0
                if s2 > 13 :
                    vode_dx = 1
            else:
                vode_dx = 1
                if s2 < 14 :
                    vode_dx = 0
            if vode_dx == 0 and int(current_result) < 14:
                xwrong = 0
            if vode_dx == 0 and int(current_result) > 13:
                xwrong = xwrong + 1
            if vode_dx == 1 and int(current_result) > 13:
                xwrong = 0
            if vode_dx == 1 and int(current_result) < 14:
                xwrong = xwrong + 1
            if xwrong == 6:
                retperiod = result_list[index][0]
                del maxdb
                return retperiod
        del maxdb
        return retperiod

    def q_curr_period(self):
        first_run = 0
        jishu = 0
        multiple = [1, 3, 7, 15, 31, 63, 127, 34, 55, 89, 144, 1, 1]
        maxwrong = 6
        global moni
        firstflag_vote = ''
        current_period = ''
        vote_retime = 0
        endf = 1
        wrong = 0
        wrongflag = False
        vote_list = []
        toufayu=False
        self.header = {"Accept": "application/json, text/javascript, */*",
                       "Accept-Encoding": "gzip, deflate",
                       "Accept-Language": "zh-cn",
                       "Cache-Control": "no-cache",
                       "Connection": "Keep-Alive",
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Host": "www.lezhuan.com",
                       "Referer": "http://www.lezhuan.com/",
                       "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                       "X-Requested-With": "XMLHttpRequest"}
        self.url = 'http://www.lezhuan.com/fast/'
        while True:
            yinshu = 2
            list_v = []
            c_time = time.strftime('%m-%d %H:%M', time.localtime(time.time()))
            try:
                gol_cookies['cGlobal[last]'] = str(int(time.time()))
                req = requests.get(self.url, cookies=gol_cookies, headers=self.header)
                # print('查询页面时使用的全局cookies', gol_cookies)
                soup = BeautifulSoup(req.text, 'lxml')
                # 查询当前投注信息
                vote_info = soup.find_all('script', attrs={'type': 'text/javascript'})
                # 第一步 找到当前期 这里必然找出当前期，目的是为了投注。
                if vote_info != None:
                    try:
                        temp_a = re.findall(r"parseInt\(\"(.+?)\"\)", vote_info[2].text)
                        temp_b = re.findall(r"fTimingNO = \"(.+?)\";", vote_info[2].text)
                        current_period = temp_b[0]
                        vote_retime = int(temp_a[0])
                        if vote_retime > 9:
                            self.up_dt_info.emit('当前期' + current_period + '剩余' + str(vote_retime) + '秒投注')
                        else:
                            self.up_dt_info.emit(str(current_period) + '截止投注')
                    except Exception as e:
                        self.up_dt_info.emit('搜索javascrpt出错，错误信息,%s' % traceback.format_exc())
                if current_period != '':
                    # 添加保存第一次金币部分
                    self.up_table_info.emit(req.text)
                    try:
                        current_jinbi = (
                            soup.find('span', attrs={'style': 'padding-left:10px;'}).find_next_sibling(
                                'span').string).replace(
                            ',', '')
                    except Exception as e:
                        print(repr(e))
                    if firstflag_vote == '':
                        firstflag_vote = current_period
                        firstflag_jinbi = current_jinbi
                        config = configparser.ConfigParser()
                        config.read("Config_lezhuan.ini")
                        config_title = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        try:
                            config.add_section(config_title)
                            config.set(config_title, "starttime：", config_title)
                            config.set(config_title, "firstvote：", firstflag_vote)
                            config.set(config_title, "firstjinbi", firstflag_jinbi)
                            config.write(open("Config_lezhuan.ini", "w"))
                            tempa = config.sections()
                            newa = []
                            findtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                            # print(findtime)
                            for x in tempa:
                                # print(x.find(findtime))
                                if x.find(findtime) >= 0:
                                    newa.append(x)
                            todayfirstjinbi = int(config.get(newa[0], 'firstjinbi'))
                        except configparser.DuplicateSectionError:
                            print("Section already exists")
                    # 循环采集部分
                    mydb = p_mysql.MySQL()
                    # 查询数据库最后一期，然后显示出来
                    sql_text = "select period from le_js28 ORDER BY period DESC limit 1"
                    sql_re = mydb.query(sql_text)
                    if len(sql_re) <= 0:
                        endf = 67
                    else:
                        endf = int((int(current_period) - int(sql_re[0][0])) / 25) + 1
                        if endf >= 67:
                            endf = 67
                    self.up_dt_info.emit("需采集" + str(endf) + "页数")
                    x = 1
                    while x <= endf:
                        self.up_dt_info.emit("开始采集，第" + str(x) + "页")
                        pdata = {'p': x}
                        try:
                            if x == 1:
                                req_one = req
                            else:
                                req_one = requests.get(self.url, cookies=gol_cookies, headers=self.header, params=pdata)
                            soup = BeautifulSoup(req_one.text, 'lxml')
                            for y in soup.find_all('tr'):
                                if str(y).find('已结束') > 0:
                                    res = y.find_all('td')
                                    period = res[0].text
                                    vote_time = res[1].text
                                    jcjg = re.findall(r'\d+', str(res[2].find_all('img')[-1]))[0]
                                    # print(period, vote_time, jcjg)
                                    sql = "insert into le_js28 values ('" + period + "','" + vote_time + "','" + str(
                                        jcjg) + "')"
                                    mydb.query(sql)
                            time.sleep(0.5)
                            x = x + 1
                        except Exception as e:
                            self.up_dt_info.emit("采集过程中，页面信息问题，重新采集该页")
                            x = x - 1
                            if x <= 0:
                                x = 1

                    self.up_dt_info.emit("采集完成")
                    if first_run == 0:
                        self.up_dt_info.emit('先搜索最近的一次错6')
                        remax = self.remaxwrong()
                        first_run = 1
                        self.up_statusinfo.emit('第一次查询错六为： ' + str(remax) + " 期")
                        self.up_dt_info.emit('搜索结束')
                    # 每一次，必须采集完成后，才开始从数据库中拿数据判断
                    if vote_list:  # 如果不为空，说明上一次投注了，判断是否正确。
                        try:
                            vote_period = str(vote_list[-1]).strip()
                            sql = "select * from le_js28 where period='" + vote_period + "' limit 1"
                            redata = mydb.query(sql)
                            last_vote = redata[0][2]
                            # print('返回列表', vote_list, '查找返回投注期的结果', last_vote[0])
                            self.up_dt_info.emit('上期投注列表' + str(vote_list))
                            if int(last_vote) in vote_list:
                                print('投注正确,倍率清空')
                                self.up_lastinfo.emit((vote_period, '', '', last_vote, '正确', ''))
                                wrong = 0
                                if wrongflag == True and moni == 1:
                                    wrongflag = False
                                    toufayu = True
                                    jishu = 0
                                    moni = 0
                            else:
                                self.up_lastinfo.emit((vote_period, '', '', last_vote, '错误', ''))
                                if int(last_vote) > 0:
                                    # print('投注错误,次数加 1 ,错误次数：', wrong)
                                    wrong = wrong + 1
                                    if wrong >= maxwrong:
                                        wrongflag = True
                                        moni = 1
                        except Exception as e:
                            self.up_dt_info.emit("查询已投注的结果错误:%s" % traceback.format_exc())
                            # ---------------------------------------------------
                    s1 = str(int(current_period) - 1)
                    s2 = str(int(current_period) - 2)
                    s3 = str(int(current_period) - 3)
                    s4 = str(int(current_period) - 4)
                    sql = "select * from le_js28 where period='" + s1 + "' or period='" + s2 + "' or period='" + s3 + "' or period='" + s4 + "' order by period DESC"
                    # print(sql)
                    redata_1 = mydb.query(sql)
                    print(redata_1)
                    last_1 = redata_1[0][2]
                    last_2 = redata_1[1][2]
                    last_3 = redata_1[2][2]
                    last_4 = redata_1[3][2]
                    print(last_1, last_2, last_3, last_4)
                    if vote_retime > 9:
                        if moni == 0:
                            if jishu >= 5 and wrong == 0:
                                toufayu = False
                            if toufayu == True:
                                yinshu = 10
                            jishu = jishu + 1
                            if jishu >= 220 and wrong<=2:
                                moni = 1
                                jishu = 0
                        print('lezhuan,最大错:', maxwrong, '当前错误', wrong, "金币：", '倍数', yinshu, '模拟', moni, '投注次数', jishu,
                              '错标', wrongflag, '偷发育', toufayu)
                        list_v = daxiao_1(last_1, last_2, last_3, last_4, multiple[wrong], yinshu)
                    if list_v:
                        vote_list = vote_thing(current_period, list_v)
                        if int(vote_list[0]) < 10:
                            dd = '小'
                        else:
                            dd = '大'
                        self.up_curinfo.emit((current_period, multiple[wrong] * yinshu * 500, jishu, wrong,
                                              int(current_jinbi) - todayfirstjinbi, moni, dd))
                    else:
                        vote_list = []
                        self.up_curinfo.emit((current_period, '', '', '', '', moni, ''))
                    del mydb
                    dealy_time = vote_retime + 28
                    self.up_dt_info.emit('延时%s刷新' % dealy_time)
                    for m in range(dealy_time, -1, -1):
                        self.up_lcd_num.emit(m)
                        time.sleep(1)
                else:
                    self.up_dt_info.emit("当前期都没找到，继续延时30秒查找")
            except Exception as e:
                print('traceback.format_exc():%s' % traceback.format_exc())
                self.up_dt_info.emit("访问网站出错，等待10秒，重新访问" + repr(e))
                time.sleep(5)

    def run(self):
        global gol_cookies
        post_head = {"Accept": "application/json, text/javascript, */*",
                     "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-cn",
                     "Cache-Control": "no-cache",
                     "Connection": "Keep-Alive",
                     "Content-Type": "application/x-www-form-urlencoded",
                     "Host": "www.lezhuan.com",
                     "Referer": "http://www.lezhuan.com/login.html",
                     "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                     "X-Requested-With": "XMLHttpRequest"}
        try:
            # 产生一个0-1的随机数字 17位
            rankey = random.random()
            # 直接发送请求ajax 获得token
            pst_ajax = {'act': 'visitReg', 'key': rankey, 'url': 'http://www.lezhuan.com/'}
            url = 'http://www.lezhuan.com/ajax.php'
            # Post数据服务器
            req = requests.post(url, data=pst_ajax, headers=post_head, allow_redirects=False)
            sub_ajax = {'act': 'login', 'key': rankey, 'url': 'http://www.lezhuan.com/',
                        'tbUserAccount': self.var1, 'tbUserPwd': 'xfcctv1983',
                        'token': json.loads(req.text)['token']}
            time.sleep(0.1)
            req1 = requests.post(url, data=sub_ajax, headers=post_head, cookies=req.cookies, allow_redirects=False)
            if json.loads(req1.text)['error'] == '10000':
                # print('登录成功')
                self.up_dt_info.emit('登录成功')
                gol_cookies = req1.cookies
                cj_dict = requests.utils.dict_from_cookiejar(gol_cookies)
                cj_dict['cGlobal[last]'] = str(int(time.time()))
                gol_cookies = requests.utils.cookiejar_from_dict(cj_dict, cookiejar=None, overwrite=True)
                # 开始循环了,NO，应该先更新个人信息，并显示出来，而且要把前面的输入框给禁止
                self.up_submit_info.emit("登录成功")
                self.q_curr_period()
            else:
                self.up_submit_info.emit("登录失败")
                pass
        except Exception as e:
            self.up_dt_info.emit(repr(e))


def daxiao_1(s1, s2, s3, s4, multiple, bt):
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    s4 = int(s4)
    vote_side = 0  # 0代表不投注，1代表买中，2代表买边
    list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    list_num = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 63, 69, 73, 75, 75, 73, 69, 63, 55, 45, 36, 28, 21, 15, 10, 6, 3,
                1]
    if s1 < 14:
        vote_dx = 0
        if s2 > 13:
            vote_dx = 1
    else:
        vote_dx = 1
        if s2 < 14:
            vote_dx = 0
    if vote_dx == 0:
        for index, i in enumerate(list_num):
            if index < 14:
                list_num[index] = int(list_num[index] * bt * multiple)
            else:
                list_num[index] = 0
        return list_num
    elif vote_dx == 1:
        for index, i in enumerate(list_num):
            if index > 13:
                list_num[index] = int(list_num[index] * bt * multiple)
            else:
                list_num[index] = 0
        return list_num


def vote_thing(vote_current, list_v):  # 负责投注的函数
    global jishu
    global moni
    global xxx
    return_list = []
    list_num = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 63, 69, 73, 75, 75, 73, 69, 63, 55, 45, 36, 28, 21, 15, 10, 6, 3,
                1]
    get_head = {"Accept": "text/html, application/xhtml+xml, */*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-cn",
                "Connection": "Keep-Alive",
                "Host": "www.lezhuan.com",
                "Referer": "http://www.lezhuan.com/fast/",
                "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"
                }
    post_head = {"Accept": "text/html, application/xhtml+xml, */*",
                 "Accept-Encoding": "gzip, deflate",
                 "Accept-Language": "zh-cn",
                 "Cache-Control": "no-cache",
                 "Connection": "Keep-Alive",
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Host": "www.lezhuan.com",
                 "Referer": "http://www.lezhuan.com/fast/insert.php?funNO=" + vote_current,
                 "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                 "X-Requested-With": "XMLHttpRequest"}
    url = 'http://www.lezhuan.com/fast/insert.php?fastNO=' + vote_current
    try:
        url_1 = "http://www.lezhuan.com/fast/insert.php?funNO=" + vote_current
        req_te = requests.get(url_1, cookies=gol_cookies, headers=get_head, allow_redirects=False, timeout=10)
        soup = BeautifulSoup(req_te.text, 'lxml')
        cc = soup.find('input', attrs={'type': "hidden", 'name': 'fast'})
        a = {}
        a['fast'] = cc['value']
        for index, bb in enumerate(list_v):
            if bb > 0:
                a['tbChk[' + str(index) + ']'] = 'on'
        for index, bb in enumerate(list_v):
            if bb > 0:
                a['tbNum[' + str(index) + ']'] = bb
            else:
                a['tbNum[' + str(index) + ']'] = ''
        gol_cookies['cGlobal[last]'] = str(int(time.time()))
        if moni == 0:
            req = requests.post(url, data=a, cookies=gol_cookies, headers=post_head,
                                allow_redirects=False, timeout=10)
            # print('打印投注返回信息:', req.content)
            if req.text.find('投注成功') > 0:
                for x in range(0, 28):
                    if int(list_v[x]) >= list_num[x]:
                        return_list.append(x)
                return_list.append(vote_current.strip())
                print(vote_current, '真实,投注成功购买的列表是', return_list)
                return return_list
            else:
                print(vote_current, '投注失败，购买的列表是空')
                return []
        else:
            for x in range(0, 28):
                if int(list_v[x]) >= list_num[x]:
                    return_list.append(x)
            return_list.append(vote_current.strip())
            print(vote_current, '模拟，投注成功购买的列表是', return_list)
            f = open('touzhu_jilu.txt', 'a+')
            f.write(vote_current.strip() + "期，投注+1\n")
            f.close()
            return return_list
    except Exception as e:
        if moni == 0:
            f.write(req.text)
        f.close()
        print('出错，购买的列表是空')
        return []


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
