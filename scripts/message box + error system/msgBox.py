# Here a simple system according a choice to the user :

from PyQt5.QtWidgets import QMessageBox

class FreeWill(QMessageBox):
    def __init__(self, parent, message, action):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Confirmation")
        self.setText(message)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        self.action = action

    def exec_and_call_action(self):
        result = self.exec_()
        if result == QMessageBox.Yes:
            self.action()
        elif result == QMessageBox.No:
            pass

