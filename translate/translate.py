# Mengimpor modul os untuk interaksi dengan sistem operasi
import os

# Mengimpor modul random untuk penggunaan fungsi acak
import random

# Mengimpor modul sys untuk akses ke argumen baris perintah dan interaksi sistem
import sys

# Mengimpor semua fungsi dan kelas dari modul deep_translator untuk penerjemahan teks
from deep_translator import *

# Mengimpor modul gTTS (Google Text-to-Speech) untuk mengonversi teks menjadi suara
from gtts import gTTS

# Mengimpor modul-modul yang diperlukan dari PyQt5 untuk membuat antarmuka pengguna
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Mendefinisikan kelas Translator yang merupakan subclass dari QWidget, menyediakan fungsi dasar jendela
class Translator(QWidget):
    # Fungsi konstruktor untuk inisialisasi objek Translator
    def __init__(self):
        super().__init__()  # Memanggil konstruktor kelas dasar QWidget
        self.init_ui()  # Memanggil fungsi untuk mengatur UI

    # Fungsi untuk mengatur tampilan antarmuka pengguna
    def init_ui(self):
        vb = QVBoxLayout()  # Membuat layout vertikal
        self.setLayout(vb)  # Menetapkan layout vertikal ke widget

        self.insert_text = QTextEdit()  # Membuat widget teks untuk input pengguna
        vb.addWidget(self.insert_text)  # Menambahkan widget input teks ke layout

        self.show_translit = QTextEdit()  # Membuat widget teks untuk menampilkan terjemahan
        vb.addWidget(self.show_translit)  # Menambahkan widget tampilan teks ke layout

        self.translate_btn = QPushButton("Terjemahan")  # Membuat tombol untuk penerjemahan
        vb.addWidget(self.translate_btn)  # Menambahkan tombol ke layout
        self.translate_btn.clicked.connect(self.translate_text)  # Menghubungkan tombol dengan fungsi penerjemahan

        self.play_sound = QPushButton("SOUND")  # Membuat tombol untuk memainkan suara
        vb.addWidget(self.play_sound)  # Menambahkan tombol ke layout
        self.play_sound.clicked.connect(self.play_translation_sound)  # Menghubungkan tombol dengan fungsi pemutaran suara

        self.combo = QComboBox()  # Membuat dropdown menu untuk pilihan bahasa
        languages = ["English", "Arabic", "French", "Indonesian", "Japanese", "Korean", "Thai"]  # Daftar bahasa
        self.combo.addItems(languages)  # Menambahkan daftar bahasa ke dropdown menu
        self.combo.setEditable(True)  # Mengizinkan pengeditan teks di dropdown
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)  # Menyetel perataan teks ke tengah
        vb.addWidget(self.combo)  # Menambahkan dropdown menu ke layout

        self.target = {"Arabic": "ar", "English": "en", "French": "fr", "Indonesian": "id", "Japanese": "ja", "Korean": "ko", "Thai": "th"}  # Peta bahasa ke kode mereka

    # Fungsi untuk menerjemahkan teks
    def translate_text(self):
        target_lang = self.target[self.combo.currentText()]  # Mendapatkan kode bahasa target dari pilihan combo
        source_text = self.insert_text.toPlainText()  # Mengambil teks dari input pengguna
        translated_text = GoogleTranslator(source="auto", target=target_lang).translate(source_text)  # Menerjemahkan teks
        self.show_translit.setPlainText(translated_text)  # Menampilkan teks yang telah diterjemahkan

    # Fungsi untuk memutar suara dari teks yang diterjemahkan
    def play_translation_sound(self):
        translated_text = self.show_translit.toPlainText()  # Mengambil teks terjemahan
        tts = gTTS(text=translated_text, lang=self.target[self.combo.currentText()])  # Membuat objek gTTS
        tts.save("temp.mp3")  # Menyimpan file suara sebagai mp3
        os.system("start temp.mp3")  # Memutar file mp3 menggunakan pemutar default

# Fungsi utama yang menjalankan aplikasi
def main():
    app = QApplication(sys.argv)  # Membuat instance aplikasi PyQt5
    gui = Translator()  # Membuat instance dari kelas Translator
    gui.setGeometry(100, 100, 800, 600)  # Menetapkan geometri jendela
    gui.setWindowTitle("APLIKASI TERJEMAHAN ANHAR")  # Menetapkan judul jendela
    gui.show()  # Menampilkan jendela
    sys.exit(app.exec_())  # Menjalankan loop acara dan keluar ketika jendela ditutup

if __name__ == '__main__':
    main()  # Memanggil fungsi main jika script dijalankan sebagai program utama
