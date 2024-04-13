import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)
tombol=QPushButton("KLIK ANHAR")
tombol.setGeometry(50, 50, 10, 10) 
# x, y, width, height in integers

tombol.show()
sys.exit(app.exec_())