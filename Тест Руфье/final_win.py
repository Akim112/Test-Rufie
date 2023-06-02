#final_win.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
class TestWin(QtWidget):
    def __init__(self):
        super()__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.line = QVBoxLayout()
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.line.addWidget(self.txt_index,aligment=Qt.AlignCenter)
        self.line.addWidget(self.txt_workheart,aligment=Qt.AlignCenter)
        final_win.setLayout(self.line)
