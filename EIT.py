#-*- coding: utf-8 -*-
'''
Created on May 12, 2017

@author: Aradina
'''
from design import Ui_MainWindow
from esipy import EsiClient, App
from json import loads
from sys import argv
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from urllib import request

esiApp = App.create('https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility') # this establishes the ESI connection.
esi_client = EsiClient()

class eitMain(QMainWindow):
    def __init__(self):
        super(eitMain, self).__init__()
                
        self.ui = Ui_MainWindow()  #Opens the main window.
        self.ui.setupUi(self)
        self.ui.searchBtn.clicked.connect(self.charSearch)  #this is the search button.
        self.ui.actionExit.triggered.connect(QApplication.quit)    #This is the quit option in the menu bar.
        
    def charSearch(self):   #this passes the text from the search box to the later thing that actually searches.
        self.charName = self.ui.charSearch.text()
        esiFunction.charIntelSearch(self, eitMain)
        
    def noResults(self):    #this is displayed if your search has no results, otherwise it would crash.
        noResults = QMessageBox()
        noResults.setIcon(QMessageBox.Information)
        noResults.setText("No Results Found.")
        noResults.setInformativeText("Search must be exact.\n\nCase Sensitive.")
        noResults.setStandardButtons(QMessageBox.Ok)
        noResults.setWindowTitle("Error")
        noResults.exec_()
        self.ui.searchBtn.clicked.connect(self.charSearch)
        
class esiFunction():
    def charIntelSearch(self, eitMain): #the main function. This takes the character name, gets the character ID via the search end point on ESI.
        charSearch = esiApp.op['get_search'](               #It then uses this to get all the data shown.
            categories = 'character',
            search = self.charName,
            strict = 'true'
            )
        charSearch = esi_client.request(charSearch)
        self.charID = loads(charSearch.raw)
        if 'character' not in self.charID:     #Makes sure there are results, if not it causes an error.
            eitMain().noResults()
        else:
            self.charID = str(self.charID['character'])
            self.charID = self.charID.strip("[]")
            esiFunction.charIntSucess(self, eitMain)
            
    def charIntSucess(self, eitMain):   #after getting the character ID, it then gets all the data and sets it. This is that.
        charID = self.charID
        charSheet = esiApp.op['get_characters_character_id'](
            character_id = charID
            )
        charSheet = esi_client.request(charSheet)
        charSheet = loads(charSheet.raw)
        charBio = charSheet['description']
        securityStatus = charSheet['security_status']
        securityStatus = round(securityStatus, 2)   #this rounds the security status to a more useful number. Hopefully.
        corpID = str(charSheet['corporation_id'])
        corpDetails = esiApp.op['get_corporations_corporation_id'](
            corporation_id = corpID
            )
        corpSheet = esi_client.request(corpDetails)
        corpSheet = loads(corpSheet.raw)
        corpName = corpSheet['corporation_name']
        corpDescription = corpSheet['corporation_description']
        corpTicker = corpSheet['ticker']
        corpMemberCount = corpSheet['member_count']
        corpCeo = corpSheet['ceo_id']
        corpCeoName = esiApp.op['get_characters_character_id'](
            character_id = corpCeo
            )
        corpCeo = esi_client.request(corpCeoName)
        corpCeo = loads(corpCeo.raw)
        corpCeo = corpCeo['name']
        if 'alliance_id' in corpSheet:      #This checks to see if the person searched is in an alliance, if they are it gets the logo.
            allianceID = corpSheet['alliance_id']
            allianceimgURL = "https://imageserver.eveonline.com/Alliance/{}_128.png".format( allianceID )
            allianceurl = request.urlopen(allianceimgURL).read()
            pixmapAlliance = QPixmap()
            pixmapAlliance.loadFromData(allianceurl)
            self.ui.allianceLogo.setPixmap(pixmapAlliance)
            self.ui.allianceLogo_2.setPixmap(pixmapAlliance)
            
        charimgURL = "https://imageserver.eveonline.com/Character/{}_128.jpg".format( charID )
        charurl = request.urlopen(charimgURL).read()
        pixmapChar = QPixmap()
        pixmapChar.loadFromData(charurl)
        self.ui.charLogo.setPixmap(pixmapChar)
        
        corpimgURL = "https://imageserver.eveonline.com/Corporation/{}_128.png".format( corpID )
        corpurl = request.urlopen(corpimgURL).read()
        pixmapCorp = QPixmap()
        pixmapCorp.loadFromData(corpurl)
        self.ui.corpLogo.setPixmap(pixmapCorp)
        self.ui.corpLogo_2.setPixmap(pixmapCorp)
        self.ui.charName.setText('Name: '+self.charName)
        self.ui.charName_2.setText('Name: '+self.charName)
        self.ui.corpCeo.setText('CEO: '+corpCeo)
        self.ui.corpName.setText('Corporation Name: '+corpName+' : '+corpTicker)
        self.ui.corpName_2.setText('Corporation Name: '+corpName+' : '+corpTicker)
        self.ui.corpMembers.setText('Member Count: '+str(corpMemberCount))
        self.ui.corpMembers_2.setText('Member Count: '+str(corpMemberCount))
        self.ui.charBio.setText(charBio)
        self.ui.charBio_2.setText(charBio)
        self.ui.charBio.setWordWrap(True)
        self.ui.charBio_2.setWordWrap(True)
        self.ui.corpDescription.setText(corpDescription)
        self.ui.corpDescription.setWordWrap(True)
        self.ui.secStatus.setText('Security Status: '+str(securityStatus))
        self.ui.secStatus_2.setText('Security Status: '+str(securityStatus))
        
def main():
    app = QApplication(argv)
    form = eitMain()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()