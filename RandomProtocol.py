# Программа для рандомной генерации номера протокола
import random
from interface import Ui_MainWindow
import sys

from PySide2.QtWidgets import QMainWindow, QApplication

class Application(QMainWindow, Ui_MainWindow):
    """GUI генерация рандомного номера протокола"""
    def __init__(self):
        """Инициализация рамки"""
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gen_protocol)

    def gen_protocol(self):
        ban_list = self.open_list()
        ban_list = self.new_number(ban_list)
        self.write_in_list(ban_list)

    def open_list(self):
        """Открытие ранее сохраненных номеров протокола"""
        ban_list = []
        output_string = ""
        numbers_list = open('ProtocolNumbers.txt', 'r')
        ban_list += numbers_list
        numbers_list.close()
        for num in ban_list:
            output_string += num
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(output_string)
        return ban_list

    def new_number(self, ban_list):
        """Генерация нового номера протокола"""
        final_number = ""
        while True:
            number1 = str(random.randint(1000, 99999))
            number2 = str(random.randint(100000, 999999))
            final_number = "441-" + number1 + "-2020-" + number2
            if final_number not in ban_list:
                break
        self.lineEdit.clear()
        self.lineEdit.setText(final_number)
        final_number += "\n"
        ban_list.append(final_number)
        return ban_list

    def write_in_list(self, ban_list):
        """Запись нового номера протокола в файл"""
        number_list = open('ProtocolNumbers.txt', 'w')
        output_string = ""
        for number in ban_list:
            number_list.write(number)
            output_string += number
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(output_string)

def main():
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    window.open_list()
    app.exec_()

if __name__ == "__main__":
    main()

