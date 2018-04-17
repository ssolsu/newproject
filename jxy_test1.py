from PyQt5.QtWidgets import QWidget, QTableWidget, QApplication, QPushButton, QVBoxLayout, QTableWidgetItem, \
    QAbstractItemView, QComboBox, QGridLayout, QLabel, QListWidget
import sys, time, os
from threading import Thread
from PyQt5.QtCore import QThread, pyqtSignal
import sqlite3,random
import p_mysql


class mywindow(QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui()

    def ui(self):
        self.setWindowTitle('测试程序')
        self.resize(1200, 700)
        self.yunsuan = QPushButton('开始运算')
        self.yunsuan.clicked.connect(self.update_js)
        vlayout = QGridLayout()
        self.combox_va = QComboBox()
        self.combox_va.addItems(
            ['jxy_疯狂28', 'jxy_韩国28', 'jxy_PC28', 'You_急速28', 'You_幸运28', 'Le_急速28', 'Le_幸运28'])
        self.combox = QComboBox()
        self.combox_va.currentIndexChanged.connect(self.update_date_combobox)
        self.load1 = QPushButton('加载数据')
        self.clear1 = QPushButton('清除表格内容')
        self.clear1.clicked.connect(self.clear_table)
        self.load1.clicked.connect(self.upload_pushbotton)
        self.listview = QListWidget()
        self.talbe1 = QTableWidget()
        self.talbe1.setColumnCount(13)
        column_name = [
            '期数',
            '时间',
            '开奖号码',
            '开奖结果',
            '中',
            '边',
            '大',
            '小',
            '单',
            '双',
            '状态',
            '连错',
            '买大小',
        ]
        self.talbe1.setHorizontalHeaderLabels(column_name)  # 设置列名称
        self.talbe1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.talbe1.setColumnWidth(0, 100)
        self.talbe1.setColumnWidth(1, 100)
        self.talbe1.setColumnWidth(2, 80)
        self.talbe1.setColumnWidth(3, 80)
        self.talbe1.setColumnWidth(4, 45)
        self.talbe1.setColumnWidth(5, 45)
        self.talbe1.setColumnWidth(6, 45)
        self.talbe1.setColumnWidth(7, 45)
        self.talbe1.setColumnWidth(8, 45)
        self.talbe1.setColumnWidth(9, 45)
        self.talbe1.setColumnWidth(10, 75)
        self.talbe1.setColumnWidth(11, 70)
        self.talbe1.setColumnWidth(12, 45)
        self.talbe1.setColumnWidth(13, 45)

        vlayout.addWidget(QLabel('模式：'), 0, 0)
        vlayout.addWidget(self.combox_va, 0, 1)
        vlayout.addWidget(QLabel('日期：'), 0, 2)
        vlayout.addWidget(self.combox, 0, 3)
        vlayout.addWidget(self.load1, 0, 4)
        vlayout.addWidget(self.clear1, 0, 5)
        vlayout.addWidget(QLabel(''), 0, 6)
        vlayout.addWidget(self.yunsuan, 1, 0, 1, 7)
        vlayout.addWidget(self.talbe1, 2, 0, 1, 7)
        vlayout.addWidget(self.listview, 2, 7)
        vlayout.setColumnStretch(6, 3)
        self.setLayout(vlayout)

    # 加载数据到表格中
    def upload_pushbotton(self):
        self.t1 = thead()
        self.t1.update_table.connect(self.update_table)
        self.t1.jieshou(self.combox_va.currentIndex(), self.combox.currentText())
        self.t1.start()

    def clear_table(self):
        self.talbe1.clearContents()
        self.talbe1.setRowCount(0)
        self.listview.clear()

    def update_table(self, data):
        dqhs = self.talbe1.rowCount()
        self.talbe1.insertRow(dqhs)
        self.talbe1.setItem(dqhs, 0, QTableWidgetItem(str(data[0])))
        self.talbe1.setItem(dqhs, 1, QTableWidgetItem(data[1]))
        self.talbe1.setItem(dqhs, 2, QTableWidgetItem(data[2]))
        self.talbe1.setItem(dqhs, 3, QTableWidgetItem(data[2]))
        if int(data[2]) < 14:
            self.talbe1.setItem(dqhs, 7, QTableWidgetItem('小'))
        else:
            self.talbe1.setItem(dqhs, 6, QTableWidgetItem('大'))
        if int(data[2]) < 8 or int(data[2]) > 19:
            self.talbe1.setItem(dqhs, 5, QTableWidgetItem('边'))
        else:
            self.talbe1.setItem(dqhs, 4, QTableWidgetItem('中'))
        if int(data[2]) % 2 == 0:
            self.talbe1.setItem(dqhs, 9, QTableWidgetItem('双'))
        else:
            self.talbe1.setItem(dqhs, 8, QTableWidgetItem('单'))

    # 计算线程
    def update_js(self):
        t = Thread(target=self.daxiao)
        t.start()

    # combox那个网站内容
    def update_date_combobox(self):
        temp1 = self.combox_va.currentIndex()
        list_a = ['jx_fk28', 'jx_hg28', 'jx_pc28', 'yz_js28', 'yz_xy28', 'le_js28', 'le_xy28']
        t1 = Thread(target=self.update_table_combobox, args=(list_a[temp1],))
        t1.start()

    # 响应的日期选择
    def update_table_combobox(self, var):
        if var != '':
            self.combox.clear()
            # conn = sqlite3.connect('shuju.db')
            # cur = conn.cursor()
            mydb = p_mysql.MySQL()
            if str(var) == "yz_js28" or str(var) == "yz_xy28":
                sql_1 = "select DISTINCT substr(vote_time,1,5) from " + str(var) + " order by vote_time"
            else:
                sql_1 = "select DISTINCT substr(vote_time,1,6) from " + str(var) + " order by vote_time"
            # sql_1 = 'select DISTINCT substr(vote_time,1,6) from js28 ORDER BY vote_time'
            print(sql_1)
            # cur.execute(sql_1)
            # result = cur.fetchall()
            result = mydb.query(sql_1)
            print(result)
            if result:
                for a in result:
                    self.combox.addItem(str(a[0]))
                self.combox.setCurrentIndex(0)

    def randaxiao(self):
        rowcout = self.talbe1.rowCount()
        wrong = 0

        for i in range(0, rowcout - 20):
            dqqs = int(self.talbe1.item(i, 0).text())
            dqjg = int(self.talbe1.item(i, 3).text())
            xia1 = int(self.talbe1.item(i + 1, 3).text())
            lstx = []
            for x in range(0, 27):
                lstx.append(random.randint(0, 28))
            nlstx = [x for x in lstx if x > 13]
            blstx = [x for x in lstx if x < 14]
            if len(set(nlstx))>len(set(blstx)):
                vode_dx=1
            elif len(set(nlstx))<len(set(blstx)):
                vode_dx=0
            else:
                if xia1<14:
                    vode_dx=0
                else:
                    vode_dx=1
            if vode_dx == 0 :
                if (dqjg < 14):
                    wrong = 0
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买小正确'))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(wrong)))
                else:
                    wrong = wrong + 1
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买小错误'))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(wrong)))
                    if wrong == 6:
                        self.listview.addItem(
                            str(dqqs) + '期,错误次数达到了' + str(wrong) + '--行数' + str(self.listview.count()))
                        # fpath = os.getcwd()
                        # f = open(fpath + '\\wrong_jilu_7.txt', 'a+')
                        # f.write(str(dqqs) + "期，错误次数达到：" + str(
                        #     wrong) + '\n')
                        # f.close()
            elif vode_dx == 1:
                if (dqjg > 13):
                    wrong = 0
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买大正确'))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(wrong)))
                else:
                    wrong = wrong + 1
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买大错误'))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(wrong)))
                    if wrong == 6:
                        self.listview.addItem(
                            str(dqqs) + '期,错误次数达到了' + str(wrong) + '--行数' + str(self.listview.count()))

    def daxiao(self):
        rowcout = self.talbe1.rowCount()
        wrong = 0
        for i in range(0, rowcout - 20):
            maizhongflag = 0
            dxjg = ''
            vode_side = 1
            vode_dx = -1
            t_lst = []
            dqqs = int(self.talbe1.item(i, 0).text())
            dqjg = int(self.talbe1.item(i, 3).text())
            xia1 = int(self.talbe1.item(i + 1, 3).text())
            xia2 = int(self.talbe1.item(i + 2, 3).text())
            xia3 = int(self.talbe1.item(i + 3, 3).text())
            xia4 = int(self.talbe1.item(i + 4, 3).text())
            xia5 = int(self.talbe1.item(i + 5, 3).text())
            xia6 = int(self.talbe1.item(i + 6, 3).text())
            for w in range(1, 20):
                t_lst.append(int(self.talbe1.item(i + w, 3).text()))
            # print(t_lst)
            if xia1 < 14:
                vode_dx = 0
                if xia2 > 13 and xia3 < 14:
                    # print('这期符合要素', dqqs)
                    for index, y in enumerate(t_lst[1:-16]):
                        # print(y)
                        if y < 14:
                            if (t_lst[index + 2] > 13 and t_lst[index + 3]<14 ):
                                # print('找到一个小于14的', t_lst[index + 2], t_lst[index + 3], t_lst[index + 4],
                                #       t_lst[index ])
                                if t_lst[index]>13:
                                    print(t_lst[index])
                                    vode_dx = 1
                                break
                if xia2 < 14 and xia3 > 13:  # 符合独立2小结构
                    # vode_dx=1
                    # print('这期符合独立2小结构')
                    for index, y in enumerate(t_lst[1:-12]):
                        # print(y)
                        if y < 14:
                            if (t_lst[index + 2] < 14):
                                # print('下一期结果', t_lst[index + 2])
                                if (t_lst[index + 3] < 14):
                                    # print('下二期结果', t_lst[index + 3])
                                    vode_dx = 0
                                else:
                                    vode_dx = 1
                                break
            else:
                vode_dx = 1
                if xia2 < 14 and xia3>13 :
                    for index, y in enumerate(t_lst[1:-16]):
                        # print(y)
                        if y > 13:
                            if (t_lst[index + 2] < 14 and t_lst[index + 3]>13 ):
                                # print('找到一个小于14的', t_lst[index + 2], t_lst[index + 3], t_lst[index + 4],
                                #       t_lst[index ])
                                if t_lst[index]<14:
                                    print(t_lst[index])
                                    vode_dx = 0
                                break
                if xia2 > 13 and xia3 < 14:  # 符合独立2小结构
                    # vode_dx=0
                    for index, y in enumerate(t_lst[1:-12]):
                        # print(y)
                        if y > 13:
                            if (t_lst[index + 2] > 13):
                                if (t_lst[index + 3] > 13):
                                    vode_dx = 1
                                else:
                                    vode_dx = 0
                                break
            if vode_dx == 0 and vode_side == 1:
                if (dqjg < 14):
                    wrong = 0
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买小正确'))
                    self.talbe1.setItem(i, 11, QTableWidgetItem(str(wrong)))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(vode_dx)))
                else:
                    wrong = wrong + 1
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买小错误'))
                    self.talbe1.setItem(i, 11, QTableWidgetItem(str(wrong)))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(vode_dx)))
                    if wrong == 6:
                        self.listview.addItem(
                            str(dqqs) + '期,错误次数达到了' + str(wrong) + '--行数' + str(self.listview.count()))
                        # fpath = os.getcwd()
                        # f = open(fpath + '\\wrong_jilu_7.txt', 'a+')
                        # f.write(str(dqqs) + "期，错误次数达到：" + str(
                        #     wrong) + '\n')
                        # f.close()
            elif vode_dx == 1 and vode_side == 1:
                if (dqjg > 13):
                    wrong = 0
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买大正确'))
                    self.talbe1.setItem(i, 11, QTableWidgetItem(str(wrong)))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(vode_dx)))
                else:
                    wrong = wrong + 1
                    self.talbe1.setItem(i, 10, QTableWidgetItem('买大错误'))
                    self.talbe1.setItem(i, 11, QTableWidgetItem(str(wrong)))
                    self.talbe1.setItem(i, 12, QTableWidgetItem(str(vode_dx)))
                    if wrong == 6:
                        self.listview.addItem(
                            str(dqqs) + '期,错误次数达到了' + str(wrong) + '--行数' + str(self.listview.count()))


class thead(QThread):
    update_table = pyqtSignal(tuple)
    database_re = pyqtSignal(list)

    # var1作为网站选择，var作为日期选择
    def jieshou(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        list_a = ['jx_fk28', 'jx_hg28', 'jx_pc28', 'yz_js28', 'yz_xy28', 'le_js28', 'le_xy28']
        mydb = p_mysql.MySQL()
        sql = "select * from " + list_a[self.var1] + "  where vote_time like '%" + str(
            self.var2) + "%' ORDER by period DESC limit 1000"
        # print(sql)
        result = mydb.query(sql)
        # result = cur.fetchall()
        # print(result)
        for index, i in enumerate(result):
            row = (index,)
            data = i + row
            # print(data)
            self.update_table.emit(data)
            time.sleep(0.01)


class showlist(QThread):
    showtext = pyqtSignal(list)

    def run(self):
        pass


class thead1(QThread):
    jisuan_table = pyqtSignal(int)

    def lianjie(self):
        print('fuck')

    def run(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = mywindow()
    mw.show()
    sys.exit(app.exec_())
