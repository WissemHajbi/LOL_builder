import sys
import requests , bs4 , os , shutil
from PyQt6.QtGui import QIcon

from PyQt6.QtWidgets import QWidget , QApplication
from PyQt6 import uic , QtGui


class window( QWidget ):
    champs = ['aatrox' , 'ahri' , 'akali' , 'akshan' , 'alistar' , 'amumu' , 'anivia' , 'annie' , 'aphelios'
        , 'ashe' , 'aurelion sol' , 'azir' , 'bard' , 'blitzcrank' , 'brand' , 'bard' , 'caitlyn' , 'camille' ,
              'cassiopeia' , 'chogath' , 'corki' , 'darius' , 'ekko' , 'elise' , 'evelynn' , 'ezreal' , 'fiddlesticks' ,
              'fiora' , 'fizz' , 'galio' , 'gangplank' , 'garen' , 'gnar' , 'gragas' , 'graves' , 'gwen' , 'hecarim' ,
              'heimerdinger' ,
              'illaoi' , 'irelia' , 'ivern' , 'janna' , 'jarvin' , 'jax' , 'jayce' , 'jhin' , 'jinx' , 'kaisa' ,
              'kalista' ,
              'karma' , 'karthus' , 'kassadin' , 'katarina' , 'kayle' , 'kayn' , 'kennen' , 'khazix' , 'kindred' ,
              'kled' ,
              'kogmaw' , 'leblanc' , 'lee sin' , 'leona' , 'lillia' , 'lissandra' , 'lucian' , 'lulu' , 'lux' ,
              'malphite' ,
              'malzahar' , 'maokai' , 'master yi' , 'miss fortune' , 'mordekaiser' , 'morgana' , 'nami' , 'nasus' ,
              'nautilus' ,
              'neeko' , 'nidalee' , 'nocturne' , 'nunu' , 'olaf' , 'orianna' , 'orn' , 'pantheon' , 'poppy' , 'pyke' ,
              'qiyana' , 'quinn' , 'rakan' , 'rammus' , 'reksai' , 'rell' , 'renekton' , 'rengar' , 'riven' ,
              'sejuani' , 'senna' ,
              'seraphine' , 'sett' , 'shaco' , 'shen' , 'shyvana' , 'singed' , 'sion' , 'sivir' , 'skarner' , 'sona' ,
              'soraka' ,
              'swain' , 'sylas' , 'syndra' , 'tahm kench' , 'taliyah' , 'talon' , 'taric' , 'teemo' , 'thresh' ,
              'tristana' , 'trundle' ,
              'tryndamere' , 'twisted fate' , 'twitch' , 'udyr' , 'urgot' , 'varus' , 'vi' , 'viego' , 'viktor' ,
              'vladimir' ,
              'volibear' , 'warwick' , 'wukong' , 'xayah' , 'xerath' , 'xin zhao' , 'yasuo' , 'yone' , 'yorick' ,
              'yuumi' ,
              'zilean' , 'zoe' , 'zyra' , 'zed']

    def __init__( self ):
        super().__init__()
        uic.loadUi( "a.ui" , self )
        self.setWindowTitle('I AM ADDICTED TO LEAGUE OF LEGENDS')
        self.Roles = { }
        self.pushButtonSearch1.clicked.connect( self.checkName )
        self.pushButtonSearch2.clicked.connect( self.checkRole )
        self.errorsLabel.setStyleSheet( 'color:#ff0000;' )
        self.setFixedHeight( 600 )
        self.setFixedWidth( 900 )
        self.ProfilePicLabel.setPixmap( QtGui.QPixmap( '' ) )

    def clearRoles( self ):
        self.role1.setText( ' ' )
        self.rolesymbol1.setPixmap( QtGui.QPixmap( '' ) )
        self.role2.setText( ' ' )
        self.rolesymbol2.setPixmap( QtGui.QPixmap( '' ) )
        self.role3.setText( ' ' )
        self.rolesymbol3.setPixmap( QtGui.QPixmap( '' ) )

    def clearErrors( self ):
        self.errorsLabel.setText( ' ' )

    def checkName( self ):
        if self.lineName.text() not in self.champs:
            self.errorsLabel.setText( 'insert correct champion name' )
        else:
            self.NameSearch()

    def NameSearch( self ):
        try:
            self.clearErrors()
            self.clearRoles()
            championName = self.lineName.text()
            try:
                URL = 'http://www.op.gg/champion/{}/statistics/mid/build'.format( championName )
            except:
                self.errorsLabel.setText( 'theres a mistake in the champion role or name' )
                URL = ''
            # nhabet lpage HTML kemla
            requestedChampionPage = requests.get( URL )
            tokenHTML = bs4.BeautifulSoup( requestedChampionPage.content , 'html.parser' )
            listNames = tokenHTML.find_all( 'span' , class_='champion-stats-header__position__role' )
            listpercentage = tokenHTML.find_all( 'span' , class_='champion-stats-header__position__rate' )
            for i in range( len( listNames ) ):
                self.Roles[listNames[i].getText()] = listpercentage[i].getText()[:str( listpercentage[i] ).index( '%' )]
            self.role1.setText( listNames[0].getText() + ' ' + self.Roles[listNames[0].getText()] )
            self.rolesymbol1.setPixmap( QtGui.QPixmap( listNames[0].getText() + '.png' ) )
            self.role2.setText( listNames[1].getText() + ' ' + self.Roles[listNames[1].getText()] )
            self.rolesymbol2.setPixmap( QtGui.QPixmap( listNames[1].getText() + '.png' ) )
            self.role3.setText( listNames[2].getText() + ' ' + self.Roles[listNames[2].getText()] )
            self.rolesymbol3.setPixmap( QtGui.QPixmap( listNames[2].getText() + '.png' ) )

            def returnNameSearch():
                return championName
        except Exception as e:
            print( e )

    def checkRole( self ):
        roles = ['Middle' , 'Top' , 'Jungle' , 'Bottom' , 'Support']
        try:
            if self.lineRole.text().capitalize() in roles:
                self.runesSearch( self.lineRole.text().capitalize() )
            elif self.lineRole.text() == 'mid':
                self.runesSearch( 'Middle' )
            elif self.lineRole.text() == 'sup':
                self.runesSearch( 'Support' )
            elif self.lineRole.text() == 'jng':
                self.runesSearch( 'Jungle' )
            elif self.lineRole.text() == 'bot':
                self.runesSearch( 'Bottom' )
            elif self.lineRole.text() == 'top':
                self.runesSearch( 'Top' )
            else:
                self.errorsLabel.setText(
                    f"please insert another role" )
        except Exception as a:
            print( a )

    def runesSearch( self , championRole ):
        self.sitem4.setPixmap( QtGui.QPixmap( ' ' ) )
        self.clearErrors()
        try:
            # runes
            URL = 'http://www.op.gg/champion/{}/statistics/{}/build'.format( self.lineName.text() , championRole )
            requestedChampionPage = requests.get( URL )
            tokenHTML = bs4.BeautifulSoup( requestedChampionPage.content , 'html.parser' )
            BigDiv = tokenHTML.find( 'div' , class_='perk-page-wrap' )
            allImages = BigDiv.find_all( 'img' )
            # champion picture
            bigDiv = tokenHTML.find( 'div' , class_='champion-stats-header-info__image' )
            profileImage = bigDiv.find( 'img' )
            profileImageLink = 'http:' + profileImage['src']
            # summonner speels
            bigDiv = tokenHTML.find_all( 'ul' , class_='champion-stats__list' )
            rownumber = 0
            numberName = 0
            for bigdiv in bigDiv:
                littleDiv = bigdiv.find_all( 'img' )
                if rownumber == 0 or rownumber == 2:
                    for j in littleDiv:
                        numberName += 1
                        link = 'http:' + j['src']
                        if 'blet.png' not in link:
                            img = open(
                                f'C:\\users\\wisse\\projects\\LOL Builder\\abilities and Summoners\\'
                                f'{str( numberName )}.jpg' ,
                                'wb' )
                            s = requests.get( link )
                            img.write( s.content )
                rownumber += 1
            # nekhou il images li activated
            activatedImages = []
            for image in allImages:
                if '?image=q_auto' in image['src']:
                    activatedImages.append( image )
            # build
            URL = 'https://app.mobalytics.gg/lol/champions/{}/build'.format( self.lineName.text() )
            request = requests.get( URL )
            tokenHTML1 = bs4.BeautifulSoup( request.content , 'html.parser' )
            bigDiv1 = tokenHTML1.find_all( 'div' , class_='m-1uz370t' )
            BuildImages = bigDiv1[3].find_all( 'img' )
            numberBuildName = 0
            for image in BuildImages:
                numberBuildName += 1
                link = image['src']
                img = open( f'C:\\users\\wisse\\projects\\LOL Builder\\Build\\{str( numberBuildName )}.jpg' ,
                            'wb' )
                s = requests.get( link )
                img.write( s.content )
            # starting items
            BuildImages1 = bigDiv1[0].find_all( 'img' )
            numberBuildName = 0
            for image in BuildImages1:
                numberBuildName += 1
                link = image['src']
                img = open(
                    f'C:\\users\\wisse\\projects\\LOL Builder\\Build\\Starting items\\'
                    f'{str( numberBuildName )}.jpg' ,
                    'wb' )
                s = requests.get( link )
                img.write( s.content )
            # nasna3 folder w nadhfou
            folderprename = 'Runes'
            pathFolder = r'C:\Users\wisse\projects\LOL Builder'
            if os.path.exists( pathFolder + '\\' + folderprename ):
                shutil.rmtree( pathFolder + '\\' + folderprename )
            os.mkdir( pathFolder + '\\' + folderprename )

            listNames = []
            namenum = 0
            for i in range( len( activatedImages ) ):
                namenum += 1
                link = 'http:' + activatedImages[i]['src']
                img = open( pathFolder + '\\Runes\\' + str( namenum ) + '.jpg' , 'wb' )
                listNames.append( str( namenum ) )
                requestedImageLinkDownload = requests.get( link )
                img.write( requestedImageLinkDownload.content )

            comps = [self.l1 , self.l2 , self.l3 , self.l4 , self.l5 , self.l6 , self.l7 , self.l8 , self.l9 ,
                     self.l10 , self.l11]
            summonerSpells = [self.sum1 , self.sum2]
            abilities = [self.ab1 , self.ab2 , self.ab3]
            FullBuildItems = [self.item1 , self.item2 , self.item3 , self.item4 , self.item5 , self.item6]
            StartingItems = [self.sitem1 , self.sitem2 , self.sitem3 , self.sitem4]

            # loading the images to the GUI
            for i in range( len( comps ) ):
                comps[i].setPixmap(
                    QtGui.QPixmap( pathFolder + '\\Runes\\' + str( i + 1 ) + '.jpg' ) )
            for i in range( len( summonerSpells ) ):
                summonerSpells[i].setPixmap(
                    QtGui.QPixmap( pathFolder + '\\abilities and Summoners\\' + str( i + 1 ) + '.jpg' ) )
            for i in range( len( abilities ) ):
                abilities[i].setPixmap(
                    QtGui.QPixmap( pathFolder + '\\abilities and Summoners\\' + str( i + i + 3 ) + '.jpg' ) )
            for i in range( len( FullBuildItems ) ):
                FullBuildItems[i].setPixmap( QtGui.QPixmap( pathFolder + '\\Build\\' + str( i + 1 ) + '.jpg' ) )
            for i in range( len( BuildImages1 ) ):
                StartingItems[i].setPixmap(
                    QtGui.QPixmap( pathFolder + '\\Build\\Starting items\\' + str( i + 1 ) + '.jpg' ) )
            self.abdash1.setText( '>' )
            self.abdash2.setText( '>' )
            img = open( 'C:\\users\\wisse\\projects\\LOL Builder\\profile.jpg' , 'wb' )
            profileImageRequest = requests.get( profileImageLink )
            img.write( profileImageRequest.content )
            self.ProfilePicLabel.setPixmap( QtGui.QPixmap( pathFolder + '\\' + 'profile.jpg' ) )

        except Exception as e:
            print( e )


app = QApplication( [] )
window = window()
window.show()
sys.exit( app.exec() )
