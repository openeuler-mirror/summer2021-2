import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,QMessageBox
from nmfront.resource_set import Ui_sysyemMonitor
from nmfront.about import nmSettingsAbout
from nmfront.utils import read_yaml,write_yaml,read_file
from nmfront.nm_qss import nmqss
class nmUi(QMainWindow):
    def __init__(self,path):
        QMainWindow.__init__(self)
        self.config_path=path
        self.main_ui = Ui_sysyemMonitor()
        self.main_ui.setupUi(self)
        self.get_config()
        self.get_default_value()
        self.center()
        self.main_ui.pushButtonOk.clicked.connect(self.nm_set_handler)
        self.main_ui.pushButtonCancel.clicked.connect(self.nm_cancel_handler)
        self.setStyleSheet(nmqss)
    def get_default_value(self):
        self.main_ui.memspinBox.setProperty("value", self.nmconfig["MEM_ALARM_THRESHOLD"])
        self.main_ui.cpuspinBox.setProperty("value", self.nmconfig["CPU_ALARM_THRESHOLD"])
        self.main_ui.diskspinBox.setProperty("value", self.nmconfig["DISK_LARM_THRESHOLD"])

    def get_config(self):
        self.nmconfig=read_yaml(self.config_path)

    def set_config(self):
        write_yaml(self.config_path,self.nmconfig)
    def restart_back(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def nm_set_handler(self):
        self.nmconfig["CPU_ALARM_THRESHOLD"]=self.main_ui.cpuspinBox.value()
        self.nmconfig["MEM_ALARM_THRESHOLD"]=self.main_ui.memspinBox.value()
        self.nmconfig["DISK_LARM_THRESHOLD"]=self.main_ui.diskspinBox.value()
        self.set_config()
        QMessageBox.information(self,'Info','Settings are in effect')

    def nm_cancel_handler(self):
        self.get_default_value()
        QMessageBox.information(self, 'Info', 'Settings restored')




def main():
    app = QApplication(sys.argv)
    nmui = nmUi('/home/openeuler/Desktop/nm/nmfront/nmconfig.yaml')
    bttn = nmui.main_ui.pushButtonAbout
    nm = nmSettingsAbout()
    bttn.clicked.connect(nm.show)
    nmui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
