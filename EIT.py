#-*- coding: utf-8 -*-
'''
Created on May 12, 2017

@author: Aradina
'''
from design import Ui_MainWindow
from esipy import EsiClient, App
import json
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap
import urllib.request

esiApp = App.create('https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility')
esi_client = EsiClient()

class eitMain(QMainWindow):
    def __init__(self):
        super(eitMain, self).__init__()
                
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchBtn.clicked.connect(self.charSearch)
        self.ui.actionExit.triggered.connect(QApplication.quit)
        
    def charSearch(self):
        self.charName = self.ui.charSearch.text()
        esiFunction.charIntelSearch(self, eitMain)
        
    def noResults(self):
        noResults = QMessageBox()
        noResults.setIcon(QMessageBox.Information)
        noResults.setText("No Results Found.")
        noResults.setInformativeText("Search must be exact.\n\nCase Sensitive.")
        noResults.setStandardButtons(QMessageBox.Ok)
        noResults.setWindowTitle("Error")
        noResults.exec_()
        self.ui.searchBtn.clicked.connect(self.charSearch)
        
    def awkward(self):
        awkward = QMessageBox()
        awkward.setText("Awkward..")
        awkward.setWindowTitle("Baka")
        awkward.addButton(QPushButton('L-lewd'), QMessageBox.NoRole)
        awkward.exec_()
        
class esiFunction():
    def charIntelSearch(self, eitMain):
        charSearch = esiApp.op['get_search'](
            categories = 'character',
            search = self.charName,
            strict = 'true'
            )
        charIDGet = esi_client.request(charSearch)
        self.charIDs = json.loads(charIDGet.raw)
        if 'character' not in self.charIDs:
            eitMain().noResults()
        else:
            esiFunction.charIntSucess(self, eitMain)
    def charIntSucess(self, eitMain):
        charIDs = self.charIDs
        charID = str(charIDs['character'])
        charID = charID.strip("[]")
        charID = int(charID)
        charSheetGet = esiApp.op['get_characters_character_id'](
            character_id = charID
            )
        charSheet = esi_client.request(charSheetGet)
        characterSheet = json.loads(charSheet.raw)
        charName = characterSheet['name']
        charBio = characterSheet['description']
        securityStatus = characterSheet['security_status']
        securityStatus = round(securityStatus, 2)
        corpID = str(characterSheet['corporation_id'])
        
        corpDetails = esiApp.op['get_corporations_corporation_id'](
            corporation_id = corpID
            )
        corpNameGet = esi_client.request(corpDetails)
        corpSheet = json.loads(corpNameGet.raw)
        corpName = corpSheet['corporation_name']
        corpDescription = corpSheet['corporation_description']
        corpTicker = corpSheet['ticker']
        corpMemberCount = corpSheet['member_count']
        corpCeo = corpSheet['ceo_id']
        corpCeoName = esiApp.op['get_characters_character_id'](
            character_id = corpCeo
            )
        corpCEOWords = esi_client.request(corpCeoName)
        corpCeoObtainment = json.loads(corpCEOWords.raw)
        corpCEO = corpCeoObtainment['name']
        if 'alliance_id' in corpSheet:
            allianceID = corpSheet['alliance_id']
            allianceimgURL = "https://imageserver.eveonline.com/Alliance/{}_128.png".format( allianceID )
            allianceurl = urllib.request.urlopen(allianceimgURL).read()
            pixmapAlliance = QPixmap()
            pixmapAlliance.loadFromData(allianceurl)
            self.ui.allianceLogo.setPixmap(pixmapAlliance)
            self.ui.allianceLogo_2.setPixmap(pixmapAlliance)
            
        charimgURL = "https://imageserver.eveonline.com/Character/{}_128.jpg".format( charID )
        charurl = urllib.request.urlopen(charimgURL).read()
        pixmapChar = QPixmap()
        pixmapChar.loadFromData(charurl)
        self.ui.charLogo.setPixmap(pixmapChar)
        
        corpimgURL = "https://imageserver.eveonline.com/Corporation/{}_128.png".format( corpID )
        corpurl = urllib.request.urlopen(corpimgURL).read()
        pixmapCorp = QPixmap()
        pixmapCorp.loadFromData(corpurl)
        self.ui.corpLogo.setPixmap(pixmapCorp)
        self.ui.corpLogo_2.setPixmap(pixmapCorp)
        
        if 'Tsao Aubbes' in charName:
            eitMain().awkward()
        self.ui.charName.setText('Name: '+self.charName)
        self.ui.charName_2.setText('Name: '+self.charName)
        self.ui.corpCeo.setText('CEO: '+corpCEO)
        self.ui.corpName.setText('Corporation Name: '+corpName+' : '+corpTicker)
        self.ui.corpName_2.setText('Corporation Name: '+corpName+' : '+corpTicker)
        self.ui.corpMembers.setText('Member Count: '+str(corpMemberCount))
        self.ui.corpMembers_2.setText('Member Count: '+str(corpMemberCount))
        """
        if charID == corpCeo:
            print("CEO")
        else:
            corpCeoGet = self.esiApp.op['get_characters_character_id'](
                character_id = corpCeo
                )
            corpCeoGetter = self.esi_client.request(corpCeoGet)
            corpCeoOther = json.loads(corpCeoGetter.raw)
            corpCeoOther = corpCeoOther['name']
            print(corpCeoOther)
        """
        self.ui.charBio.setText(charBio)
        self.ui.charBio_2.setText(charBio)
        self.ui.charBio.setWordWrap(True)
        self.ui.charBio_2.setWordWrap(True)
        self.ui.corpDescription.setText(corpDescription)
        self.ui.corpDescription.setWordWrap(True)
        self.ui.secStatus.setText('Security Status: '+str(securityStatus))
        self.ui.secStatus_2.setText('Security Status: '+str(securityStatus))
        
def main():
    app = QApplication(sys.argv)
    form = eitMain()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()