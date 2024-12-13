from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtMultimedia import QSound
import os

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:01:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.timer = QTimer(self)
        self.countdown_time = QTime(0, 1, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Timer")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 40px; background-color: blue; color: white; padding: 10px;")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()

    def update_display(self):
        self.countdown_time = self.countdown_time.addSecs(-1)
        self.time_label.setText(self.countdown_time.toString("hh:mm:ss"))

        if self.countdown_time == QTime(0, 0, 0):
            self.timer.stop()
            self.play_beep()

    def play_beep(self):
        if os.path.exists("beep.wav"):
            QSound.play("beep.wav")
        else:
            print("\a")  # Fallback: system beep
