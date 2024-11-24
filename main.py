from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow



app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

 
NOTES = {
    "Купи хліба":{
        "текст": "Не забудь купити хліба за 30грн"
        "теги": ["покупка", "хліб"]
    }

}






win.show()
app.exec()