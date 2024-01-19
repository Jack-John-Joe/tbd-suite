import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QTextCursor  # Import QTextCursor
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread

class Server(QObject):
    messageReceived = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 5555))
        self.server_socket.listen()

    def run(self):
        while True:
            client_socket, _ = self.server_socket.accept()
            self.clients.append(client_socket)
            client_thread = ClientThread(client_socket)
            client_thread.messageReceived.connect(self.handle_message)
            client_thread.start()

    @pyqtSlot(str)
    def handle_message(self, message):
        self.messageReceived.emit(message)

    def send_message(self, message):
        for client_socket in self.clients:
            client_socket.send(message.encode())

class ClientThread(QThread):
    messageReceived = pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if not message:
                break
            self.messageReceived.emit(message)

class CollaborativeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Collaborative Text Editor')

        self.text_edit = QTextEdit(self)
        self.code_input = QLineEdit(self)
        self.join_button = QPushButton('Join', self)
        self.join_button.clicked.connect(self.join_server)

        self.server = Server()
        self.server_thread = QThread()
        self.server.moveToThread(self.server_thread)  # Move server to separate thread
        self.server_thread.started.connect(self.server.run)
        self.server.messageReceived.connect(self.receive_message)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Enter Server Code:"))
        layout.addWidget(self.code_input)
        layout.addWidget(self.join_button)
        layout.addWidget(self.text_edit)

    def join_server(self):
        server_code = self.code_input.text()
        if server_code:
            self.server_thread.start()

    @pyqtSlot(str)
    def receive_message(self, message):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)  # Fix movePosition
        cursor.insertText(message)

def main():
    app = QApplication(sys.argv)
    editor = CollaborativeEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# note to self: TEST THE CODE HERE AND IN REALITYENGINE!!!
#    (oh my god don't forget)
    # no seriously, also make sure to fetch source!! these changes aren't gonna appear if you DON'T FETCH SOURCE!!!!!
    