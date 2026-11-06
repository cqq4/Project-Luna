from PySide6.QtCore import Qt
from PySide6.QtWidgets import(
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
)

from ui.title_bar import TitleBar
from ui.chat_widget import ChatWidget
from api.client import LunaClient

class LunaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #dimensoes do chat
        self.resize(1100, 700)
        self.setMinimumSize(800,600)

        ### Abre janela sem borda ###
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )

        
        central = QWidget()
        self.main_layout = QVBoxLayout(central)
        
        self.titlebar = TitleBar()
        self.client = LunaClient()
        self.chat = ChatWidget(self.client)

        #abre a barra de titulo
        self.main_layout.addWidget(self.titlebar)
        #abre o chat
        self.main_layout.addWidget(self.chat)
        
        self.setCentralWidget(central)

        ##faz a conexao com os as funcionalidades
        self.titlebar.closeRequested.connect(self.close)
        self.titlebar.minimizeRequested.connect(self.showMinimized)
        self.titlebar.maximizeRequested.connect(self.toggle_maximize)

        central.setStyleSheet(
            "background-color:17171d;"
        )    


    def toggle_maximize(self):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()