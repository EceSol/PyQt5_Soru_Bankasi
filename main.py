import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.uic import loadUi

def get_ui_path(filename):
    return os.path.join(os.path.dirname(__file__), "ui", filename)



class SoruEklemeEkrani(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(get_ui_path("soru_ekleme.ui"), self)
        self.btnEkle.clicked.connect(self.soru_ekle)
        self.btnKaydet.clicked.connect(self.kaydet)

        self.soruListesi = []

    def soru_ekle(self):
        soru = self.textSoru.toPlainText()
        cevaplar = [
            self.cevap1.text(),
            self.cevap2.text(),
            self.cevap3.text(),
            self.cevap4.text(),
            self.cevap5.text()
        ]
        dogru_index = -1
        for i, radio in enumerate([self.radio1, self.radio2, self.radio3, self.radio4, self.radio5]):
            if radio.isChecked():
                dogru_index = i
                break

        if soru and all(cevaplar) and dogru_index != -1:
            self.soruListesi.append({
                "soru": soru,
                "cevaplar": cevaplar,
                "dogru": dogru_index
            })
            self.textSoru.clear()
            for lineEdit in [self.cevap1, self.cevap2, self.cevap3, self.cevap4, self.cevap5]:
                lineEdit.clear()
            for radio in [self.radio1, self.radio2, self.radio3, self.radio4, self.radio5]:
                radio.setChecked(False)

    def kaydet(self):
        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "Text Dosyaları (*.txt)")
        if dosya_adi:
            with open(dosya_adi, "w", encoding="utf-8") as f:
                for s in self.soruListesi:
                    f.write(f"Soru: {s['soru']}\n")
                    for i, cev in enumerate(s['cevaplar']):
                        dogru_mu = " (Doğru)" if i == s['dogru'] else ""
                        f.write(f"  {chr(65+i)}. {cev}{dogru_mu}\n")
                    f.write("\n")

class SoruSecmeEkrani(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(get_ui_path("soru_yazdirma.ui"), self)
        self.btnSec.clicked.connect(self.dosya_sec)
        self.btnYazdir.clicked.connect(self.yazdir)

        self.icerik = ""

    def dosya_sec(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Dosya Seç", "", "Text Dosyaları (*.txt)")
        if dosya_adi:
            with open(dosya_adi, "r", encoding="utf-8") as f:
                self.icerik = f.read()
                self.textAlan.setPlainText(self.icerik)

    def yazdir(self):
        # Buraya yazıcıya gönderme veya PDF yapma özelliği eklenebilir
        print("Yazdırılıyor...")
        print(self.icerik)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaSayfa()
    pencere.show()
    sys.exit(app.exec_())
