from PySide6 import QtWidgets

app = QtWidgets.QApplication()

central = QtWidgets.QWidget()
central_layout = QtWidgets.QVBoxLayout(central)
pane = QtWidgets.QPlainTextEdit()
central_layout.addWidget(pane)

window = QtWidgets.QMainWindow()
window.setWindowTitle("pysidetheme")
window.setCentralWidget(central)
window.show()

app.exec()
