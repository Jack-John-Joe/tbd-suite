import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window transparency
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Widgets
        self.title_label = QLabel('real-todo', self)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")

        self.task_input = QLineEdit(self)
        self.task_button = QPushButton('Add Task', self)
        self.task_button.clicked.connect(self.addTask)

        self.task_list = QLabel(self)
        self.task_list.setStyleSheet("color: white;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.task_input)
        layout.addWidget(self.task_button)
        layout.addWidget(self.task_list)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set background color to black
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('real-todo')
        self.show()

    def addTask(self):
        task = self.task_input.text()
        if task:
            current_tasks = self.task_list.text()
            new_tasks = f"{current_tasks}\n- {task}"
            self.task_list.setText(new_tasks)
            self.task_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    sys.exit(app.exec_())
