# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfeic5.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class StarWindow(QtWidgets.QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 320, 124)
        self.image = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap("Images/emblem.gif")
        self.image.setPixmap(pixmap)
        self.image.resize(320, 124)
        self.image.move(0, 0)
        self.show()
class Errors(QtWidgets.QMainWindow):
    def __init__(self, h):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(623, 460)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Ошибки"))
        self.label.setText(_translate("MainWindow", "Отклонение нагрузок:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО учителя"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Класс"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Предмет"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Нагрузка\nучителя"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Нагрузка\nрасписание"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Отклонение"))
        self.label_2.setText(_translate("MainWindow", "Протокол использования учителя одновременно в друх разных классах"))
        self.show()
        print(h)
        for i in h:
            if i[0] == 0:
                self.tableWidget.insertRow(0)
                i = i[1:]
                for j in range(6):
                    self.tableWidget.setItem(0, j, QtWidgets.QTableWidgetItem(str(i[j])))
        dic = {2: "во Вторник", 1: "в Понедельник", 3: "в Среду", 4: "в Четверг", 5: "в Пятницу", 6: "в Субботу"}
        for i in h:
            if i[0] == 1:
                i = i[1:]
                print(i[3])
                self.listWidget.addItem(f"Учитель {i[0]} {dic[i[1]]} на {i[2]} уроке\nошибочно использован в классах: {', '.join(list(map(lambda x: str(x[0]), i[3])))}")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_of_tabs = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.list_of_tabs.setFont(font)
        self.list_of_tabs.setObjectName("list_of_tabs")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_timetable_to_excel = QtWidgets.QPushButton(self.tab_3)
        self.btn_timetable_to_excel.setObjectName("btn_timetable_to_excel")
        self.horizontalLayout_9.addWidget(self.btn_timetable_to_excel)
        self.btn_check = QtWidgets.QPushButton(self.tab_3)
        self.btn_check.setObjectName("btn_check")
        self.horizontalLayout_9.addWidget(self.btn_check)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_7.addWidget(self.lineEdit)
        self.table_of_timetable = QtWidgets.QTableWidget(self.tab_3)
        self.table_of_timetable.setRowCount(6)
        self.table_of_timetable.setObjectName("table_of_timetable")
        self.table_of_timetable.setColumnCount(0)
        self.table_of_timetable.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.table_of_timetable)
        self.list_of_tabs.addTab(self.tab_3, "")
        self.teachers = QtWidgets.QWidget()
        self.teachers.setObjectName("teachers")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.teachers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_btn_teachers = QtWidgets.QPushButton(self.teachers)
        self.add_btn_teachers.setMaximumSize(QtCore.QSize(161, 51))
        self.add_btn_teachers.setObjectName("add_btn_teachers")
        self.horizontalLayout_2.addWidget(self.add_btn_teachers)
        self.delete_btn_teachers = QtWidgets.QPushButton(self.teachers)
        self.delete_btn_teachers.setMaximumSize(QtCore.QSize(161, 51))
        self.delete_btn_teachers.setObjectName("delete_btn_teachers")
        self.horizontalLayout_2.addWidget(self.delete_btn_teachers)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.table_of_teachers = QtWidgets.QTableWidget(self.teachers)
        self.table_of_teachers.setInputMethodHints(QtCore.Qt.ImhNone)
        self.table_of_teachers.setObjectName("table_of_teachers")
        self.table_of_teachers.setColumnCount(4)
        self.table_of_teachers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(False)
        item.setFont(font)
        self.table_of_teachers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(157, 157, 157))
        self.table_of_teachers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.table_of_teachers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(211, 211, 211))
        self.table_of_teachers.setHorizontalHeaderItem(3, item)
        self.table_of_teachers.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_3.addWidget(self.table_of_teachers)
        self.list_of_tabs.addTab(self.teachers, "")
        self.school_objects = QtWidgets.QWidget()
        self.school_objects.setObjectName("school_objects")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.school_objects)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_btn_school_objects = QtWidgets.QPushButton(self.school_objects)
        self.add_btn_school_objects.setMaximumSize(QtCore.QSize(161, 51))
        self.add_btn_school_objects.setObjectName("add_btn_school_objects")
        self.horizontalLayout_4.addWidget(self.add_btn_school_objects)
        self.delete_btn_school_objects = QtWidgets.QPushButton(self.school_objects)
        self.delete_btn_school_objects.setMaximumSize(QtCore.QSize(161, 51))
        self.delete_btn_school_objects.setObjectName("delete_btn_school_objects")
        self.horizontalLayout_4.addWidget(self.delete_btn_school_objects)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.table_of_subjects = QtWidgets.QTableWidget(self.school_objects)
        self.table_of_subjects.setObjectName("table_of_subjects")
        self.table_of_subjects.setColumnCount(3)
        self.table_of_subjects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_subjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_subjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_subjects.setHorizontalHeaderItem(2, item)
        self.table_of_subjects.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.table_of_subjects)
        self.list_of_tabs.addTab(self.school_objects, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_btn_school_classes = QtWidgets.QPushButton(self.tab_4)
        self.add_btn_school_classes.setMaximumSize(QtCore.QSize(161, 51))
        self.add_btn_school_classes.setObjectName("add_btn_school_classes")
        self.horizontalLayout_6.addWidget(self.add_btn_school_classes)
        self.delete_btn_school_classes = QtWidgets.QPushButton(self.tab_4)
        self.delete_btn_school_classes.setMaximumSize(QtCore.QSize(161, 51))
        self.delete_btn_school_classes.setObjectName("delete_btn_school_classes")
        self.horizontalLayout_6.addWidget(self.delete_btn_school_classes)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.table_of_classes = QtWidgets.QTableWidget(self.tab_4)
        self.table_of_classes.setObjectName("table_of_classes")
        self.table_of_classes.setColumnCount(3)
        self.table_of_classes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_classes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_classes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_classes.setHorizontalHeaderItem(2, item)
        self.table_of_classes.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_4.addWidget(self.table_of_classes)
        self.list_of_tabs.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.filter_for_loads_on_class = QtWidgets.QComboBox(self.tab_2)
        self.filter_for_loads_on_class.setMinimumSize(QtCore.QSize(161, 1))
        self.filter_for_loads_on_class.setMaximumSize(QtCore.QSize(161, 32))
        self.filter_for_loads_on_class.setObjectName("filter_for_loads_on_class")
        self.horizontalLayout.addWidget(self.filter_for_loads_on_class)
        self.horizontalLayout_10.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.add_btn_loads = QtWidgets.QPushButton(self.tab_2)
        self.add_btn_loads.setMinimumSize(QtCore.QSize(161, 0))
        self.add_btn_loads.setMaximumSize(QtCore.QSize(161, 51))
        self.add_btn_loads.setObjectName("add_btn_loads")
        self.horizontalLayout_10.addWidget(self.add_btn_loads)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.delete_btn_loads = QtWidgets.QPushButton(self.tab_2)
        self.delete_btn_loads.setMinimumSize(QtCore.QSize(161, 0))
        self.delete_btn_loads.setMaximumSize(QtCore.QSize(161, 51))
        self.delete_btn_loads.setObjectName("delete_btn_loads")
        self.horizontalLayout_10.addWidget(self.delete_btn_loads)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.table_of_loads = QtWidgets.QTableWidget(self.tab_2)
        self.table_of_loads.setObjectName("table_of_loads")
        self.table_of_loads.setColumnCount(5)
        self.table_of_loads.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_loads.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_loads.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_loads.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_loads.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_loads.setHorizontalHeaderItem(4, item)
        self.table_of_loads.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_6.addWidget(self.table_of_loads)
        self.list_of_tabs.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(110, 20, 320, 124))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 101, 16))
        self.label_2.setObjectName("label_2")
        self.name_of_school = QtWidgets.QLineEdit(self.tab)
        self.name_of_school.setGeometry(QtCore.QRect(150, 180, 421, 20))
        self.name_of_school.setObjectName("name_of_school")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(750, 520, 175, 75))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(670, 500, 221, 61))
        self.label_4.setObjectName("label_4")
        self.save_name_of_school = QtWidgets.QPushButton(self.tab)
        self.save_name_of_school.setGeometry(QtCore.QRect(350, 200, 221, 23))
        self.save_name_of_school.setObjectName("save_name_of_school")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 250, 213, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.one_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.one_urok.setObjectName("one_urok")
        self.horizontalLayout_12.addWidget(self.one_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.two_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.two_urok.setObjectName("two_urok")
        self.horizontalLayout_3.addWidget(self.two_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.three_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.three_urok.setObjectName("three_urok")
        self.horizontalLayout_14.addWidget(self.three_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.fout_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.fout_urok.setObjectName("fout_urok")
        self.horizontalLayout_5.addWidget(self.fout_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.five_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.five_urok.setObjectName("five_urok")
        self.horizontalLayout_13.addWidget(self.five_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.six_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.six_urok.setObjectName("six_urok")
        self.horizontalLayout_7.addWidget(self.six_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.seven_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.seven_urok.setObjectName("seven_urok")
        self.horizontalLayout_15.addWidget(self.seven_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.eight_urok = QtWidgets.QLineEdit(self.layoutWidget)
        self.eight_urok.setObjectName("eight_urok")
        self.horizontalLayout_8.addWidget(self.eight_urok)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.save_nastroiki = QtWidgets.QPushButton(self.layoutWidget)
        self.save_nastroiki.setObjectName("save_nastroiki")
        self.verticalLayout_5.addWidget(self.save_nastroiki)
        self.list_of_tabs.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.list_of_tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.list_of_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расписание 1.0"))
        self.btn_timetable_to_excel.setText(_translate("MainWindow", "Выгрузить расписание в Excel файл "))
        self.btn_check.setText(_translate("MainWindow", "Проверить"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.tab_3), _translate("MainWindow", "Расписание"))
        self.add_btn_teachers.setText(_translate("MainWindow", "Добавить"))
        self.delete_btn_teachers.setText(_translate("MainWindow", "Удалить"))
        item = self.table_of_teachers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table_of_teachers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия "))
        item = self.table_of_teachers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.table_of_teachers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "id"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.teachers), _translate("MainWindow", "Учителя"))
        self.add_btn_school_objects.setText(_translate("MainWindow", "Добавить"))
        self.delete_btn_school_objects.setText(_translate("MainWindow", "Удалить"))
        item = self.table_of_subjects.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Наименование предмета"))
        item = self.table_of_subjects.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Трудность предмета"))
        item = self.table_of_subjects.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "id"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.school_objects), _translate("MainWindow", "Предметы"))
        self.add_btn_school_classes.setText(_translate("MainWindow", "Добавить"))
        self.delete_btn_school_classes.setText(_translate("MainWindow", "Удалить"))
        item = self.table_of_classes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Класс"))
        item = self.table_of_classes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Классный Руководитель"))
        item = self.table_of_classes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "id"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.tab_4), _translate("MainWindow", "Классы"))
        self.label_11.setText(_translate("MainWindow", "Фильтр:"))
        self.add_btn_loads.setText(_translate("MainWindow", "Добавить"))
        self.delete_btn_loads.setText(_translate("MainWindow", "Удалить"))
        item = self.table_of_loads.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО учителя"))
        item = self.table_of_loads.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Класс"))
        item = self.table_of_loads.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Предмет"))
        item = self.table_of_loads.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Нагрузка"))
        item = self.table_of_loads.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "id"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.tab_2), _translate("MainWindow", "Нагрузки"))
        self.label.setText(_translate("MainWindow", "Картинка"))
        self.label_2.setText(_translate("MainWindow", "Название школы:"))
        self.label_3.setText(_translate("MainWindow", "Эмблема Яндекс"))
        self.label_4.setText(_translate("MainWindow", "Проект подготовил:\n"
"ученик 2 курса \n"
"Очилов Тимур"))
        self.save_name_of_school.setText(_translate("MainWindow", "Сохранить изменения в названии школы"))
        self.label_5.setText(_translate("MainWindow", "График Уроков"))
        self.label_10.setText(_translate("MainWindow", "1 урок"))
        self.label_6.setText(_translate("MainWindow", "2 урок"))
        self.label_15.setText(_translate("MainWindow", "3 урок"))
        self.label_7.setText(_translate("MainWindow", "4 урок"))
        self.label_14.setText(_translate("MainWindow", "5 урок"))
        self.label_8.setText(_translate("MainWindow", "6 урок"))
        self.label_16.setText(_translate("MainWindow", "7 урок"))
        self.label_9.setText(_translate("MainWindow", "8 урок"))
        self.save_nastroiki.setText(_translate("MainWindow", "Сохранить изменения Графика уроков"))
        self.list_of_tabs.setTabText(self.list_of_tabs.indexOf(self.tab), _translate("MainWindow", "Настройки"))
