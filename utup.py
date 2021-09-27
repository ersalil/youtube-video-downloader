
import sys
import time
import speedtest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication

from ut import Ui_MainWindow
from pytube import YouTube

global role

class Ui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Fastest YouTube Video Downloader")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        self.ui.pushButton_2.clicked.connect(self.updatewin)
        self.ui.pushButton.clicked.connect(self.browse)
        self.ui.radioButton.toggled.connect(self.on)
        self.ui.radioButton_2.toggled.connect(self.chk)
        self.ui.pushButton_3.clicked.connect(self.download)
        self.ui.comboBox.currentIndexChanged.connect(self.itagv)
        self.ui.progressBar.setValue(0)
        print("default index" , self.ui.comboBox.currentIndex())
        self.ui.role = 22

    def updatewin(self):
        link = f"{self.ui.lineEdit.text()}"
        print(link)
        try:
            self.yt = YouTube(link)
            if self.yt.title == "":
                self.ui.textBrowser.setText("Please enter the url")
            else:
                self.ui.textBrowser.setText(self.yt.title)
                # self.label_8.setPixmap(self.yt.thumbnail_url)
                # self.label_8.adjustSize()
                print(self.yt.title)
        except:
            self.ui.textBrowser.setText("Envalid URL")

    def browse(self):
        self.ui.lineEdit_2.setText(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        print(self.ui.lineEdit_2.text())

    def download(self):
        self.ui.progressBar.setFormat("Extracting Youtube video...")
        self.ui.label_6.setText("Don't close the Window, Downloading is in Process")
        self.ui.label_6.adjustSize()
        for i in range(95):
            time.sleep(0.02)
            self.ui.progressBar.setValue(i)
        self.ui.label_9.setText("Video Extraction Completed!")
        print(self.role)
        print(self.yt.streams.get_by_itag(self.role))
        self.stream = self.yt.streams.get_by_itag(self.role)
        self.ui.progressBar.setFormat("Downloading Extracted File...")
        self.ui.label_9.setText("Downloading Speed Depends upon the Internet!")
        self.stream.download(self.ui.lineEdit_2.text())
        print(self.stream.filesize)
        self.ui.progressBar.setValue(100)
        if self.ui.progressBar.value() == 100:
            self.ui.label_9.setText("Thank You for Using this Software")
            self.ui.progressBar.setFormat("Video Downloaded!")
        else:
            self.ui.label_9.setText("Please Check Your Internet Connection!")
            self.ui.progressBar.setFormat("Downloading Error!")

        #self.yt.register_on_progress_callback(progress_bar)

    def itagv(self):
        if int(self.ui.comboBox.currentIndex()) == 0:
            self.role = 137
        elif int(self.ui.comboBox.currentIndex()) == 1:
            self.role = 136
        elif int(self.ui.comboBox.currentIndex()) == 2:
            self.role = 135
        elif int(self.ui.comboBox.currentIndex()) == 3:
            self.role = 134
        elif int(self.ui.comboBox.currentIndex()) == 4:
            self.role = 133
        elif int(self.ui.comboBox.currentIndex()) == 5:
            self.role = 160
        elif int(self.ui.comboBox.currentIndex()) == 6:
            self.role = 140
        else:
            self.ui.label_6.setText("Please Select a Valid option")
        print(self.role)
    # def progress_bar(stream, chunk, bytes_remaining):
    #     current = int((stream.filesize - bytes_remaining)/stream.filesize)
    #     percent = current * 100
    #     self.progressBar.setValue(percent)

    def on(self, o):
        if o:
            self.__init__()
            self.show()
        else:
            self.close()

    def chk(self, c):
        if c:
            try:
                st = speedtest.Speedtest()
                down = (st.download()/1000000)
                down = format(down, '.3f')
                self.ui.label_7.setText(down)
                self.ui.radioButton_2.setText("Check Internet Speed")
            except:
                self.ui.label_7.setText("No Internet")
                self.ui.label_7.adjustSize()
            self.ui.radioButton_2.setText("Check Internet Speed")
        else:
            self.ui.radioButton_2.setText("Check Internet Speed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())