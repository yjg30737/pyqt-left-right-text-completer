# pyqt-left-right-text-completer
PyQt Left text, right text completer. Left text is major target of search.

## Detailed Description

QCompleter's popup widget is gridless QTableView. Right text is gray colored.

You can add a new pair of text to search with ```addText(text1, text2)```. 

Text1 is left text, text2 is right text.

This completer is case insensitive as default.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-left-right-text-completer`

## Example
Code Example
```python
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication

from pyqt_left_right_text_completer import LeftRightTextCompleter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        searchBar = QLineEdit()
        completer = LeftRightTextCompleter()
        for i in range(1, 128):
            completer.addText(chr(i), f'{i}') # chr(i) is left text, f'{i} is right text.
        searchBar.setCompleter(completer)
        self.setCentralWidget(searchBar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/145187262-498b2862-6af7-4f6c-b8ef-cea3f19974ec.png)
