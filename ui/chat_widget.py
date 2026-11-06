from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from api.worker import LunaWorker

class ChatWidget(QWidget):
    def __init__(self, client):
        super().__init__()
        
        self.client = client
        self.worker = None
                
        #Layout
        self.layout = QVBoxLayout(self)
        
        #area de sms
        self.messages = QListWidget()
        self.messages.setStyleSheet("""
            QListWidget{
                background-color: #17171d;
                color: #ffffff;
                border: none;
                font-size: 14px;
                padding: 10px;
                }
        """)
        
        #texto
        self.input = QLineEdit()
        self.input.setPlaceholderText("Digite sua mensagem...")
        self.input.setStyleSheet("""
            QLineEdit {
                background-color: #25252e;
                color: white;
                border: 1px solid #444450;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        
        ####vatar
        #self.avatar =
        #self.avatar.setStyleSheet("""""")
        
        #layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.input)
        self.input.returnPressed.connect(self.send_message)
        
        #geral
        self.layout.addWidget(self.messages)
        self.layout.addLayout(input_layout)
        
    def send_message(self):
        message = self.input.text().strip()
            
        if not message:
            return
            
        self.messages.addItem(f"Voce: {message}")
        self.messages.scrollToBottom()
        
        self.input.clear()
        self.input.setDisabled(True)
        
        self.worker = LunaWorker(self.client, message)
        
        self.worker.response_received.connect(self.show_response)
        self.worker.error_occurred.connect(self.show_error)
        
        self.worker.finished.connect(
            lambda: self.input.setDisabled(False)
        )
        self.worker.start()
        
    def show_response(self,response):
        self.messages.addItem(f"Luna: {response}")
        self.messages.scrollToBottom()
        
    def show_error(self,error):
        self.messages.addItem(f"Error: {error}")
        self.messages.scrollToBottom()
        