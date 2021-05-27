
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader



class windozmain(QMainWindow):
    def __init__(self):
        super(windozmain, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.bt_1.clicked.connect(self.translate)


    def translate(self):
        f = open('translate.txt')
        big_text = f.read()
        parts = big_text.split('\n')
        words = []
        for word in parts:
            words.append(word)
        if self.ui.rb_2.isChecked():
            text = self.ui.tb_1.text()
            for i in range(len(words)):
                if words[i] == text:
                    self.ui.tb_2.setText(str(words[i - 1]))

        elif self.ui.rb_1.isChecked():
            text = self.ui.tb_1.text()
            for i in range(len(words)):
                if words[i] == text:
                    self.ui.tb_2.setText(str(words[i + 1]))


if __name__ == "__main__":
    app = QApplication([])
    window = windozmain()
    sys.exit(app.exec_())
