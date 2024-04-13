import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)
wg=QWidget()

lineedit=QLineEdit(wg)
lineedit.setGeometry(100,100,500,80)

tombol_enter=QPushButton("enter",wg)
tombol_enter.setGeometry(512,190,90,50)

label=QLabel(wg)
label.setGeometry(100, 200, 600, 80)
def keyboard_enter():
    text = lineedit.text()  # Mengambil teks dari LineEdit
    label.setText(text)  # Menampilkan teks pada label

# Menghubungkan signal ke slot
lineedit.returnPressed.connect(keyboard_enter)  # Menghubungkan tekanan tombol enter pada LineEdit ke fungsi keyboard_enter
tombol_enter.clicked.connect(keyboard_enter)  # Menghubungkan klik pada tombol ke fungsi keyboard_enter

# Menampilkan widget
wg.show()

# Memulai loop aplikasi
sys.exit(app.exec_())