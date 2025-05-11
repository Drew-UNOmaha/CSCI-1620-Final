from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_VoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submitButton.clicked.connect(lambda: self.submit())
        self.exitButton.clicked.connect(lambda: self.closeEvent())

        self.votes = {'Bianca':0,'Edward':0,'Felicia':0}
        self.idList = []

    def getIds(self) -> list[int]:
        return self.idList

    def updateIds(self, ids:list[int]) -> None:
        self.idList = ids

    def closeEvent(self):
        import sys
        sys.exit(0)

    def submit(self) -> None:
        '''This is called when the submit button is pushed
        It will check the voter id and compare it to voter ids already in use
        It will also update the text in the vote counts, and the instruction label'''
        id = self.voterID.text()
        idList = self.getIds()

        if id not in idList:
            idList.append(id)


