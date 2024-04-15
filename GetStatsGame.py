from bs4 import BeautifulSoup
import requests
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def getStats(html_doc, sChrome):

    chrome_options = Options()
    # maximized window
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
    driver.get(html_doc)
    time.sleep(4)
    to_soup = driver.page_source
    driver.close()

    soup = BeautifulSoup(to_soup, 'lxml')

    #req = requests.get(html_doc)
    #soup = BeautifulSoup(req.text, 'lxml')

    #infoList = soup.find_all('div', class_="css-1dbjc4n r-qklmqi")
    # infoList = soup.find_all('div', class_="css-1dbjc4n r-6koalj r-18u37iz r-117bsoe")
    infoList = soup.find_all('div', class_="css-146c3p1")
    teamStats = []

    count = 0

    while len(infoList) == 0 and count<5:
        driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
        driver.get(html_doc)
        time.sleep(5)
        to_soup = driver.page_source
        driver.close()

        soup = BeautifulSoup(to_soup, 'lxml')

        # req = requests.get(html_doc)
        # soup = BeautifulSoup(req.text, 'lxml')

        # infoList = soup.find_all('div', class_="css-1dbjc4n r-qklmqi")
        #infoList = soup.find_all('div', class_="css-1dbjc4n r-6koalj r-18u37iz r-117bsoe")
        infoList = soup.find_all('div', class_="css-146c3p1")
        count+=1

    for ii in range(0, len(infoList)-1):

        if 'Fc' in infoList[ii].text and '#' in infoList[ii+1].text:
            teamStats.append(getStatsByTeam2(infoList, ii))

    if len(infoList) == 0:
        teamStats.append(0)
        teamStats.append(0)
    elif len(infoList) ==1 and ("no estan disponibles" in infoList[0].text):
        teamStats.append(0)
        teamStats.append(0)

    return teamStats

def getStatsByTeam(info):

    playersHome = []
    numHome = []
    init5Home = []
    minHome = []
    ptsHome = []
    t2Home = []
    t3Home = []
    t1Home = []
    rOfHome = []
    rDefHome = []
    assisHome = []
    recHome = []
    perHome = []
    tapFavHome = []
    tapConHome = []
    matHome = []
    falComHome = []
    falSofHome = []
    valHome = []

    #playersList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b")
    #numbersList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b r-18qmn74 r-q4m81j")
    #minsFaltList = info.find_all('div', class_="css-901oao r-n6v787 r-q4m81j r-1y566p8")
    #puntosList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b r-q4m81j r-1y566p8")
    #tirsList = info.find_all('div', class_='css-901oao r-n6v787 r-q4m81j')

    #playersList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b")
    #numbersList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b r-1vr07ui r-q4m81j")
    #minsFaltList = info.find_all('div', class_="css-901oao r-n6v787 r-q4m81j r-1yvhtrz")
    #puntosList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b r-q4m81j r-1yvhtrz")
    #tirsList = info.find_all('div', class_='css-901oao r-n6v787 r-q4m81j')

    playersList = info.find_all('div', class_="css-146c3p1 r-vw2c0b")
    numbersList = info.find_all('div', class_="css-901oao r-n6v787 r-vw2c0b r-1vr07ui r-q4m81j")
    minsFaltList = info.find_all('div', class_="css-146c3p1")
    puntosList = info.find_all('div', class_="css-146c3p1 r-vw2c0b")
    tirsList = info.find_all('div', class_='css-901oao r-n6v787 r-q4m81j')

    players_len = len(playersList) // 3
    for i in range(0, players_len):
        mins = minsFaltList[2 * i + 3].text
        iMins = int(time2secs(mins))
        if iMins>0:
            playersHome.append(playersList[i].text)
            numHome.append(numbersList[i].text.replace('#',''))
            init5Home.append(False)
            minHome.append(mins)
            ptsHome.append(puntosList[i].text)
            t1Home.append(tirsList[6 * i].text)
            t2Home.append(tirsList[6 * i + 2].text)
            t3Home.append(tirsList[6 * i + 4].text)
            rOfHome.append('0')
            rDefHome.append('0')
            assisHome.append('0')
            recHome.append('0')
            perHome.append('0')
            tapFavHome.append('0')
            tapConHome.append('0')
            matHome.append('0')
            falComHome.append(minsFaltList[2*i+1+3].text)
            falSofHome.append('0')
            valHome.append('0')

    return [playersHome, numHome, init5Home, minHome, ptsHome, t2Home, t3Home, t1Home, rOfHome, rDefHome, assisHome, recHome, perHome, tapFavHome, tapConHome, matHome, falComHome, falSofHome, valHome]

def time2secs(timeVec):
    try:
        timeSec = int(int(timeVec) * 60)
    except:
        timeSec = 0

    return timeSec

def getStatsByTeam2(info, ii):

    playersHome = []
    numHome = []
    init5Home = []
    minHome = []
    ptsHome = []
    t2Home = []
    t3Home = []
    t1Home = []
    rOfHome = []
    rDefHome = []
    assisHome = []
    recHome = []
    perHome = []
    tapFavHome = []
    tapConHome = []
    matHome = []
    falComHome = []
    falSofHome = []
    valHome = []

    info_len = len(info)
    i = ii+1
    while i < info_len:
        info_text = info[i].text
        if '#' in info_text:
            mins = info[i+3].text
            iMins = int(time2secs(mins))
            if iMins>0:
                playersHome.append(info[i+1].text)
                numHome.append(info_text.replace('#',''))
                init5Home.append(False)
                minHome.append(mins)
                ptsHome.append(info[i+2].text)
                t1Home.append(info[i+4].text)
                t2Home.append(info[i+6].text)
                t3Home.append(info[i+8].text)
                rOfHome.append('0')
                rDefHome.append('0')
                assisHome.append('0')
                recHome.append('0')
                perHome.append('0')
                tapFavHome.append('0')
                tapConHome.append('0')
                matHome.append('0')
                falComHome.append(info[i+10].text)
                falSofHome.append('0')
                valHome.append('0')
            i=i+12
        else:
            break

    return [playersHome, numHome, init5Home, minHome, ptsHome, t2Home, t3Home, t1Home, rOfHome, rDefHome, assisHome, recHome, perHome, tapFavHome, tapConHome, matHome, falComHome, falSofHome, valHome]

def getStatsTeam(pointsHome, a, team):

    teamStats = list(np.array(a)[:, -1])
    teamStats[0] = team
    teamStats[1] = '101'
    teamStats[4] = str(pointsHome)

    min = 0
    t2S = 0
    t2A = 0
    t3S = 0
    t3A = 0
    t1S = 0
    t1A = 0
    faltes = 0

    for i in range(0,len(a[0])):
        min += int(a[3][i])
        t2 = a[5][i].split('/')
        t2S += int(t2[0])
        t2A += int(t2[1])
        t3 = a[6][i].split('/')
        t3S += int(t3[0])
        t3A += int(t3[1])
        t1 = a[7][i].split('/')
        t1S += int(t1[0])
        t1A += int(t1[1])
        faltes += int(a[16][i])

    teamStats[3] = str(min)
    teamStats[5] = str(t2S) + '/' + str(t2A)
    teamStats[6] = str(t3S) + '/' + str(t3A)
    teamStats[7] = str(t1S) + '/' + str(t1A)
    teamStats[16] = str(faltes)

    return teamStats