# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_linhyd.ui',
# licensing of 'widget_linhyd.ui' applies.
#
# Created: Thu Oct 31 16:19:27 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_widget_linhyd(object):
    def setupUi(self, widget_linhyd):
        widget_linhyd.setObjectName("widget_linhyd")
        widget_linhyd.resize(447, 809)
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_linhyd)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(widget_linhyd)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_1.setDecimals(3)
        self.doubleSpinBox_1.setMinimum(-1e+18)
        self.doubleSpinBox_1.setMaximum(999999999999.0)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.gridLayout.addWidget(self.doubleSpinBox_1, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMinimum(-1e+18)
        self.doubleSpinBox_3.setMaximum(999999999999.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.BMT = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.BMT.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.BMT.setDecimals(3)
        self.BMT.setMinimum(-1e+18)
        self.BMT.setMaximum(999999999999.0)
        self.BMT.setObjectName("BMT")
        self.gridLayout.addWidget(self.BMT, 5, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(-1e+18)
        self.doubleSpinBox_2.setMaximum(999999999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.COFY = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.COFY.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.COFY.setDecimals(3)
        self.COFY.setMinimum(-1e+18)
        self.COFY.setMaximum(999999999999.0)
        self.COFY.setObjectName("COFY")
        self.gridLayout.addWidget(self.COFY, 10, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 15, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.kHeave = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.kHeave.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.kHeave.setDecimals(3)
        self.kHeave.setMinimum(-1e+18)
        self.kHeave.setMaximum(999999999999.0)
        self.kHeave.setObjectName("kHeave")
        self.gridLayout.addWidget(self.kHeave, 12, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 18, 0, 1, 1)
        self.COFX = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.COFX.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.COFX.setDecimals(3)
        self.COFX.setMinimum(-1e+18)
        self.COFX.setMaximum(999999999999.0)
        self.COFX.setObjectName("COFX")
        self.gridLayout.addWidget(self.COFX, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.BML = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.BML.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.BML.setDecimals(3)
        self.BML.setMinimum(-1e+18)
        self.BML.setMaximum(999999999999.0)
        self.BML.setObjectName("BML")
        self.gridLayout.addWidget(self.BML, 6, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 14, 0, 1, 1)
        self.waterline = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.waterline.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.waterline.setDecimals(3)
        self.waterline.setMinimum(-1e+18)
        self.waterline.setMaximum(999999999999.0)
        self.waterline.setObjectName("waterline")
        self.gridLayout.addWidget(self.waterline, 16, 1, 1, 1)
        self.disp = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.disp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.disp.setDecimals(3)
        self.disp.setMinimum(-1e+18)
        self.disp.setMaximum(999999999999.0)
        self.disp.setObjectName("disp")
        self.gridLayout.addWidget(self.disp, 18, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(widget_linhyd)
        QtCore.QMetaObject.connectSlotsByName(widget_linhyd)
        widget_linhyd.setTabOrder(self.doubleSpinBox_1, self.doubleSpinBox_2)
        widget_linhyd.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBox_3)

    def retranslateUi(self, widget_linhyd):
        widget_linhyd.setWindowTitle(QtWidgets.QApplication.translate("widget_linhyd", "Form", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("widget_linhyd", "Y - position", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("widget_linhyd", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">CoB position</span></p><p>[Defined in parent axis system]</p><p><br/></p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("widget_linhyd", "X - position", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("widget_linhyd", "BM-t (heel)", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("widget_linhyd", "<html><head/><body><br/><span style=\" font-weight:600; text-decoration: underline;\">Stability</span><br/></body></html>", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("widget_linhyd", "Z - position", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("widget_linhyd", "Waterline elevation (relative to CoB, usually positive)", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("widget_linhyd", "BM-l (trim)", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("widget_linhyd", "Displacement [kN]", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("widget_linhyd", "CoF - Y (relative to CoB)", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("widget_linhyd", "<html><head/><body><br/><span style=\" font-weight:600; text-decoration: underline;\">Heave effect</span><br/></body></html>", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("widget_linhyd", "Heave stiffness [kN/m]", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("widget_linhyd", "CoF - X (relative to CoB)", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("widget_linhyd", "<html><head/><body><br/><span style=\" font-weight:600; text-decoration: underline;\">Draft</span><br/></body></html>", None, -1))

