from bs4 import BeautifulSoup
import requests
import numpy as np

import GetPlayByPlayGame
import GetStatsGame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from pandas import DataFrame
import GamesCommonFunctionsAllLeagueExtended as GLCE
import GamesCommonFuctions as GC
import unicodedata
import platform

statsPlayers = []
teamNames = []
sLocal = []
sAway = []
sWin = []
sDif = []

def extractStatisticsAllLeague(html_doc,season,jorFirst,jorLast,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang, bOnlyTeam, targetTeams):
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    system = platform.system()

    if sLang == "Castellano":
        sAllR = "Jornadas"
        sJor = 'Jornada: '
        sExtr = 'Extrayendo Partidos:'
    else:
        sAllR = "AllRounds"
        sJor = 'Round: '
        sExtr = 'Extracting Games:'

    jornadas = soup.find_all('div', class_="rowsJornada")
    # firstJornada = jornadas[0].text.split('/')[0]

    iBenIn = 2
    iEndIn = -1

    chrome_options = Options()
    # maximized window
    chrome_options.add_argument("--start-maximized")

    resLoc = []
    resVis = []
    sLocal = []
    sAway = []
    sWin = []
    sDif = []

    jorTot = 0

    pageIn = 0
    pageFin = 1

    jorProcessFirst = int(jorFirst)-1
    jorProcessLast = int(jorLast)

    sPlayers = sPlayers.split(',')
    sPlayers = [x.upper() for x in sPlayers]

    for page in range(pageIn,pageFin):
        print(sExtr)
        for jornada in range(jorProcessFirst, jorProcessLast):
            print(sJor + str(jorProcessFirst + (jornada-jorProcessFirst) + 1))
            jorTot += 1
            jornadaInd = jornadas[jornada]
            gamesJorn = jornadaInd.find_all('div', class_="rowJornada col-md-12 col-xs-12 text-center")+jornadaInd.find_all('div', class_="rowJornada shadowRow col-md-12 col-xs-12 text-center")
            linksJorn = jornadaInd.find_all('div', class_="rowJornada fs-38 col-md-12 col-xs-12 text-center")+jornadaInd.find_all('div', class_="rowJornada shadowRow fs-38 col-md-12 col-xs-12 text-center")

            itOdd = 0
            for k in range(0, len(gamesJorn)):
                itOdd += 1

                try:
                    gameCode = linksJorn[k].find_all('a')[0 ]['href']
                except:
                    continue
                gameCodeTirs = gameCode.replace('estadistiques', 'estadistiques/tirs')
                gameCodeJugades = gameCode.replace('estadistiques', 'estadistiques/jugades')

                if not gameCodeTirs.__contains__("basquetcatala"):
                    gameCodeTirs = gameCodeTirs.replace("/competicions-anteriors/resultat",
                                                        "https://www.basquetcatala.cat")
                    gameCodeJugades = gameCodeJugades.replace("/competicions-anteriors/resultat",
                                                              "https://www.basquetcatala.cat")
                if not gameCodeTirs.__contains__("/" + season + "/"):
                    gameCodeTirs = gameCodeTirs.replace('estadistiques/tirs', 'estadistiques/tirs/' + season)
                    gameCodeJugades = gameCodeJugades.replace('estadistiques/jugades',
                                                              'estadistiques/jugades/' + season)

                if not gameCodeTirs.__contains__("tirs"):
                    print('Data Not Exists')
                    continue

                a, b = GetStatsGame.getStats(gameCodeTirs, sChrome)

                if a==0:
                    print("Game not found")
                    continue

                #TODO check stats
                #c, d = GetPlayByPlayGame.getStats(gameCode, sChrome, a[0], b[0])
                c, d = GetPlayByPlayGame.getEmptyStats(a[0], b[0])

                a += c
                b += d

                locTeam = str(
                    unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[2]).encode('ascii', 'ignore'))[
                          iBenIn:iEndIn]
                visTeam = str(
                    unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[8]).encode('ascii', 'ignore'))[
                          iBenIn:iEndIn]

                try:
                    linksSplit = linksJorn[k].text.split('\n')
                    resLocVisNonEmpty = [s for s in linksSplit if s]
                    resLocIn = int(resLocVisNonEmpty[0])
                    resVisIn = int(resLocVisNonEmpty[1])

                    resLoc.append(resLocIn)
                    resVis.append(resVisIn)

                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        a1 = GC.filterPlayers(a, sPlayers)
                    else:
                        a1 = a
                    if a1 != []:
                        dif = resLocIn - resVisIn
                        statsPlayers.append(a1)
                        teamStats = GetStatsGame.getStatsTeam(resLocIn, a, 'Equipo')
                        teamStatsAgainst = GetStatsGame.getStatsTeam(resVisIn, b, 'Equipo Rival')
                        if sLang == 'Castellano':
                            teamStats[0] = 'Equipo'
                            teamStatsAgainst[0] = 'Equipo Rival'
                        else:
                            teamStats[0] = 'Team'
                            teamStatsAgainst[0] = 'Team Against'

                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(locTeam)
                        teamNames.append(visTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resLoc[-1])-float(resVis[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)

                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        b1 = GC.filterPlayers(b, sPlayers)
                    else:
                        b1 = b
                    if b1 != []:
                        dif = resVisIn - resLocIn
                        statsPlayers.append(b1)
                        teamStats = GetStatsGame.getStatsTeam(resVisIn, b, 'Equipo')
                        teamStatsAgainst = GetStatsGame.getStatsTeam(resLocIn, a, 'Equipo Rival')
                        if sLang == 'Castellano':
                            teamStats[0] = 'Equipo'
                            teamStatsAgainst[0] = 'Equipo Rival'
                        else:
                            teamStats[0] = 'Team'
                            teamStatsAgainst[0] = 'Team Against'
                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(visTeam)
                        teamNames.append(locTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resVis[-1])-float(resLoc[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)
                except:
                    pass

    if sPlayers != [] and bOnlyTeam == False:
        sOutput = sOutput + '-' + str(len(sPlayers)) + 'Pl'

    if bOnlyTeam == False:
        GLCE.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang, False, targetTeams)
        GLCE.get5FasesStats(statsPlayers, season, jorFirst, jorLast, sDir, int(1), sLeague.split(',')[0], sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif, teamNames, sLang, len(sPlayers))
    else:
#        if targetTeam[4:9] == 'PLATA' or targetTeam[4:7] == 'LF2' or targetTeam[4:7] == 'EBA':
 #           sOutput = targetTeam[4:]
  #          sLeague = ''
        GLCE.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang, True, targetTeams)
