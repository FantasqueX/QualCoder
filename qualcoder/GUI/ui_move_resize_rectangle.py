# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_move_resize_rectangle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_move_resize_rect(object):
    def setupUi(self, Dialog_move_resize_rect):
        Dialog_move_resize_rect.setObjectName("Dialog_move_resize_rect")
        Dialog_move_resize_rect.resize(532, 249)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_move_resize_rect)
        self.buttonBox.setGeometry(QtCore.QRect(290, 200, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label.setGeometry(QtCore.QRect(10, 70, 201, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_2.setGeometry(QtCore.QRect(240, 68, 201, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_3.setGeometry(QtCore.QRect(10, 136, 201, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_4.setGeometry(QtCore.QRect(237, 136, 201, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_move_horizontal = QtWidgets.QLineEdit(Dialog_move_resize_rect)
        self.lineEdit_move_horizontal.setGeometry(QtCore.QRect(10, 90, 61, 25))
        self.lineEdit_move_horizontal.setObjectName("lineEdit_move_horizontal")
        self.lineEdit_move_vetical = QtWidgets.QLineEdit(Dialog_move_resize_rect)
        self.lineEdit_move_vetical.setGeometry(QtCore.QRect(240, 88, 61, 25))
        self.lineEdit_move_vetical.setObjectName("lineEdit_move_vetical")
        self.lineEdit_resize_horizontal = QtWidgets.QLineEdit(Dialog_move_resize_rect)
        self.lineEdit_resize_horizontal.setGeometry(QtCore.QRect(10, 156, 61, 25))
        self.lineEdit_resize_horizontal.setObjectName("lineEdit_resize_horizontal")
        self.lineEdit_resize_vertical = QtWidgets.QLineEdit(Dialog_move_resize_rect)
        self.lineEdit_resize_vertical.setGeometry(QtCore.QRect(237, 156, 61, 25))
        self.lineEdit_resize_vertical.setObjectName("lineEdit_resize_vertical")
        self.label_5 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_5.setGeometry(QtCore.QRect(91, 94, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_6.setGeometry(QtCore.QRect(320, 90, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_7.setGeometry(QtCore.QRect(90, 157, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_8.setGeometry(QtCore.QRect(320, 160, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_info = QtWidgets.QLabel(Dialog_move_resize_rect)
        self.label_info.setGeometry(QtCore.QRect(8, 7, 511, 51))
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")

        self.retranslateUi(Dialog_move_resize_rect)
        self.buttonBox.accepted.connect(Dialog_move_resize_rect.accept)
        self.buttonBox.rejected.connect(Dialog_move_resize_rect.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_move_resize_rect)

    def retranslateUi(self, Dialog_move_resize_rect):
        _translate = QtCore.QCoreApplication.translate
        Dialog_move_resize_rect.setWindowTitle(_translate("Dialog_move_resize_rect", "Move and Resize"))
        self.label.setText(_translate("Dialog_move_resize_rect", "Move horizontally"))
        self.label_2.setText(_translate("Dialog_move_resize_rect", "Move vertically"))
        self.label_3.setText(_translate("Dialog_move_resize_rect", "Resize horizontally"))
        self.label_4.setText(_translate("Dialog_move_resize_rect", "Resize vertically"))
        self.label_5.setText(_translate("Dialog_move_resize_rect", "pixels"))
        self.label_6.setText(_translate("Dialog_move_resize_rect", "pixels"))
        self.label_7.setText(_translate("Dialog_move_resize_rect", "pixels"))
        self.label_8.setText(_translate("Dialog_move_resize_rect", "pixels"))
        self.label_info.setText(_translate("Dialog_move_resize_rect", "Enter the amount of change required. e.g. 10 for 10 pixels or -10 for a reduction of 10 pixels."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_move_resize_rect = QtWidgets.QDialog()
    ui = Ui_Dialog_move_resize_rect()
    ui.setupUi(Dialog_move_resize_rect)
    Dialog_move_resize_rect.show()
    sys.exit(app.exec_())
