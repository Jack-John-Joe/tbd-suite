import sys
import time
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QTimer

class LoadingApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = LoadingWindow()
        self.main_window.show()

class LoadingWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Loading Reality.. This may take a while.")
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)

        self.loading_timer = QTimer(self)
        self.loading_timer.timeout.connect(self.update_loading)
        self.loading_timer.start(500)  # Update every 500 milliseconds

        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_requirements)
        self.check_timer.start(120000)  # Check requirements after 2 minutes

    def update_loading(self):
        text = self.text()
        if text.endswith("..."):
            text = "Loading"
        else:
            text += "."
        self.setText(text)

    def check_requirements(self):
        self.loading_timer.stop()
        self.check_timer.stop()

        result = QMessageBox.question(self, "Requirements Check",
                                      "Your device does not meet the minimum requirements. Check with JJJ for more info.",
                                      QMessageBox.Ok)

        if result == QMessageBox.Ok:
            sys.exit()

def main():
    app = LoadingApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
