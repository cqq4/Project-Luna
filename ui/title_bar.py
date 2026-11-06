from PySide6.QtCore import Signal
from PySide6.QtWidgets import(
    QWidget,
    QPushButton,
    QHBoxLayout,
)


class TitleBar(QWidget):
    closeRequested = Signal()
    minimizeRequested = Signal()
    maximizeRequested = Signal()

    def __init__(self):
        super().__init__()
        self.layout= QHBoxLayout(self)

        self.layout.setContentsMargins(12,10,12,10)
        self.layout.setSpacing(8)

        ## Botão fechar ##
        self.close_button = QPushButton()
        self.close_button.setFixedSize(12, 12)

        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #ff5f57;
                border: 1px solid #e0443e;
                border-radius: 6px;
            }    
            
            QPushButton:hover {
                background-color: #ff7b73;
            }
        """)

        ## Botão minimizar ##
        self.min_button = QPushButton()
        self.min_button.setFixedSize(12, 12)

        self.min_button.setStyleSheet("""
            QPushButton {
                background-color: #ffff00;
                border: 1px solid #d6b800;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #fff176;
            }   
        """)
        

        ## Botão maximizar ##
        self.max_button = QPushButton()
        self.max_button.setFixedSize(12, 12)

        self.max_button.setStyleSheet("""
            QPushButton {
                background-color: #008000;
                border: 1px solid #006400;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #00a000;
            }
        """)
        
        #layout botoes
        self.layout.addWidget(self.close_button)
        self.layout.addWidget(self.min_button)
        self.layout.addWidget(self.max_button)
        self.layout.addStretch()
        
        
        ##conexao dos botoess###
        self.close_button.clicked.connect(
            self.closeRequested.emit
        )
        
        self.min_button.clicked.connect(
            self.minimizeRequested.emit
        )
       
        self.max_button.clicked.connect(
            self.maximizeRequested.emit
        )

        

