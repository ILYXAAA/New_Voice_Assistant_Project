# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_window(object):
    def setupUi(self, Settings_window):
        Settings_window.setObjectName("Settings_window")
        Settings_window.resize(1326, 581)
        Settings_window.setMaximumSize(QtCore.QSize(1326, 581))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/icons/settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings_window.setWindowIcon(icon)
        self.backup_to_mine = QtWidgets.QPushButton(Settings_window)
        self.backup_to_mine.setEnabled(True)
        self.backup_to_mine.setGeometry(QtCore.QRect(990, 260, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_to_mine.sizePolicy().hasHeightForWidth())
        self.backup_to_mine.setSizePolicy(sizePolicy)
        self.backup_to_mine.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.backup_to_mine.setFont(font)
        self.backup_to_mine.setStyleSheet("QPushButton{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 159, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    \n"
"}")
        self.backup_to_mine.setObjectName("backup_to_mine")
        self.reset = QtWidgets.QPushButton(Settings_window)
        self.reset.setEnabled(True)
        self.reset.setGeometry(QtCore.QRect(210, 510, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reset.setFont(font)
        self.reset.setStyleSheet("QPushButton{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 159, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    \n"
"}")
        self.reset.setObjectName("reset")
        self.verticalLayoutWidget = QtWidgets.QWidget(Settings_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 801, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.assistant_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assistant_name.sizePolicy().hasHeightForWidth())
        self.assistant_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.assistant_name.setFont(font)
        self.assistant_name.setStyleSheet("color: rgb(49, 49, 49);")
        self.assistant_name.setText("")
        self.assistant_name.setObjectName("assistant_name")
        self.horizontalLayout_5.addWidget(self.assistant_name)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.person_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.person_name.sizePolicy().hasHeightForWidth())
        self.person_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.person_name.setFont(font)
        self.person_name.setStyleSheet("color: rgb(49, 49, 49);")
        self.person_name.setText("")
        self.person_name.setObjectName("person_name")
        self.horizontalLayout_3.addWidget(self.person_name)
        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.line_region = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_region.sizePolicy().hasHeightForWidth())
        self.line_region.setSizePolicy(sizePolicy)
        self.line_region.setMinimumSize(QtCore.QSize(260, 31))
        self.line_region.setMaximumSize(QtCore.QSize(290, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_region.setFont(font)
        self.line_region.setStyleSheet("color: rgb(49, 49, 49);")
        self.line_region.setText("")
        self.line_region.setObjectName("line_region")
        self.horizontalLayout_4.addWidget(self.line_region)
        self.region = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.region.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.region.setFont(font)
        self.region.setObjectName("region")
        self.horizontalLayout_4.addWidget(self.region)
        spacerItem4 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(191, 52))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.program_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.program_path.sizePolicy().hasHeightForWidth())
        self.program_path.setSizePolicy(sizePolicy)
        self.program_path.setMaximumSize(QtCore.QSize(600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.program_path.setFont(font)
        self.program_path.setStyleSheet("color: rgb(49, 49, 49);")
        self.program_path.setObjectName("program_path")
        self.horizontalLayout_6.addWidget(self.program_path)
        spacerItem6 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(191, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.keepass_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keepass_path.sizePolicy().hasHeightForWidth())
        self.keepass_path.setSizePolicy(sizePolicy)
        self.keepass_path.setMaximumSize(QtCore.QSize(600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.keepass_path.setFont(font)
        self.keepass_path.setStyleSheet("color: rgb(49, 49, 49);")
        self.keepass_path.setObjectName("keepass_path")
        self.horizontalLayout_9.addWidget(self.keepass_path)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.choose_keepass_path = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.choose_keepass_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_keepass_path.sizePolicy().hasHeightForWidth())
        self.choose_keepass_path.setSizePolicy(sizePolicy)
        self.choose_keepass_path.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_keepass_path.setFont(font)
        self.choose_keepass_path.setStyleSheet("QPushButton{\n"
"    background-color: rgb(199, 199, 199);\n"
"    color: rgb(49, 49, 49);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(184, 184, 184);\n"
"    color: rgb(49, 49, 49);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(89, 89, 89);\n"
"    color: rgb(49, 49, 49);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    \n"
"}")
        self.choose_keepass_path.setObjectName("choose_keepass_path")
        self.horizontalLayout_9.addWidget(self.choose_keepass_path)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pc_speed = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pc_speed.setFont(font)
        self.pc_speed.setObjectName("pc_speed")
        self.horizontalLayout_2.addWidget(self.pc_speed)
        spacerItem9 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.speech_recognition_base = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.speech_recognition_base.setFont(font)
        self.speech_recognition_base.setPlaceholderText("")
        self.speech_recognition_base.setObjectName("speech_recognition_base")
        self.horizontalLayout_7.addWidget(self.speech_recognition_base)
        spacerItem10 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem11 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.vk_api = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vk_api.sizePolicy().hasHeightForWidth())
        self.vk_api.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vk_api.setFont(font)
        self.vk_api.setStyleSheet("color: rgb(49, 49, 49);")
        self.vk_api.setObjectName("vk_api")
        self.horizontalLayout_8.addWidget(self.vk_api)
        spacerItem12 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.test = QtWidgets.QPushButton(Settings_window)
        self.test.setEnabled(True)
        self.test.setGeometry(QtCore.QRect(1180, 260, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test.sizePolicy().hasHeightForWidth())
        self.test.setSizePolicy(sizePolicy)
        self.test.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.test.setFont(font)
        self.test.setStyleSheet("QPushButton{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 159, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    \n"
"}")
        self.test.setObjectName("test")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(Settings_window)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(850, 20, 471, 51))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_11.setMaximumSize(QtCore.QSize(201, 41))
        self.label_11.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.speaker_engine = QtWidgets.QComboBox(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.speaker_engine.setFont(font)
        self.speaker_engine.setObjectName("speaker_engine")
        self.horizontalLayout_10.addWidget(self.speaker_engine)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.apply = QtWidgets.QPushButton(Settings_window)
        self.apply.setEnabled(True)
        self.apply.setGeometry(QtCore.QRect(20, 510, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply.sizePolicy().hasHeightForWidth())
        self.apply.setSizePolicy(sizePolicy)
        self.apply.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.apply.setFont(font)
        self.apply.setStyleSheet("QPushButton{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 159, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(10, 104, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    \n"
"}")
        self.apply.setObjectName("apply")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Settings_window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(870, 80, 451, 167))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setMaximumSize(QtCore.QSize(103, 29))
        self.label_12.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        spacerItem15 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.language = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.language.setFont(font)
        self.language.setObjectName("language")
        self.horizontalLayout_11.addWidget(self.language)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setMaximumSize(QtCore.QSize(150, 29))
        self.label_14.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        spacerItem17 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem17)
        self.speaker_voice = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speaker_voice.setFont(font)
        self.speaker_voice.setObjectName("speaker_voice")
        self.horizontalLayout_13.addWidget(self.speaker_voice)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setMaximumSize(QtCore.QSize(134, 29))
        self.label_16.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        spacerItem19 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.sample_rate = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sample_rate.setFont(font)
        self.sample_rate.setObjectName("sample_rate")
        self.horizontalLayout_15.addWidget(self.sample_rate)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setMaximumSize(QtCore.QSize(96, 29))
        self.label_13.setStyleSheet("color: rgb(49, 49, 49);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        spacerItem21 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem21)
        self.model_id = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.model_id.setFont(font)
        self.model_id.setObjectName("model_id")
        self.horizontalLayout_12.addWidget(self.model_id)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.retranslateUi(Settings_window)
        QtCore.QMetaObject.connectSlotsByName(Settings_window)

    def retranslateUi(self, Settings_window):
        _translate = QtCore.QCoreApplication.translate
        Settings_window.setWindowTitle(_translate("Settings_window", "Settings"))
        self.backup_to_mine.setText(_translate("Settings_window", "Return engine"))
        self.reset.setText(_translate("Settings_window", "Reset"))
        self.label_6.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Assistant Name</span></p></body></html>"))
        self.label_4.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Person Name</span></p></body></html>"))
        self.label_5.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Region</span></p></body></html>"))
        self.label_7.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Program Path</span></p></body></html>"))
        self.label_10.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">KeePass Path</span></p></body></html>"))
        self.choose_keepass_path.setText(_translate("Settings_window", "Choose"))
        self.label_3.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">PC Speed</span></p></body></html>"))
        self.label_8.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Speech Recognition Base</span></p></body></html>"))
        self.label_9.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">VK API</span></p></body></html>"))
        self.test.setText(_translate("Settings_window", "Test"))
        self.label_11.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:16pt;\">Speaker Engine</span></p></body></html>"))
        self.apply.setText(_translate("Settings_window", "Apply"))
        self.label_12.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:14pt;\">Language</span></p></body></html>"))
        self.label_14.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:14pt;\">Speaker Voice</span></p></body></html>"))
        self.label_16.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:14pt;\">Sample Rate</span></p></body></html>"))
        self.label_13.setText(_translate("Settings_window", "<html><head/><body><p><span style=\" font-size:14pt;\">Model ID</span></p></body></html>"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings_window = QtWidgets.QDialog()
    ui = Ui_Settings_window()
    ui.setupUi(Settings_window)
    Settings_window.show()
    sys.exit(app.exec_())
