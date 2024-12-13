from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, QDate, Qt

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Clock")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 40px; background-color: blue; color: white; padding: 10px;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        self.time_label.setText(f"{current_date.toString('dddd, MMMM d, yyyy')}\n{current_time.toString('hh:mm:ss AP')}")
