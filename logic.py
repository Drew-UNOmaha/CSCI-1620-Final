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

    def getIds(self) -> list[str]:
        return self.idList

    def updateIds(self, ids:list[str]) -> None:
        self.idList = ids

    def getVotes(self) -> dict:
        return self.votes

    def updateVotes(self, newVotes:dict):
        self.votes = newVotes

    def closeEvent(self):
        import sys
        sys.exit(0)

    def updateText(self, votes:dict, instructions:str) -> None:
        """updates labels for instructions and vote counts"""
        self.instructionLabel.setText(instructions)
        self.voteCountBianca.setText(str(votes['Bianca']))
        self.voteCountEdward.setText(str(votes['Edward']))
        self.voteCountFelicia.setText(str(votes['Felicia']))

    def updateCsv(self, votes:dict, ids:list[str]):
        with open('votes.csv','a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Voter ids'] + ids)
            writer.writerow(['Bianca',votes['Bianca']])
            writer.writerow(['Edward',votes['Edward']])
            writer.writerow(['Felicia',votes['Felicia']])


    def submit(self) -> None:
        """This is called when the submit button is pushed
        It will check the voter id and compare it to voter ids already in use
        It will also update the text in the vote counts, and the instruction label"""
        voterId = self.voterID.text()
        idList = self.getIds()
        votes = self.getVotes()

        if len(voterId) == 3 and voterId.isdigit():
            if voterId not in idList:
                idList.append(voterId)

                if self.biancaRadio.isChecked():
                    votes['Bianca'] += 1
                    self.updateVotes(votes)

                    self.updateText(votes, 'Votes successfully updated')
                elif self.edwardRadio.isChecked():
                    votes['Edward'] += 1
                    self.updateVotes(votes)

                    self.updateText(votes, 'Votes successfully updated')
                elif self.feliciaRadio.isChecked():
                    votes['Felicia'] += 1
                    self.updateVotes(votes)

                    self.updateText(votes, 'Votes successfully updated')
                else:
                    self.updateText(votes, 'Candidate not selected')
            else:
                self.updateText(votes, 'Id already used')
        else:
            self.updateText(votes, 'Id is invalid, please enter a three digit number')

        self.updateCsv(votes, idList)