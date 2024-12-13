import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QWidget
from clock_page import Clock
from stopwatch_page import Stopwatch
from timer_page import Timer
from alarm_page import Alarm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock, Timer, Stopwatch, and Alarm")

        self.stack = QStackedWidget()
        self.clock = Clock()
        self.stopwatch = Stopwatch()
        self.timer = Timer()
        self.alarm = Alarm()

        self.stack.addWidget(self.clock)
        self.stack.addWidget(self.stopwatch)
        self.stack.addWidget(self.timer)
        self.stack.addWidget(self.alarm)

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        clock_button = QPushButton("Clock")
        stopwatch_button = QPushButton("Stopwatch")
        timer_button = QPushButton("Timer")
        alarm_button = QPushButton("Alarm")

        button_layout.addWidget(clock_button)
        button_layout.addWidget(stopwatch_button)
        button_layout.addWidget(timer_button)
        button_layout.addWidget(alarm_button)

        clock_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.clock))
        stopwatch_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.stopwatch))
        timer_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.timer))
        alarm_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.alarm))

        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
