from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog

from ui import Ui_MainWindow
import json


app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

 
NOTES = {
    "Купи хліба":{
        "текст": "Не забудь купити хліба за 30грн",
        "теги": ["покупка", "хліб"]
    }

}


with open("notes_data.json", "r", encoding='UTF-8') as file:
    NOTES = json.load(file)

ui.Notes_list.addItems(NOTES)

def show_note():
    note_name = ui.Notes_list.selectedItems()[0].text()
    note = NOTES[note_name]
    ui.textEdit.setText(note["текст"])
    ui.tags_list.clear()
    ui.tags_list.addItems(note['теги'])

ui.Notes_list.itemClicked.connect(show_note)


def add_note():
    note_name, ok = QInputDialog.getText(
        win, "Додати нотатку", "Назва Нотатки:"
    )
    if ok:
        NOTES[note_name] = {
            "текст": "",
            "теги":[]
        }
        ui.Notes_list.addItem(note_name)

ui.btn_create_note.clicked.connect(add_note)


def save_note():
    if ui.Notes_list.selectedItems():
        note_name = ui.Notes_list.currentItem().text()
        note_text = ui.textEdit.toPlainText()

        NOTES[note_name] = {
           "текст": note_text,
            "теги":[] 
        }

        with open("notes_data.json", "w", encoding="UTF-8") as file:
            json.dump(NOTES, file)
            
ui.btn_save_note.clicked.connect(save_note)

win.show()
app.exec()