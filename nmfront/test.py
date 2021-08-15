# # from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow,QSpinBox
# # import sys
# # from PyQt5 import QtCore
# # stytle="""
# # QPushButton{border-image:url(test1.png);
# # background-color:#d0e4fe;}
# # """
# # class ChangeStyle(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #     def initUI(self):
# #         self.setWindowTitle('change style')
# #         self.setGeometry(300,300,300,200)
# #
# #         self.btn=QSpinBox(self)
# #         self.btn.setMaximum(100)
# #         self.btn.setAlignment(QtCore.Qt.AlignCenter)
# #         self.btn.setProperty("value", 90)
# #         self.btn.move(100,100)
# #         # self.btn.clicked.connect(self.change_style)
# #
# #     def change_style(self):
# #
# #         self.setStyleSheet(stytle)
# #
# # #--------------------main-------------------------------
# #
# #
# # if __name__=='__main__':
# #     app=QApplication(sys.argv)
# #     demo=ChangeStyle()
# #     demo.show()
# #
# #     sys.exit(app.exec_())
# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(320, 240)
#         self.spinBox = QtWidgets.QSpinBox(Form)
#         self.spinBox.setGeometry(QtCore.QRect(80, 120, 139, 40))
#         self.spinBox.setObjectName("spinBox")
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(100, 40, 63, 22))
#         self.label.setObjectName("label")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label.setText(_translate("Form", "TextLabel"))
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog1 = QtWidgets.QDialog()
#     dialog_ui1 = Ui_Form()
#     dialog_ui1.setupUi(Dialog1)
#     Dialog1.show()
#     sys.exit(app.exec_())
import subprocess
subprocess.call("ping baidu.com",shell=True)
