from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableView, QHeaderView, QCompleter, QTableWidgetItem, \
    QTableWidget, QAbstractItemView
from PyQt5.QtCore import Qt


class CompleterView(QTableView):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setShowGrid(False)
        

class LeftRightTextCompleter(QCompleter):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__tableWidget = QTableWidget()
        self.__tableWidget.setColumnCount(2)

        self.__model = self.__tableWidget.model()
        self.setModel(self.__model)
        
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setPopup(CompleterView())
        self.setCompletionColumn(0)
        self.popup().setMinimumHeight(100)

    def addText(self, text1, text2):
        item1 = QTableWidgetItem(text1)
        item2 = QTableWidgetItem(text2)

        item1.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        item2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        item2.setForeground(QColor('#888888'))

        rowIdx = self.__tableWidget.rowCount()
        self.__tableWidget.setRowCount(rowIdx+1)
        self.__tableWidget.setItem(rowIdx, 0, item1)
        self.__tableWidget.setItem(rowIdx, 1, item2)




