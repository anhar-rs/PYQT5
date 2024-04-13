import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

pp=QApplication(sys.argv)
wg=QWidget()
textedit=QTextEdit(wg)
textedit.setGeometry(10,10,800,600)
slider=QSlider(wg)
slider.setMinimum(1)  # Set the minimum value of the slider to 1
slider.setMaximum(100)
slider.setOrientation(Qt.Horizontal)
slider.setGeometry(840,10,50,50)
label=QLabel(wg)
label.setGeometry(840,30,50,50)
label.setText("font")
def font_size():
    val=slider.value()
    font=QFont("Time",val)
    textedit.setFont(font)
    label.setText("font:"+str(val))
slider.valueChanged.connect(font_size)
wg.show()
sys.exit(pp.exec_())

