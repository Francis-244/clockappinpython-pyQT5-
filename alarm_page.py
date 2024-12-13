from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtMultimedia import QSound
import os

class Alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("Set Alarm Time", self)
        self.set_alarm_button = QPushButton("Set Alarm", self)
        self.reset_alarm_button = QPushButton("Reset Alarm", self)
        self.alarm_time = None
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Alarm")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.set_alarm_button)
        vbox.addWidget(self.reset_alarm_button)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 40px; background-color: blue; color: white; padding: 10px;")

        self.set_alarm_button.clicked.connect(self.set_alarm)
        self.reset_alarm_button.clicked.connect(self.reset_alarm)
        self.timer.timeout.connect(self.check_alarm)
        self.timer.start(1000)

    def set_alarm(self):
        current_time = QTime.currentTime()
        self.alarm_time = current_time.addSecs(60)  # Example: 1 minute from now
        self.time_label.setText(f"Alarm set for: {self.alarm_time.toString('hh:mm:ss AP')}")

    def reset_alarm(self):
        self.alarm_time = None
        self.time_label.setText("Alarm reset.")

    def check_alarm(self):
        if self.alarm_time and QTime.currentTime() >= self.alarm_time:
            self.time_label.setText("ALARM! Wake Up!")
            self.play_beep()
            self.alarm_time = None

    def play_beep(self):
        if os.path.exists("beep.wav"):
            QSound.play("beep.wav")
        else:
            print("\a")  # Fallback: system beep
