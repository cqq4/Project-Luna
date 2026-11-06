
import sys

from PySide6.QtWidgets import QApplication
from window import LunaWindow

app = QApplication(sys.argv)

window = LunaWindow()
window.show()
sys.exit(app.exec())
