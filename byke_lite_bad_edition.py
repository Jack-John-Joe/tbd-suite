import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class TextAdventure(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Game variables
        self.player_name = ""
        self.location = 0  # Start location

    def init_ui(self):
        self.setWindowTitle('E-Bike Commute Adventure')

        self.text_label = QLabel(self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.button_layout = QVBoxLayout()

        self.next_button = QPushButton('Start Adventure', self)
        self.next_button.clicked.connect(self.next_scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_label)
        layout.addLayout(self.button_layout)
        layout.addWidget(self.next_button)

        self.show_intro()

    def show_intro(self):
        self.text_label.setText("Welcome to E-Bike Commute Adventure!\n"
                                "You are about to embark on a long commute to work.\n"
                                "Are you ready to start your journey?")
        self.clear_buttons()
        self.add_button("Yes", self.get_player_name)
        self.add_button("No", self.close)

    def get_player_name(self):
        self.player_name, ok = PlayerNameDialog.get_player_name(self)
        if ok:
            self.next_scene()

    def next_scene(self):
        self.location += 1

        if self.location == 1:
            self.scene1()

    def scene1(self):
        self.text_label.setText(f"Hello {self.player_name}!\n"
                                "You hop on your e-bike and start your journey.\n"
                                "As you ride through the city, you encounter a friendly stranger.\n"
                                "What do you want to do?")
        self.clear_buttons()
        self.add_button("Greet the stranger", self.greet_stranger)
        self.add_button("Ignore and continue riding", self.continue_riding)

    def greet_stranger(self):
        self.text_label.setText("You greet the stranger, and they respond warmly.\n"
                                "They offer you a shortcut to avoid traffic.\n"
                                "Do you want to take the shortcut?")
        self.clear_buttons()
        self.add_button("Take the shortcut", self.take_shortcut)
        self.add_button("Decline and continue riding", self.continue_riding)

    def continue_riding(self):
        self.text_label.setText("You continue riding your e-bike through the city.\n"
                                "The streets are bustling with activity.\n"
                                "What will you do next?")
        self.clear_buttons()
        self.add_button("Explore a new route", self.explore_route)
        self.add_button("Keep riding towards work", self.head_to_work)

    def take_shortcut(self):
        self.text_label.setText("You decide to take the shortcut recommended by the stranger.\n"
                                "The route is scenic, and you enjoy the ride.\n"
                                "You arrive at work early. Congratulations!")
        self.clear_buttons()
        self.add_button("Play again", self.show_intro)

    def explore_route(self):
        self.text_label.setText("You decide to explore a new route through the city.\n"
                                "You discover interesting places and meet new people.\n"
                                "It's a delightful journey. You arrive at work with a smile!")
        self.clear_buttons()
        self.add_button("Play again", self.show_intro)

    def head_to_work(self):
        self.text_label.setText("You decide to stick to the usual route and head straight to work.\n"
                                "As you approach the office, you feel accomplished.\n"
                                "You arrive at work on time. Well done!")
        self.clear_buttons()
        self.add_button("Play again", self.show_intro)

    def clear_buttons(self):
        for i in reversed(range(self.button_layout.count())):
            self.button_layout.itemAt(i).widget().setParent(None)

    def add_button(self, text, callback):
        button = QPushButton(text, self)
        button.clicked.connect(callback)
        self.button_layout.addWidget(button)


class PlayerNameDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Enter Your Name')

        label = QLabel('Enter your name:', self)

        self.name_input = QLineEdit(self)

        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.name_input)
        layout.addWidget(ok_button)

    def accept(self):
        self.player_name = self.name_input.text()
        self.close()

    @staticmethod
    def get_player_name(parent):
        dialog = PlayerNameDialog()
        result = dialog.exec_()
        return dialog.player_name, result == QDialog.Accepted


def main():
    app = QApplication(sys.argv)
    game = TextAdventure()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
