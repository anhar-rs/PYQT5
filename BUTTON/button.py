import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# Container
wg = QWidget()
wg.setWindowTitle("Exit Button Example")

# Button setup
tombol = QPushButton("KLIK ANHAR", wg)
tombol.setGeometry(50, 50, 100, 50)  # Adjusted width and height for better visibility
tombol_enter=QPushButton("ENTER", wg)
label=QLabel(wg)
label.setGeometry(50, 20, 100, 50) #
tombol_enter.setGeometry(50, 100, 100, 50)
wg.show()
# Function to exit
def exit_function():
    sys.exit()
def enter_function():
    label.setText("tombol enter di klik")
    
tombol.clicked.connect(exit_function)
tombol_enter.clicked.connect(enter_function)
sys.exit(app.exec_())