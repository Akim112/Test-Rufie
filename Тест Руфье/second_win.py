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
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.h_line = QHBoxLayout() 
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_timer = QLabel(txt_timer)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_hintage = QLineEdit(txt_hintage)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.txt_name,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hintname,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hintage,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_starttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_starttest2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_starttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest2,alignment=Qt.AlignLeft)
        self.l_line.addwidget(self.txt_hinttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_sendresults,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.txt_timer,alignment=Qt.AlignCenter)
        self.h_line.addWidget(self.l_line)
        self.h_line.addWidget(self.r_line)
        second_win.setLayout(self.h_line)
    def connects(self):
        self.txt_sendresults.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinWin()

        
    