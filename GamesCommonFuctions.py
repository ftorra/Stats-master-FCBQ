from pandas import DataFrame
import numpy as np
import datetime
import platform
import barChart

def time2secsOld(timeVec):
    try:
        timeSec = (int(timeVec.split(":")[0]) * 60 + int(timeVec.split(":")[1]))
    except:
        timeSec = 0

    return timeSec

def time2secs(timeVec):
    try:
        timeSec = int(int(timeVec) * 60)
    except:
        timeSec = 0

    return timeSec

def parse_stats_scratch_player(statsPlayers, game, indPl, sType):
    lnum = []
    lnum.append(statsPlayers[game][1][indPl])
    lNames = []
    lNames.append(statsPlayers[game][0][indPl].encode('ascii', errors='ignore'))
    lTypes = []
    lTypes.append(sType)
    lGames = []
    lGames.append(int(1))
    lMins = []
    iMins = int(time2secs(statsPlayers[game][3][indPl]))
    lMins.append(iMins)
    lPts = []
    lPts.append(int(statsPlayers[game][4][indPl]))
    lt2S = []
    it2S = int(statsPlayers[game][5][indPl].split("/")[0])
    lt2S.append(it2S)
    lt2A = []
    it2A = int(statsPlayers[game][5][indPl].split("/")[1])
    lt2A.append(it2A)
    lt2p = []
    if it2A == 0:
        lt2p.append(round(0.0, 2))
    else:
        lt2p.append(round(float(it2S)/it2A,2))
    lt3S = []
    it3S = int(statsPlayers[game][6][indPl].split("/")[0])
    lt3S.append(it3S)
    lt3A = []
    it3A = int(statsPlayers[game][6][indPl].split("/")[1])
    lt3A.append(it3A)
    lt3p = []
    if it3A == 0:
        lt3p.append(round(0.0, 2))
    else :
        lt3p.append(round(float(it3S)/it3A,2))
    lt1S = []
    it1S = int(statsPlayers[game][7][indPl].split("/")[0])
    lt1S.append(it1S)
    lt1A = []
    it1A = int(statsPlayers[game][7][indPl].split("/")[1])
    lt1A.append(it1A)
    lt1p = []
    if it1A == 0:
        lt1p.append(round(0.0, 2))
    else :
        lt1p.append(round(float(it1S)/it1A,2))
    lrOf = []
    lrOf.append(int(statsPlayers[game][8][indPl]))
    lrDef = []
    lrDef.append(int(statsPlayers[game][9][indPl]))
    lrReb = []
    lrReb.append(int(statsPlayers[game][8][indPl])+int(statsPlayers[game][9][indPl]))
    lAssis = []
    iAssis = int(statsPlayers[game][10][indPl])
    lAssis.append(iAssis)
    lRec = []
    lRec.append(int(statsPlayers[game][11][indPl]))
    lPer = []
    lPer.append(int(statsPlayers[game][12][indPl]))
    lTapF = []
    lTapF.append(int(statsPlayers[game][13][indPl]))
    lTapC = []
    lTapC.append(int(statsPlayers[game][14][indPl]))
    lMat = []
    lMat.append(int(statsPlayers[game][15][indPl]))
    lFalC = []
    lFalC.append(int(statsPlayers[game][16][indPl]))
    lFalF = []
    lFalF.append(int(statsPlayers[game][17][indPl]))
    lVal = []
    lVal.append(int(statsPlayers[game][18][indPl]))
    lAssisP = []
    lAssisP.append(0)
    lEffp = []
    lEffp.append(0)
    lTShoot = []
    lTShoot.append(0)
    lGScore = []
    lGScore.append(0)
    lScPoss = []
    lScPoss.append(0)
    lnScPoss = []
    lnScPoss.append(0)
    lTotPoss = []
    lTotPoss.append(0)
    lFloorPer = []
    lFloorPer.append(0)
    lPpshot = []
    lPpshot.append(0)
    lPerReb = []
    lPerDefReb = []
    lPerOfReb = []
    lPerReb.append(0)
    lPerDefReb.append(0)
    lPerOfReb.append(0)
    lStPer = []
    lStPer.append(0)
    lTouches = []
    lTouches.append(0)
    lUsage = []
    lUsage.append(0)
    lVersatility = []
    lVersatility.append(0)
    lWinScore = []
    lWinScore.append(0)
    lOERi = []
    lOERi.append(0)
    lDERi = []
    lDERi.append(0)
    lNet = []
    lNet.append(0)
    lPerPas = []
    lPerPas.append(int(statsPlayers[game][19][indPl]))
    lPerBal = []
    lPerBal.append(int(statsPlayers[game][20][indPl]))
    lPerOthers = []
    lPerOthers.append(int(statsPlayers[game][21][indPl]))
    lFalTir = []
    lFalTir.append(int(statsPlayers[game][22][indPl]))
    lFalNoTir = []
    lFalNoTir.append(int(statsPlayers[game][23][indPl]))
    lTecnica = []
    lTecnica.append(int(statsPlayers[game][24][indPl]))
    lAnti = []
    lAnti.append(int(statsPlayers[game][25][indPl]))
    lOff = []
    lOff.append(int(statsPlayers[game][26][indPl]))
    lRebOff2p = []
    lRebOff2p.append(int(statsPlayers[game][33][indPl]))
    lRebOff3p = []
    lRebOff3p.append(int(statsPlayers[game][34][indPl]))
    lRebOff2pR = []
    lRebOff2pR.append(0)
    lRebOff3pR = []
    lRebOff3pR.append(0)
    # UsT3
    lu3p = []
    if it3A == 0:
        lu3p.append(round(0.0,2))
    else:
        lu3p.append(round(float(it3A) / (float(it2A)+float(it3A)),2))
    ltcS = []
    itcS = it2S+it3S
    ltcS.append(itcS)
    ltcA = []
    itcA = it2A+it3A
    ltcA.append(itcA)
    ltcp = []
    if itcA == 0:
        ltcp.append(round(0.0, 2))
    else:
        ltcp.append(round(float(itcS)/itcA,2))

    return [lNames, lTypes, lGames, lMins, lPts, lt2S, lt2A, lt2p, lt3S, lt3A, lt3p, lt1S, lt1A, lt1p, lrOf, lrDef, lrReb, lAssis, lRec, lPer, lTapF, lTapC, lMat, lFalC, lFalF, lVal, lAssisP, lEffp, lTShoot, lGScore, lScPoss, lnScPoss, lTotPoss, lFloorPer, lPpshot, lPerReb, lPerDefReb, lPerOfReb, lStPer, lTouches, lUsage, lVersatility, lWinScore, lOERi, lDERi, lNet, lPerPas, lPerBal, lPerOthers, lFalTir, lFalNoTir, lTecnica, lAnti, lOff, lRebOff2p, lRebOff3p, lRebOff2pR, lRebOff3pR,lu3p,ltcS,ltcA,ltcp,lnum]

def parse_stats_existing_player(statsPlayers, game, indPl, avStats, iPlayer, sType):
    avStats[indPl][2][0] = (int(avStats[indPl][2][0])+1)
    # Minutes
    try:
        iMins = time2secs(statsPlayers[game][3][iPlayer])
        avStats[indPl][3][0] = avStats[indPl][3][0]+iMins
    except:
        pass
    # Points
    iPts = int(statsPlayers[game][4][iPlayer])
    avStats[indPl][4][0] = int(avStats[indPl][4][0]) + iPts
    # lt2
    it2M = int(statsPlayers[game][5][iPlayer].split("/")[0])
    it2A = int(statsPlayers[game][5][iPlayer].split("/")[1])
    avStats[indPl][5][0] = int(avStats[indPl][5][0]) + it2M
    avStats[indPl][6][0] = int(avStats[indPl][6][0]) + it2A
    try:
        avStats[indPl][7][0] = round(float(avStats[indPl][5][0]) / float(avStats[indPl][6][0]),2)
    except:
        avStats[indPl][7][0] = 0
    # lt3
    it3M = int(statsPlayers[game][6][iPlayer].split("/")[0])
    it3A = int(statsPlayers[game][6][iPlayer].split("/")[1])
    avStats[indPl][8][0] = int(avStats[indPl][8][0]) + it3M
    avStats[indPl][9][0] = int(avStats[indPl][9][0]) + it3A
    try:
        avStats[indPl][10][0] = round(float(avStats[indPl][8][0]) / float(avStats[indPl][9][0]),2)
    except:
        avStats[indPl][10][0] = 0
    # lt1
    it1M =  int(statsPlayers[game][7][iPlayer].split("/")[0])
    it1A =  int(statsPlayers[game][7][iPlayer].split("/")[1])
    avStats[indPl][11][0] = int(avStats[indPl][11][0]) + it1M
    avStats[indPl][12][0] = int(avStats[indPl][12][0]) + it1A

    try:
        avStats[indPl][13][0] = round(float(avStats[indPl][11][0]) / float(avStats[indPl][12][0]),2)
    except:
        avStats[indPl][13][0] = 0

    #Rebs
    iOfReb = int(statsPlayers[game][8][iPlayer])
    iDefReb = int(statsPlayers[game][9][iPlayer])
    avStats[indPl][14][0] = int(avStats[indPl][14][0]) + iOfReb
    avStats[indPl][15][0] = int(avStats[indPl][15][0]) + iDefReb
    avStats[indPl][16][0] = int(avStats[indPl][16][0]) + iOfReb + iDefReb
    # Resta
    iAssis = int(statsPlayers[game][10][iPlayer])
    avStats[indPl][17][0] = int(avStats[indPl][17][0]) + iAssis
    # Rec
    iRec = int(statsPlayers[game][11][iPlayer])
    avStats[indPl][18][0] = int(avStats[indPl][18][0]) + iRec
    # Per
    avStats[indPl][19][0] = int(avStats[indPl][19][0]) + int(statsPlayers[game][12][iPlayer])
    # Tap Fav
    iTapF = int(statsPlayers[game][13][iPlayer])
    avStats[indPl][20][0] = int(avStats[indPl][20][0]) + iTapF
    # Tap Contra
    avStats[indPl][21][0] = int(avStats[indPl][21][0]) + int(statsPlayers[game][14][iPlayer])
    # Mates
    avStats[indPl][22][0] = int(avStats[indPl][22][0]) + int(statsPlayers[game][15][iPlayer])
    # FCom
    avStats[indPl][23][0] = int(avStats[indPl][23][0]) + int(statsPlayers[game][16][iPlayer])
    # FSof
    avStats[indPl][24][0] = int(avStats[indPl][24][0]) + int(statsPlayers[game][17][iPlayer])
    # Val
    avStats[indPl][25][0] = int(avStats[indPl][25][0]) + int(statsPlayers[game][18][iPlayer])
    # Perduda passe
    avStats[indPl][46][0] = int(avStats[indPl][46][0]) + int(statsPlayers[game][19][iPlayer])
    # Perduda pilota
    avStats[indPl][47][0] = int(avStats[indPl][47][0]) + int(statsPlayers[game][20][iPlayer])
    # Perduda altres
    avStats[indPl][48][0] = int(avStats[indPl][48][0]) + int(statsPlayers[game][21][iPlayer])
    # Faltes de tir
    avStats[indPl][49][0] = int(avStats[indPl][49][0]) + int(statsPlayers[game][22][iPlayer])
    # Faltes no de tir
    avStats[indPl][50][0] = int(avStats[indPl][50][0]) + int(statsPlayers[game][23][iPlayer])
    # Tecn
    avStats[indPl][51][0] = int(avStats[indPl][51][0]) + int(statsPlayers[game][24][iPlayer])
    # Antiesportives
    avStats[indPl][52][0] = int(avStats[indPl][52][0]) + int(statsPlayers[game][25][iPlayer])
    # Ofensives
    avStats[indPl][53][0] = int(avStats[indPl][53][0]) + int(statsPlayers[game][26][iPlayer])
    # Rebots ofensius 2p,3p
    avStats[indPl][54][0] = int(avStats[indPl][54][0]) + int(statsPlayers[game][33][iPlayer])
    avStats[indPl][55][0] = int(avStats[indPl][55][0]) + int(statsPlayers[game][34][iPlayer])

    # UsT3
    try:
        avStats[indPl][58][0] = round(float(avStats[indPl][9][0]) / (float(avStats[indPl][6][0])+float(avStats[indPl][9][0])),2)
    except:
        avStats[indPl][58][0] = 0
    # TC
    avStats[indPl][59][0] = int(avStats[indPl][5][0])+int(avStats[indPl][8][0])
    avStats[indPl][60][0] = int(avStats[indPl][6][0])+int(avStats[indPl][9][0])
    try:
        avStats[indPl][61][0] = round(float(avStats[indPl][59][0]) / float(avStats[indPl][60][0]),2)
    except:
        avStats[indPl][61][0] = 0

    avStats[indPl][1][0] = sType

def computeAdvStatsTeam(teamStats, oppFGA, oppPer, oppFTa, oppORB, teamFGa, teamPer, teamFTa, teamORB, teamPts, teamFGm, team3Pm, teamFTm, teamDRB, oppDRB, teamAssis, teamPerPas, teamPerBal, teamPerOthers, teamAssisFT, teamAssis2P, teamAssis3P,teamORB2p,teamORB3p,oppDRB2p,oppDRB3p):
    oppPos = int(0.96 * (oppFGA + oppPer + 0.44 * oppFTa - oppORB))
    teamPoss = int(0.96 * (teamFGa + teamPer + 0.44 * teamFTa - teamORB))
    try:
        teamPace = float(teamPoss) / float(teamPoss+oppPos)
    except:
        pass
    try:
        teamOER = float(100 * teamPts) / float(teamPoss)
    except:
        pass
    teamEffPer = 100 * ((teamFGm + 0.5 * team3Pm) / float(teamFGa))
    try:
        teamScoringP = float(teamFGm + (1 - (1 - (teamFTm / teamFTa)) ** 2) * teamFTa * 0.4)
    except:
        pass
    teamPlayPer = 100 * (float(teamScoringP) / float(teamFGa + teamFTa * 0.4 + teamPer))
    teamt1R = 100 * (float(teamFTm) / float(teamFGa))

    #teamDefRebR = 100 * (teamDRB / (teamDRB + oppORB))
    #teamOfRebR = 100 * (teamORB / (teamORB + oppDRB))
    #teamAssisR = 100 * (teamAssis / (teamFGa + 0.44 * teamFTa + teamAssis + teamPer))
    #teamPerR = 100 * (teamPer) / (teamFGa+teamFTa*0.44+teamPer)
    #teamPerPasR = 100 * (teamPerPas) / (teamFGa+teamFTa*0.44+teamPer)
    #teamPerBalR = 100 * (teamPerBal) / (teamFGa+teamFTa*0.44+teamPer)
    #teamPerOthersR = 100 * (teamPerOthers) / (teamFGa+teamFTa*0.44+teamPer)
    #teamOfReb1 = teamOfRebR / 100
    #teamPlayPer1 = teamPlayPer / 100
    #teamOfRebWt = ((1-teamOfReb1) * teamPlayPer1) / ((1-teamOfReb1)*teamPlayPer1+teamOfReb1*(1-teamPlayPer1))
    #teamAssisFTR = 100 * (teamAssisFT / (teamFGa + 0.44 * teamFTa + teamAssis + teamPer))
    #teamAssis2PR = 100 * (teamAssis2P / (teamFGa + 0.44 * teamFTa + teamAssis + teamPer))
    #teamAssis3PR = 100 * (teamAssis3P / (teamFGa + 0.44 * teamFTa + teamAssis + teamPer))
    #teamAssistPoints = teamAssisFT + 2*teamAssis2P+3*teamAssis3P
    #teamAssistPointsR = float(100*teamAssistPoints) / float(teamPoss)

    teamDefRebR = 0
    teamOfRebR = 0
    teamAssisR = 0
    teamPerR = 0
    teamPerPasR = 0
    teamPerBalR = 0
    teamPerOthersR = 0
    teamOfReb1 = 0
    teamPlayPer1 = teamPlayPer / 100
    teamOfRebWt = 0.0
    teamAssisFTR = 0
    teamAssis2PR = 0
    teamAssis3PR = 0
    teamAssistPoints = 0
    teamAssistPointsR = 0

    if teamORB2p + oppDRB2p > 0:
        teamORB2pR = 100 * (teamORB2p / (teamORB2p + oppDRB2p))
    else:
        teamORB2pR = 0
    if teamORB3p + oppDRB3p > 0:
        teamORB3pR = 100 * (teamORB3p / (teamORB3p + oppDRB3p))
    else:
        teamORB3pR = 0

    teamStats[0][26][0] = round(teamPoss,2)
    teamStats[0][27][0] = round(teamPace,2)
    teamStats[0][28][0] = round(teamOER,2)
    teamStats[0][29][0] = round(teamEffPer,2)
    teamStats[0][30][0] = round(teamPlayPer,2)
    teamStats[0][31][0] = round(teamt1R,2)
    teamStats[0][32][0] = round(teamDefRebR,2)
    teamStats[0][33][0] = round(teamOfRebR,2)
    teamStats[0][34][0] = round(teamAssisR,2)
    teamStats[0][35][0] = round(teamPerR,2)
    teamStats[0][44][0] = round(teamPerPasR,2)
    teamStats[0][45][0] = round(teamPerBalR,2)
    teamStats[0][46][0] = round(teamPerOthersR,2)
    teamStats[0][47][0] = round(teamOfRebWt,2)
    teamStats[0][51][0] = round(teamAssisFTR,2)
    teamStats[0][52][0] = round(teamAssis2PR,2)
    teamStats[0][53][0] = round(teamAssis3PR,2)
    teamStats[0][54][0] = round(teamAssistPoints,2)
    teamStats[0][55][0] = round(teamAssistPointsR,2)
    teamStats[0][58][0] = round(teamORB2pR,2)
    teamStats[0][59][0] = round(teamORB3pR,2)

def computeAdvStats(statsPlayers, avStats, teamStats=None, teamStatsAg=None):
    teamMinsv = []
    teamFGmv = []
    teamFGav = []
    teamFTmv = []
    teamFTav = []
    team3Pmv = []
    teamAssisv = []
    teamPtsv = []
    teamORBv = []
    teamDRBv = []
    teamPerv = []
    teamTapv = []
    teamRecv = []
    teamFpv = []
    teamPerPasv = []
    teamPerBalv = []
    teamPerOthersv = []
    teamAssisFTv = []
    teamAssis2Pv = []
    teamAssis3Pv = []
    teamORB2pv = []
    teamORB3pv = []
    teamDRB2pv = []
    teamDRB3pv = []

    oppFGMv = []
    oppFGAv = []
    oppFTmv = []
    oppFTav = []
    oppPointsv = []
    oppORBv = []
    oppDRBv = []
    opp3PMv = []
    oppPerv = []
    oppFpv = []
    oppAssisv = []
    oppPerPasv = []
    oppPerBalv = []
    oppPerOthersv = []
    oppAssisFTv = []
    oppAssis2Pv = []
    oppAssis3Pv = []
    oppORB2pv = []
    oppORB3pv = []
    oppDRB2pv = []
    oppDRB3pv = []

    game = 0
    for gameAux in range(0, int(len(statsPlayers)/3)):
        teamMinsv.append(float(statsPlayers[game + 1][3].replace('\n', '').replace(':', '.')))
        teamPtsv.append(float(statsPlayers[game + 1][4]))
        teamFGmv.append(int(statsPlayers[game + 1][5].split("/")[0]) + int(statsPlayers[game + 1][6].split("/")[0]))
        teamFGav.append(int(statsPlayers[game + 1][5].split("/")[1]) + int(statsPlayers[game + 1][6].split("/")[1]))
        teamFTmv.append(int(statsPlayers[game + 1][7].split("/")[0]))
        teamFTav.append(int(statsPlayers[game + 1][7].split("/")[1]))
        team3Pmv.append(int(statsPlayers[game + 1][6].split("/")[0]))
        teamAssisv.append(int(statsPlayers[game + 1][10]))

        teamORBv.append(float(statsPlayers[game + 1][8]))
        teamDRBv.append(float(statsPlayers[game + 1][9]))
        teamRecv.append(float(statsPlayers[game + 1][11]))
        teamPerv.append(float(statsPlayers[game + 1][12]))
        teamTapv.append(float(statsPlayers[game + 1][13]))
        teamFpv.append(float(statsPlayers[game + 1][16]))

        teamPerPasv.append(float(statsPlayers[game+1][19]))
        teamPerBalv.append(float(statsPlayers[game+1][20]))
        teamPerOthersv.append(float(statsPlayers[game+1][21]))

        teamAssisFTv.append(float(statsPlayers[game+1][27]))
        teamAssis2Pv.append(float(statsPlayers[game+1][28]))
        teamAssis3Pv.append(float(statsPlayers[game+1][29]))

        teamORB2pv.append(float(statsPlayers[game+1][33]))
        teamORB3pv.append(float(statsPlayers[game+1][34]))
        teamDRB2pv.append(float(statsPlayers[game + 1][35]))
        teamDRB3pv.append(float(statsPlayers[game + 1][36]))

        oppFGMv.append(float(statsPlayers[game + 2][5].split("/")[0]) + int(statsPlayers[game + 2][6].split("/")[0]))
        oppFGAv.append(float(statsPlayers[game + 2][5].split("/")[1]) + int(statsPlayers[game + 2][6].split("/")[1]))
        oppFTmv.append(int(statsPlayers[game + 2][7].split("/")[0]))
        oppFTav.append(int(statsPlayers[game + 2][7].split("/")[1]))
        opp3PMv.append(int(statsPlayers[game + 2][6].split("/")[0]))
        oppPointsv.append(float(statsPlayers[game + 2][4]))
        oppAssisv.append(int(statsPlayers[game + 2][10]))
        oppORBv.append(float(statsPlayers[game + 2][8]))
        oppDRBv.append(float(statsPlayers[game + 2][9]))
        oppPerv.append(float(statsPlayers[game + 2][12]))
        oppFpv.append(float(statsPlayers[game + 2][16]))

        oppPerPasv.append(float(statsPlayers[game + 2][19]))
        oppPerBalv.append(float(statsPlayers[game + 2][20]))
        oppPerOthersv.append(float(statsPlayers[game + 2][21]))

        oppAssisFTv.append(float(statsPlayers[game + 2][27]))
        oppAssis2Pv.append(float(statsPlayers[game + 2][28]))
        oppAssis3Pv.append(float(statsPlayers[game + 2][29]))

        oppORB2pv.append(float(statsPlayers[game + 2][33]))
        oppORB3pv.append(float(statsPlayers[game + 2][34]))
        oppDRB2pv.append(float(statsPlayers[game + 2][35]))
        oppDRB3pv.append(float(statsPlayers[game + 2][36]))

        game = game+3

    if teamStats != None:
        teamPts = float(np.sum(np.array(teamPtsv)))
        teamFGm = float(np.sum(np.array(teamFGmv)))
        teamFGa = float(np.sum(np.array(teamFGav)))
        teamFTm = float(np.sum(np.array(teamFTmv)))
        teamFTa = float(np.sum(np.array(teamFTav)))
        team3Pm = float(np.sum(np.array(team3Pmv)))
        teamAssis = float(np.sum(np.array(teamAssisv)))
        teamORB = float(np.sum(np.array(teamORBv)))
        teamDRB = float(np.sum(np.array(teamDRBv)))
        teamPer = float(np.sum(np.array(teamPerv)))

        teamPerPas = float(np.sum(np.array(teamPerPasv)))
        teamPerBal = float(np.sum(np.array(teamPerBalv)))
        teamPerOthers = float(np.sum(np.array(teamPerOthersv)))

        teamAssisFT = float(np.sum(np.array(teamAssisFTv)))
        teamAssis2P = float(np.sum(np.array(teamAssis2Pv)))
        teamAssis3P = float(np.sum(np.array(teamAssis3Pv)))

        teamORB2p = float(np.sum(np.array(teamORB2pv)))
        teamORB3p = float(np.sum(np.array(teamORB3pv)))
        teamDRB2p = float(np.sum(np.array(teamDRB2pv)))
        teamDRB3p = float(np.sum(np.array(teamDRB3pv)))

        oppFGM = float(np.sum(np.array(oppFGMv)))
        oppFGA = float(np.sum(np.array(oppFGAv)))
        oppFTm = float(np.sum(np.array(oppFTmv)))
        oppFTa = float(np.sum(np.array(oppFTav)))
        oppPts = float(np.sum(np.array(oppPointsv)))
        oppORB = float(np.sum(np.array(oppORBv)))
        oppDRB = float(np.sum(np.array(oppDRBv)))
        oppPer = float(np.sum(np.array(oppPerv)))
        opp3PM = float(np.sum(np.array(opp3PMv)))
        oppAssis = float(np.sum(np.array(oppAssisv)))

        oppPerPas = float(np.sum(np.array(oppPerPasv)))
        oppPerBal = float(np.sum(np.array(oppPerBalv)))
        oppPerOthers = float(np.sum(np.array(oppPerOthersv)))

        oppAssisFT = float(np.sum(np.array(oppAssisFTv)))
        oppAssis2P = float(np.sum(np.array(oppAssis2Pv)))
        oppAssis3P = float(np.sum(np.array(oppAssis3Pv)))

        oppORB2p = float(np.sum(np.array(oppORB2pv)))
        oppORB3p = float(np.sum(np.array(oppORB3pv)))
        oppDRB2p = float(np.sum(np.array(oppDRB2pv)))
        oppDRB3p = float(np.sum(np.array(oppDRB3pv)))

        computeAdvStatsTeam(teamStats, oppFGA, oppPer, oppFTa, oppORB, teamFGa, teamPer, teamFTa, teamORB, teamPts, teamFGm, team3Pm, teamFTm, teamDRB, oppDRB, teamAssis, teamPerPas, teamPerBal, teamPerOthers, teamAssisFT, teamAssis2P, teamAssis3P,teamORB2p,teamORB3p,oppDRB2p,oppDRB3p)
        computeAdvStatsTeam(teamStatsAg, teamFGa, teamPer, teamFTa, teamORB, oppFGA, oppPer, oppFTa, oppORB, oppPts, oppFGM, opp3PM, oppFTm, oppDRB, teamDRB, oppAssis, oppPerPas, oppPerBal, oppPerOthers, oppAssisFT, oppAssis2P, oppAssis3P,oppORB2p,oppORB3p,teamDRB2p,teamDRB3p)


    for indPl in range(0, len(avStats)):
        name = avStats[indPl][0]
        bPlayed = []
        game = 0
        for gameAux in range(0, int(len(statsPlayers)/3)):
            namesGame = statsPlayers[game][0]
            if platform.system() == 'Linux' or platform.system() == 'Darwin':
                namesGame = ['\n' +  str(x.encode('ascii', errors='ignore'))[4:-3] +'\n' for x in namesGame]
                if '\n' + str(name[0])[4:-3] + '\n' in namesGame:
                    bPlayed.append(gameAux)
            else:
                namesGame = ['\n' +  str(x.encode('ascii', errors='ignore')) +'\n' for x in namesGame]
                if '\n' + str(name[0]) + '\n' in namesGame:
                    bPlayed.append(gameAux)

            game = game + 3
            timePlayed = divmod(avStats[indPl][3][0], 60)
            if bPlayed != [] and float(str(timePlayed[0]) + '.' + str(float(timePlayed[1]) / float(60))[2:]) > 0:
                iMins = float(str(timePlayed[0]) + '.' + str(float(timePlayed[1])/float(60))[2:])
                iPts = float(avStats[indPl][4][0])
                it2M = float(avStats[indPl][5][0])
                it2A = float(avStats[indPl][6][0])
                it3M = float(avStats[indPl][8][0])
                it3A = float(avStats[indPl][9][0])
                it1M = float(avStats[indPl][11][0])
                it1A = float(avStats[indPl][12][0])
                indFGm = it2M + it3M
                indFGa = it2A + it3A
                iOfReb = float(avStats[indPl][14][0])
                iDefReb = float(avStats[indPl][15][0])
                iAssis = float(avStats[indPl][17][0])
                iRec = float(avStats[indPl][18][0])
                iPer = float(avStats[indPl][19][0])
                iTapF = float(avStats[indPl][20][0])
                iFal = float(avStats[indPl][23][0])
                iOfReb2p = float(avStats[indPl][54][0])
                iOfReb3p = float(avStats[indPl][55][0])

                teamMins = float(np.sum(np.array(teamMinsv)[bPlayed]))
                teamPts = float(np.sum(np.array(teamPtsv)[bPlayed]))
                teamFGm = float(np.sum(np.array(teamFGmv)[bPlayed]))
                teamFGa = float(np.sum(np.array(teamFGav)[bPlayed]))
                teamFTm = float(np.sum(np.array(teamFTmv)[bPlayed]))
                teamFTa = float(np.sum(np.array(teamFTav)[bPlayed]))
                team3Pm = float(np.sum(np.array(team3Pmv)[bPlayed]))
                teamAssis = float(np.sum(np.array(teamAssisv)[bPlayed]))
                teamORB = float(np.sum(np.array(teamORBv)[bPlayed]))
                teamDRB = float(np.sum(np.array(teamDRBv)[bPlayed]))
                teamRec = float(np.sum(np.array(teamRecv)[bPlayed]))
                teamPer = float(np.sum(np.array(teamPerv)[bPlayed]))
                teamTap = float(np.sum(np.array(teamTapv)[bPlayed]))
                teamFp = float(np.sum(np.array(teamFpv)[bPlayed]))
                teamORB2p = float(np.sum(np.array(teamORB2pv)[bPlayed]))
                teamORB3p = float(np.sum(np.array(teamORB3pv)[bPlayed]))
                teamDRB2p = float(np.sum(np.array(teamDRB2pv)[bPlayed]))
                teamDRB3p = float(np.sum(np.array(teamDRB3pv)[bPlayed]))

                oppFGM = float(np.sum(np.array(oppFGMv)[bPlayed]))
                oppFGA = float(np.sum(np.array(oppFGAv)[bPlayed]))
                oppFTm = float(np.sum(np.array(oppFTmv)[bPlayed]))
                oppFTa = float(np.sum(np.array(oppFTav)[bPlayed]))
                oppPoints = float(np.sum(np.array(oppPointsv)[bPlayed]))
                oppORB = float(np.sum(np.array(oppORBv)[bPlayed]))
                oppDRB = float(np.sum(np.array(oppDRBv)[bPlayed]))
                oppPer = float(np.sum(np.array(oppPerv)[bPlayed]))
                oppFp = float(np.sum(np.array(oppFpv)[bPlayed]))
                oppORB2p = float(np.sum(np.array(oppORB2pv)[bPlayed]))
                oppORB3p = float(np.sum(np.array(oppORB3pv)[bPlayed]))
                oppDRB2p = float(np.sum(np.array(oppDRB2pv)[bPlayed]))
                oppDRB3p = float(np.sum(np.array(oppDRB3pv)[bPlayed]))

                try:
                    teamScoringP = float(teamFGm + (1 - (1 - (teamFTm / teamFTa)) ** 2) * teamFTa * 0.4)
                except:
                    pass
                teamPlayp = float(teamScoringP) / float(teamFGa + teamFTa * 0.4 + teamPer)
                if float(teamORB + oppDRB) > 0:
                    teamORBp = float(teamORB) / float(teamORB + oppDRB)
                    teamStats = (teamFGa + 0.4 * teamFTa - 1.07 * (teamORB / (teamORB + oppDRB)) * (
                                teamFGa - teamFGm) + teamPer)
                    oppStats = (oppFGA + 0.4 * oppFTa - 1.07 * (oppORB / (oppORB + teamDRB)) * (
                                oppFGA - oppFGM) + oppPer)
                else:
                    teamORBp = 0
                    teamStats = (teamFGa + 0.4 * teamFTa + teamPer)
                    oppStats = (oppFGA + 0.4 * oppFTa + oppPer)
                teamORBw = float((1 - teamORBp) * teamPlayp) / float((1 - teamORBp) * teamPlayp + teamORBp * (1 - teamPlayp))
                teamPoss = 0.5*(teamStats+oppStats)
                oppPos = teamPoss

                try:
                    avStats[indPl][26][0] = round((100*float(iAssis)/(((float(iMins)/(float(teamMins)/float(5)))*teamFGm)-indFGm)),2)
                except:
                    pass

                # eFG
                if indFGa != 0:
                    avStats[indPl][27][0] = round((float(indFGm+0.5*(int(it3M)))/float(indFGa)),2)
                else:
                    avStats[indPl][27][0] = 0

                # TS
                if float(2*(float(indFGa)+0.44*float(it1A))) != 0:
                    avStats[indPl][28][0] = round(float(iPts)/float(2*(float(indFGa)+0.44*float(it1A))),2)
                else:
                    avStats[indPl][28][0] = 0

                # Gscore
                avStats[indPl][29][0] = round(float(iPts)+0.4*float(indFGm)+0.7*float(iOfReb)+0.3*float(iDefReb)+float(iRec)+0.7*float(iAssis)+0.7*float(iTapF)-0.7*float(indFGa)-0.4*float(it1A-it1M)-0.4*float(iFal)-float(iPer),2)

                # qAst = ((float(iMins)/float(teamMins/5)) * (1.14 * (float(teamAssis-iAssis)/float(teamFGm)))) + ((((teamAssis / teamMins) * iMins * 5 - iAssis) / ((teamFGm / teamMins) * iMins * 5 - indFGm)) * (1 - (iMins / (teamMins / 5))))
                try:
                    qAst = ((float(iMins)/float(teamMins/5)) * (float(teamAssis-iAssis)/float(teamFGm-indFGm))) + ((((teamAssis / teamMins) * iMins * 5 - iAssis) / ((teamFGm / teamMins) * iMins * 5 - indFGm)) * (1 - (iMins / (teamMins / 5))))
                except:
                    qAst = 0

                try:
                    FG_Part = indFGm * (1 - 0.5 * ((iPts - it1M) / (2 * indFGa)) * qAst)
                except:
                    FG_Part = 0

                try:
                    AST_Part = 0.5 * (((teamPts - teamFTm) - (iPts - it1M)) / (2 * (teamFGa - indFGa))) * iAssis
                except:
                    AST_Part = 0
                    pass

                try:
                    FT_Part = (1 - (1 - (it1M / it1A)) ** 2) * 0.4 * it1A
                except:
                    FT_Part = 0

                ORB_Part = iOfReb * teamORBw * teamPlayp
                scPoss = (FG_Part + AST_Part + FT_Part) * (1 - (teamORB / teamScoringP) * teamORBw * teamPlayp) + ORB_Part

                FGxPoss = (indFGa - indFGm) * (1 - 1.07 * teamORBp)
                try:
                    FTxPoss = ((1 - (it1M /it1A)) ** 2) * 0.4 * it1A
                except:
                    FTxPoss = 0

                nscPoss = FGxPoss + FTxPoss + iPer

                # Free Throw Rate
                try:
                    avStats[indPl][30][0] = round(100*(it1M/indFGa),2)
                except:
                    avStats[indPl][30][0] = 0

                # Scored Poss
                avStats[indPl][31][0] = round(scPoss,2)

                # Non Scored Poss
                avStats[indPl][32][0] = round(nscPoss,2)

                # Floor Percentage
                try:
                    avStats[indPl][33][0] = round((float(100)*(float(scPoss)/float(nscPoss+scPoss))),2)
                except:
                    pass

                # Points per Shot
                if float(it2A+it3A) != 0:
                    fPointspshot = float(2*it2M+3*it3M)/float(it2A+it3A)
                    avStats[indPl][34][0] = round(fPointspshot,2)

                # % Reb
                teamAgRebs = oppDRB+oppORB
                teamRebs = teamDRB+teamORB
                if teamRebs>0:
                    fPerReb = 100*float((iOfReb+iDefReb)*(float(teamMins)/float(5)))/float(float(iMins)*(teamRebs+teamAgRebs))
                    fPerDefReb = 100 * (float(iDefReb * float(teamMins) / float(5)) / float(float(iMins) * (teamDRB + oppORB)))
                    fPerOfReb = 100 * (float(iOfReb * float(teamMins) / float(5)) / float(float(iMins) * (teamORB + oppDRB)))
                else:
                    fPerReb = 0
                    fPerDefReb = 0
                    fPerOfReb = 0
                if teamORB2p + oppDRB2p > 0:
                    fPerOfReb2p = 100 * (float(iOfReb2p * float(teamMins) / float(5)) / float(float(iMins) * (teamORB2p + oppDRB2p)))
                else:
                    fPerOfReb2p = 0
                if teamORB3p + oppDRB3p > 0:
                    fPerOfReb3p = 100 * (float(iOfReb3p * float(teamMins) / float(5)) / float(float(iMins) * (teamORB3p + oppDRB3p)))
                else:
                    fPerOfReb3p = 0

                avStats[indPl][35][0] = round(fPerReb,2)
                avStats[indPl][36][0] = round(fPerDefReb,2)
                avStats[indPl][37][0] = round(fPerOfReb,2)

                avStats[indPl][56][0] = round(fPerOfReb2p,2)
                avStats[indPl][57][0] = round(fPerOfReb3p,2)

                # % Steals
                fStPer = float(100)*(float(float(iRec)*(float(teamMins)/float(5)))/float(iMins*oppPos))
                avStats[indPl][38][0] = round(fStPer,2)

                # Touches
                fTouches = indFGa + iPer + (iAssis/float(0.17)) + (it1A / (teamFTa / oppFp))
                avStats[indPl][39][0] = round(fTouches,2)

                fUsage1 = (float(indFGa)+0.44*it1A+iPer)*float(teamMins)
                fUsage2 = (float(teamFGa) + 0.44*teamFTa + teamPer) * float(5) * float(iMins)

                if fUsage2 != 0:
                    fUsage = 100*(fUsage1)/(fUsage2)
                    avStats[indPl][40][0] = round(fUsage,2)

                # Versatility
                avStats[indPl][41][0] = round((iPts*float(iOfReb+iDefReb)*iAssis)**(0.333),2)

                # Win Scores
                fWinScore = iPts + iDefReb + iOfReb + iRec + 0.5*iAssis + 0.5*iTapF - indFGa - iPer - 0.5*it1A - 0.5*iFal
                avStats[indPl][42][0] = round(fWinScore,2)

                try:
                    pPointsProd_FG_Part = 2*(indFGm + 0.5*it3M) * (1 - 0.5*(float(iPts-it1M)/float(2*indFGa)) * qAst)
                except:
                    pPointsProd_FG_Part = 0

                try:
                    pPointsProd_AST_Part = 2 * ((teamFGm - indFGm + 0.5 * (team3Pm - it3M)) / (teamFGm - indFGm)) * 0.5 * (((teamPts - teamFTm) - (iPts - it1M)) / (2 * (teamFGa - indFGa))) * iAssis
                except:
                    pPointsProd_AST_Part = 0

                try:
                    pPointsProd_ORB_Part = iOfReb * teamORBw * teamPlayp * (teamPts / (teamFGm + (1 - (1 - (teamFTm / teamFTa))** 2) *0.4 * teamFTa))
                except:
                    pPointsProd_ORB_Part = 0

                pProd = (pPointsProd_FG_Part + pPointsProd_AST_Part + it1M) * (1 - (teamORB / teamScoringP) * teamORBw * teamPlayp) + pPointsProd_ORB_Part
                try:
                    OERi = 100*(float(pProd)/float(int(scPoss)+int(nscPoss)))
                except:
                    OERi = 100*(float(teamPts) / float(teamPoss))

                if OERi < 1:
                    OERi = 100*(float(teamPts) / float(teamPoss))

                DFGp = oppFGM / oppFGA
                if float(oppORB) + float(teamDRB) > 0:
                    DORp = float(oppORB) / (float(oppORB) + float(teamDRB))
                else:
                    DORp = 0
                FMwt = (DFGp * (1 - DORp)) / (DFGp * (1 - DORp) + (1 - DFGp) * DORp)
                Stops1 = iRec + iTapF * FMwt * (1 - 1.07 * DORp) + iDefReb * (1 - FMwt)
                Stops2 = (((oppFGA - oppFGM - teamTap) / teamMins) * FMwt * (1 - 1.07 * DORp) + ((oppPer - teamRec) / teamMins)) * iMins + (iFal / teamFp) * 0.4 * oppFTa * ((1 - (oppFTm / oppFTa))**2)
                Stops = Stops1 + Stops2
                Stopp = (Stops * teamMins) / (teamPoss * iMins)
                DERating = 100 * (oppPoints / teamPoss)
                DpScore = oppPoints / (oppFGM + (1 - (1 - (oppFTm / oppFTa)) ** 2) * oppFTa * 0.4)
                DERi = DERating + 0.2 * (100 * DpScore * (1 - Stopp) - DERating)

                avStats[indPl][43][0] = round(OERi,2)
                avStats[indPl][44][0] = round(DERi,2)
                lNeti = float(OERi - DERi)
                avStats[indPl][45][0] = round(lNeti,2)



def parse_stats_scratch_team(statsPlayers, game, indPl, sType, bAgainst):
    lNames = []
    lNames.append(statsPlayers[game][0])
    lTypes = []
    lTypes.append(sType)
    lGames = []
    lGames.append(int(1))
    lMins = []
    lMins.append(int(time2secs(statsPlayers[game][3])))
    lPts = []
    lPts.append(int(statsPlayers[game][4]))
    lt2S = []
    it2S = int(statsPlayers[game][5].split("/")[0])
    lt2S.append(it2S)
    lt2A = []
    it2A = int(statsPlayers[game][5].split("/")[1])
    lt2A.append(it2A)
    lt2p = []
    if it2A == 0:
        lt2p.append(round(0.0,2))
    else:
        lt2p.append(round(float(it2S)/it2A,2))
    lt3S = []
    it3S = int(statsPlayers[game][6].split("/")[0])
    lt3S.append(it3S)
    lt3A = []
    it3A = int(statsPlayers[game][6].split("/")[1])
    lt3A.append(it3A)
    lt3p = []
    if it3A == 0:
        lt3p.append(round(0.0, 2))
    else:
        lt3p.append(round(float(it3S)/it3A,2))
    lt1S = []
    it1S = int(statsPlayers[game][7].split("/")[0])
    lt1S.append(it1S)
    lt1A = []
    it1A = int(statsPlayers[game][7].split("/")[1])
    lt1A.append(it1A)
    lt1p = []
    if it1A == 0:
        lt1p.append(round(0.0, 2))
    else:
        lt1p.append(round(float(it1S)/it1A,2))
    lrOf = []
    lrOf.append(int(statsPlayers[game][8]))
    lrDef = []
    lrDef.append(int(statsPlayers[game][9]))
    lrReb = []
    lrReb.append(int(statsPlayers[game][8]) + int(statsPlayers[game][9]))
    lAssis = []
    lAssis.append(int(statsPlayers[game][10]))
    lRec = []
    lRec.append(int(statsPlayers[game][11]))
    lPer = []
    lPer.append(int(statsPlayers[game][12]))
    lTapF = []
    lTapF.append(int(statsPlayers[game][13]))
    lTapC = []
    lTapC.append(int(statsPlayers[game][14]))
    lMat = []
    lMat.append(int(statsPlayers[game][15]))
    lFalC = []
    lFalC.append(int(statsPlayers[game][16]))
    lFalF = []
    lFalF.append(int(statsPlayers[game][17]))
    lVal = []
    lVal.append(int(statsPlayers[game][18]))
    lPoss = []
    lPoss.append(0)
    lPace = []
    lPace.append(0)
    lOER = []
    lOER.append(0)
    lEffPer = []
    lEffPer.append(0)
    lPlayPer = []
    lPlayPer.append(0)
    lt1R =[]
    lt1R.append(0)
    lOfRebR = []
    lOfRebR.append(0)
    lDefRebR = []
    lDefRebR.append(0)
    lAssR = []
    lAssR.append(0)
    lPerR = []
    lPerR.append(0)
    lPerPas = []
    lPerPas.append(int(statsPlayers[game][19]))
    lPerBal = []
    lPerBal.append(int(statsPlayers[game][20]))
    lPerOthers = []
    lPerOthers.append(int(statsPlayers[game][21]))
    lFalTir = []
    lFalTir.append(int(statsPlayers[game][22]))
    lFalNoTir = []
    lFalNoTir.append(int(statsPlayers[game][23]))
    lTecnica = []
    lTecnica.append(int(statsPlayers[game][24]))
    lAnti = []
    lAnti.append(int(statsPlayers[game][25]))
    lOff = []
    lOff.append(int(statsPlayers[game][26]))
    lPerPasR = []
    lPerPasR.append(0)
    lPerBalR = []
    lPerBalR.append(0)
    lPerOthersR = []
    lPerOthersR.append(0)
    lOfRebWt = []
    lOfRebWt.append(0)
    lAssFT = []
    lAssFT.append(int(statsPlayers[game][27]))
    lAss2P = []
    lAss2P.append(int(statsPlayers[game][28]))
    lAss3P = []
    lAss3P.append(int(statsPlayers[game][29]))
    lAssFTR = []
    lAssFTR.append(0)
    lAss2PR = []
    lAss2PR.append(0)
    lAss3PR = []
    lAss3PR.append(0)
    lPointsAssist = []
    lPointsAssist.append(0)
    lPointsAssistR = []
    lPointsAssistR.append(0)
    lOfReb2p = []
    lOfReb2p.append(int(statsPlayers[game][33]))
    lOfReb3p = []
    lOfReb3p.append(int(statsPlayers[game][34]))
    lOfReb2pR = []
    lOfReb2pR.append(0)
    lOfReb3pR = []
    lOfReb3pR.append(0)
    # UsT3
    lu3p = []
    if it3A == 0:
        lu3p.append(round(0.0,2))
    else:
        lu3p.append(round(float(it3A) / (float(it2A)+float(it3A)),2))
    ltcS = []
    itcS = it2S+it3S
    ltcS.append(itcS)
    ltcA = []
    itcA = it2A+it3A
    ltcA.append(itcA)
    ltcp = []
    if itcA == 0:
        ltcp.append(round(0.0, 2))
    else:
        ltcp.append(round(float(itcS)/itcA,2))

    return [lNames, lTypes, lGames, lMins, lPts, lt2S, lt2A, lt2p, lt3S, lt3A, lt3p, lt1S, lt1A, lt1p, lrOf, lrDef,  lrReb, lAssis, lRec, lPer, lTapF, lTapC, lMat, lFalC, lFalF, lVal, lPoss, lPace, lOER, lEffPer, lPlayPer, lt1R, lDefRebR, lOfRebR, lAssR, lPerR, lPerPas, lPerBal, lPerOthers, lFalTir, lFalNoTir, lTecnica, lAnti, lOff, lPerPasR, lPerBalR, lPerOthersR, lOfRebWt, lAssFT, lAss2P, lAss3P, lAssFTR, lAss2PR, lAss3PR, lPointsAssist, lPointsAssistR, lOfReb2p, lOfReb3p, lOfReb2pR, lOfReb3pR,lu3p,ltcS,ltcA,ltcp]


def parse_stats_existing_team(statsPlayers, game, indPl, avStats, iPlayer, sType, bAgainst):
    # N Games
    avStats[indPl][2][0] = (int(avStats[indPl][2][0]) + 1)
    # Minutes
    try:
        avStats[indPl][3][0] = avStats[indPl][3][0] + time2secs(statsPlayers[game][3])
    except:
        pass
    # Points
    avStats[indPl][4][0] = int(avStats[indPl][4][0]) + int(statsPlayers[game][4])
    # lt2
    t2SAux = int(statsPlayers[game][5].split("/")[0])
    t2AAux = int(statsPlayers[game][5].split("/")[1])
    avStats[indPl][5][0] = int(avStats[indPl][5][0]) + t2SAux
    avStats[indPl][6][0] = int(avStats[indPl][6][0]) + t2AAux
    try:
        avStats[indPl][7][0] = round(float(avStats[indPl][5][0]) / float(avStats[indPl][6][0]),2)
    except:
        avStats[indPl][7][0] = 0
    # lt3
    t3SAux = int(statsPlayers[game][6].split("/")[0])
    t3AAux = int(statsPlayers[game][6].split("/")[1])
    avStats[indPl][8][0] = int(avStats[indPl][8][0]) + t3SAux
    avStats[indPl][9][0] = int(avStats[indPl][9][0]) + t3AAux
    try:
        avStats[indPl][10][0] = round(float(avStats[indPl][8][0]) / float(avStats[indPl][9][0]),2)
    except:
        avStats[indPl][10][0] = 0
    # lt1
    t1SAux = int(statsPlayers[game][7].split("/")[0])
    t1AAux = int(statsPlayers[game][7].split("/")[1])
    avStats[indPl][11][0] = int(avStats[indPl][11][0]) + t1SAux
    avStats[indPl][12][0] = int(avStats[indPl][12][0]) + t1AAux
    try:
        avStats[indPl][13][0] = round(float(avStats[indPl][11][0]) / float(avStats[indPl][12][0]),2)
    except:
        avStats[indPl][13][0] = 0

    # Rebs
    rofAux = int(statsPlayers[game][8])
    rdefAux = int(statsPlayers[game][9])
    avStats[indPl][14][0] = int(avStats[indPl][14][0]) + rofAux
    avStats[indPl][15][0] = int(avStats[indPl][15][0]) + rdefAux
    avStats[indPl][16][0] = int(avStats[indPl][16][0]) + rofAux + rdefAux

    assisAux = int(statsPlayers[game][10])
    avStats[indPl][17][0] = int(avStats[indPl][17][0]) + assisAux
    recAux = int(statsPlayers[game][11])
    avStats[indPl][18][0] = int(avStats[indPl][18][0]) + recAux
    perAux = int(statsPlayers[game][12])
    avStats[indPl][19][0] = int(avStats[indPl][19][0]) + perAux
    tapAux = int(statsPlayers[game][13])
    avStats[indPl][20][0] = int(avStats[indPl][20][0]) + tapAux
    tapRAux = int(statsPlayers[game][14])
    avStats[indPl][21][0] = int(avStats[indPl][21][0]) + tapRAux
    matAux = int(statsPlayers[game][15])
    avStats[indPl][22][0] = int(avStats[indPl][22][0]) + matAux
    fcomAux = int(statsPlayers[game][16])
    avStats[indPl][23][0] = int(avStats[indPl][23][0]) + fcomAux
    frebAux = int(statsPlayers[game][17])
    avStats[indPl][24][0] = int(avStats[indPl][24][0]) + frebAux
    valAux = int(statsPlayers[game][18])
    avStats[indPl][25][0] = int(avStats[indPl][25][0]) + valAux
    # Perduda passe
    perPasAux = int(statsPlayers[game][19])
    avStats[indPl][36][0] = int(avStats[indPl][36][0]) + perPasAux
    # Perduda pilota
    perBalAux = int(statsPlayers[game][20])
    avStats[indPl][37][0] = int(avStats[indPl][37][0]) + perBalAux
    # Perduda altres
    perOthersAux = int(statsPlayers[game][21])
    avStats[indPl][38][0] = int(avStats[indPl][38][0]) + perOthersAux
    # Faltes de tir
    falTirAux = int(statsPlayers[game][22])
    avStats[indPl][39][0] = int(avStats[indPl][39][0]) + falTirAux
    # Faltes no de tir
    falNoTirAux = int(statsPlayers[game][23])
    avStats[indPl][40][0] = int(avStats[indPl][40][0]) + falNoTirAux
    # Tecn
    tecniAux = int(statsPlayers[game][24])
    avStats[indPl][41][0] = int(avStats[indPl][41][0]) + tecniAux
    # Antiesportives
    antiAux = int(statsPlayers[game][25])
    avStats[indPl][42][0] = int(avStats[indPl][42][0]) + antiAux
    # Ofensives
    offAux = int(statsPlayers[game][26])
    avStats[indPl][43][0] = int(avStats[indPl][43][0]) + offAux
    # Assist
    assFTAux = int(statsPlayers[game][27])
    avStats[indPl][48][0] = int(avStats[indPl][48][0]) + assFTAux
    ass2PAux = int(statsPlayers[game][28])
    avStats[indPl][49][0] = int(avStats[indPl][49][0]) + ass2PAux
    ass3PAux = int(statsPlayers[game][29])
    avStats[indPl][50][0] = int(avStats[indPl][50][0]) + ass3PAux
    # Reb ofensius 2p&3p
    ofReb2pAux = int(statsPlayers[game][33])
    avStats[indPl][56][0] = int(avStats[indPl][56][0]) + ofReb2pAux
    ofReb3pAux = int(statsPlayers[game][34])
    avStats[indPl][57][0] = int(avStats[indPl][57][0]) + ofReb3pAux

    # UsT3
    try:
        avStats[indPl][60][0] = round(float(avStats[indPl][9][0]) / (float(avStats[indPl][6][0])+float(avStats[indPl][9][0])),2)
    except:
        avStats[indPl][60][0] = 0
    # TC
    avStats[indPl][61][0] = int(avStats[indPl][5][0])+int(avStats[indPl][8][0])
    avStats[indPl][62][0] = int(avStats[indPl][6][0])+int(avStats[indPl][9][0])
    try:
        avStats[indPl][63][0] = round(float(avStats[indPl][61][0]) / float(avStats[indPl][62][0]),2)
    except:
        avStats[indPl][63][0] = 0
    avStats[indPl][1][0] = sType

def tot2Av(avStats, indPl):
    games = avStats[indPl][2][0]

    lP = [7, 10, 13, 26, 27, 28, 33, 34, 35, 36, 37, 38, 40, 43, 44, 45]
    avStats[indPl][3][0] = "%.2f" % round((float(avStats[indPl][3][0]/60)/float(games)),2)

    for iStat in range(4, 56):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])/float(games)),2)
            except:
                pass

    for iStat in range(59, 61):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])/float(games)),2)
            except:
                pass
    return avStats

def tot2AvTeam(avStats, indPl):
    games = avStats[indPl][2][0]

    lP = [7, 10, 13]
    avStats[indPl][3][0] = "%.2f" % round((float(avStats[indPl][3][0] / 60) / float(games)), 2)
    for iStat in range(4, 27):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0]) / float(games)), 2)
            except:
                pass
    for iStat in range(36, 44):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0]) / float(games)), 2)
            except:
                pass
    for iStat in range(48, 51):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0]) / float(games)), 2)
            except:
                pass
    for iStat in range(56, 58):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0]) / float(games)), 2)
            except:
                pass

    avStats[indPl][54][0] = "%.2f" % round((float(avStats[indPl][54][0]) / float(games)), 2)

    for iStat in range(61, 63):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])/float(games)),2)
            except:
                pass

    return avStats

def tot2Proj(avStats, indPl, mins):
    fFac = float(40)/float(mins)
    lP = [7, 10, 13]

    for iStat in range(4, 46):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])*fFac),2)
            except:
                pass

    return avStats

def parseGameData(iGame, players, stats, sType, statsPlayers, bTeam):
    try:
        game = statsPlayers[iGame]
    except:
        pass

    if bTeam == False:
        try:
            playersGame = game[0]
            for iPlayer in range(0, len(playersGame)):
                if playersGame[iPlayer] not in players:
                    players.append(playersGame[iPlayer])
                    stats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sType))
                else:
                    index = players.index(playersGame[iPlayer])
                    parse_stats_existing_player(statsPlayers, iGame, index, stats, iPlayer, sType)
        except:
            pass
    else:
        try:
            playersGame = game[0]
            if playersGame[0][-4:] == 'inst' or playersGame[0][-4:] == 'ival':
                bAgainst = False
            else:
                bAgainst = True

            if playersGame not in players:
                players.append(playersGame)
                stats.append(parse_stats_scratch_team(statsPlayers, iGame, 0, sType, bAgainst))
            else:
                index = players.index(playersGame)
                parse_stats_existing_team(statsPlayers, iGame, index, stats, 0, sType, bAgainst)
        except:
            pass

def parseGameDataTit(iGame, playersTit, titStats, playersBench, benchStats, stats, statsPlayers, sLang):
    game = statsPlayers[iGame]
    playersGame = game[0]
    titStatsAux = []
    benchStatsAux = []

    if sLang == 'Castellano':
        sRow = '4 Titular'
        sRow2 = '4 Banqueta'
    else:
        sRow = '4 Initial5'
        sRow2 = '4 Bench'

    for iPlayer in range(0, len(playersGame)):
        if stats[iGame][2][iPlayer] == True:
            titStatsAux.append(list(np.array(stats[iGame])[:,iPlayer]))
            if playersGame[iPlayer] not in playersTit:
                playersTit.append(playersGame[iPlayer])
                titStats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sRow))
            else:
                index = playersTit.index(playersGame[iPlayer])
                parse_stats_existing_player(statsPlayers, iGame, index, titStats, iPlayer, sRow)
        else:
            benchStatsAux.append(list(np.array(stats[iGame])[:,iPlayer]))
            if playersGame[iPlayer] not in playersBench:
                playersBench.append(playersGame[iPlayer])
                benchStats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sRow2))
            else:
                index = playersBench.index(playersGame[iPlayer])
                parse_stats_existing_player(statsPlayers, iGame, index, benchStats, iPlayer, sRow2)
    titStatsAux = list(np.transpose(np.array(titStatsAux)))
    benchStatsAux = list(np.transpose(np.array(benchStatsAux)))
    return [l.tolist() for l in titStatsAux],[l.tolist() for l in benchStatsAux]

def tryAppend(mat, iPlayer):
    try:
        tot2Av(mat, iPlayer)
    except:
        pass

def tryAppendTeam(mat, iPlayer):
    try:
        tot2AvTeam(mat, iPlayer)
    except:
        pass

def tryAppendProj(mat, iPlayer):
    try:
        mins = float(mat[iPlayer][3][0])
        tot2Proj(mat, iPlayer, mins)
    except:
        pass

def substBrackets(df, tag):
    df[tag] = df[tag].str.get(0).astype(float)

def get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast, sDir, iFase, targetTeam, sFase, bTeam, bProj, sLocal=None, sAway=None, sWin=None, sDif=None):

    if iFase != 1:
        iTotFases = int(np.ceil(float(len(statsPlayers)/3) / float(iFase))) # int(float(jorLast-jorFirst)/float(iFase))+1
    else:
        iTotFases = int(float(len(statsPlayers)/3)) # int(float(jorLast - jorFirst) / float(iFase))

    iTotLast = jorLast-iFase*iTotFases

    strPlayersTot = []
    avStatsTot = []
    strPlayersTotT = []
    avStatsTotT = []
    strPlayersTotAg = []
    avStatsTotAg = []

    if sLang == 'Castellano':
        if iFase == 1:
            sJor = 'Jornada '
            sSave = 'Jornades'
        else:
            sJor = 'Fase '
            sSave = 'Fases'
    else:
        if iFase == 1:
            sJor = 'Round '
            sSave = 'Rounds'
        else:
            sJor = 'Phase '
            sSave = 'Phases'

    if sLocal != None:
        bAddition = True
    else:
        bAddition = False

    statsPlayersAux = []
    for indFase in range(0,iTotFases):
        strPlayers = []
        avStats = []
        strPlayersT = []
        avStatsT = []
        strPlayersAg = []
        avStatsAg = []
        if indFase == iTotFases:
            nGames = (indFase)*iFase+iTotLast
        else:
            nGames = (indFase+1)*iFase

        iFirstGame = max(0, (indFase) * iFase)
        if indFase != (iTotFases-1):
            iLastGame = (indFase+1)*iFase
        else:
            iLastGame = ((indFase+1) * iFase)+iTotLast

        statsPlayersAux.append(statsPlayers[iFirstGame*3:iLastGame*3])
        bTitp = []
        for iGame in range((indFase)*iFase,nGames):
            iGame = iGame * 3
            parseGameData(iGame, strPlayers, avStats, sJor + str(indFase+1).zfill(2), statsPlayers, False)
            if bAddition:
                try:
                    bTitp.append(statsPlayers[iGame][2])
                except:
                    pass
            iGame = iGame + 1
            parseGameData(iGame, strPlayersT, avStatsT, sJor + str(indFase+1).zfill(2), statsPlayers, True)
            iGame = iGame + 1
            parseGameData(iGame, strPlayersAg, avStatsAg, sJor + str(indFase+1).zfill(2), statsPlayers, True)

        strPlayersTot.append(strPlayers)
        avStatsTot.append(avStats)
        strPlayersTotT.append(strPlayersT)
        avStatsTotT.append(avStatsT)
        strPlayersTotAg.append(strPlayersAg)
        avStatsTotAg.append(avStatsAg)

        if sLocal != None:
            avStatsTotT[indFase][0].append(sLocal[indFase])
            avStatsTotT[indFase][0].append(sAway[indFase])
            avStatsTotT[indFase][0].append(sWin[indFase])
            avStatsTotT[indFase][0].append(sDif[indFase])
            for iPlayer in range(0, len(avStatsTot[indFase])):
                avStatsTot[indFase][iPlayer].append(sLocal[indFase])
                avStatsTot[indFase][iPlayer].append(sAway[indFase])
                avStatsTot[indFase][iPlayer].append(sWin[indFase])
                avStatsTot[indFase][iPlayer].append(sDif[indFase])
                avStatsTot[indFase][iPlayer].append(bTitp[0][iPlayer])

    for indFase in range(0, iTotFases):
        computeAdvStats(statsPlayersAux[indFase], avStatsTot[indFase], avStatsTotT[indFase], avStatsTotAg[indFase])

    flat_avStatsTot = [item for sublist in avStatsTot for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTot)):
        tryAppend(flat_avStatsTot, iPlayer)

    flat_avStatsTotT = [item for sublist in avStatsTotT for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTotT)):
        tryAppend(flat_avStatsTotT, iPlayer)

    flat_avStatsTotAg = [item for sublist in avStatsTotAg for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTotAg)):
        tryAppend(flat_avStatsTotAg, iPlayer)

    stats2csvFase(flat_avStatsTot, sDir + '/p'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sSave + '.csv', bAddition, sLang)
    if bTeam:
        stats2csvFaseTeam(flat_avStatsTotT, flat_avStatsTotAg, sDir + '/t'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sSave + '.csv', bAddition, sLang)

    if bProj == True:
        for iPlayer in range(0, len(flat_avStatsTot)):
            tryAppendProj(flat_avStatsTot, iPlayer)
        stats2csvFase(flat_avStatsTot, sDir + '/p' + targetTeam + season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sFase + 'PeriodosProj.csv', bAddition)


def stats2csvFase(avStats,csvFile, bAddition, sLang):

    if sLang == 'Castellano':
        headers = ['Nom', 'Jornada', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'Reb. Ofensius', 'Reb. Defensius', 'Rebots', 'Assist', 'Recuperacions', 'Perd', 'Taps', 'Taps Recibidos', 'Mates', 'Faltes Comeses', 'Faltes Rebudes', 'Val', '% Asist', '% Tir Efec', '% Tir Verdader', 'GScore', 'TLr%', 'Possesions Anotades', 'Possesions No Anotades', 'Floor Percentage', 'Punts per Tir', '% Rebots', '% Rebots Def', '% Rebots Of', '% Recuperacions', 'Tocs', 'Us', 'Versatilitat', 'Win Scores', 'Eficiencia Ofensiva', 'Eficiencia Defensiva', 'Diferencia eficiencia', 'Perd Mal Pase','Perd Pilota Controlada','Altres Perd','Faltes de Tir','Faltes No de Tir','Tecn','Antieportives','Ofensives','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC','Num','Local', 'Visitant','Victoria','Diferencia','Titular']
    else:
        headers = ['Name', 'Round', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR', 'AST%', 'eFG%', 'TS%', 'GScore', 'FTR', 'Scored Poss.', 'Non-scored Poss.', 'Floor Percentage', 'PPS', 'TRB%', 'DRB%', 'ORB%', 'STL%', 'Touches', 'Usage', 'Versatility', 'Win Scores', 'OER', 'DER', 'Net','Pérdidas Mal Pase','Perdidas Balón Controlado','Otras Perdidas','Faltas de Tiro','Faltas No de Tiro','Técnicas','Antideportivas','Ofensivas','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','FGm','FGa','%FG','Num','Local', 'Away','Win','Difference','Initial 5']

    if bAddition == False:
        headers = headers[:-5]

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Jornada'
    else:
        sCon1 = 'Name'
        sCon2 = 'Round'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]

    if bAddition:
        iFac = 5
    else:
        iFac = 0
    for iStat in range(2, int(len(headers) - iFac)):
        substBrackets(df, headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csvTeam(avStats,last3Stats,homeStats,awayStats,winStats,lostStats,easyStats,toughStats,target1Stats,target2Stats,avStatsAg, last3StatsAg, homeStatsAg, awayStatsAg, winStatsAg, lostStatsAg, easyStatsAg, toughStatsAg, target1StatsAg, target2StatsAg,csvFile,sLang):
    if last3Stats != []:
        avStats.extend(last3Stats)
    if homeStats != []:
        avStats.extend(homeStats)
    if awayStats != []:
        avStats.extend(awayStats)
    if winStats != []:
        avStats.extend(winStats)
    if lostStats != []:
        avStats.extend(lostStats)
    if easyStats != []:
        avStats.extend(easyStats)
    if toughStats != []:
        avStats.extend(toughStats)
    if target1Stats != []:
        avStats.extend(target1Stats)
    if target2Stats != []:
        avStats.extend(target2Stats)
    if avStatsAg != []:
        avStats.extend(avStatsAg)
    if last3StatsAg != []:
        avStats.extend(last3StatsAg)
    if homeStatsAg != []:
        avStats.extend(homeStatsAg)
    if awayStatsAg != []:
        avStats.extend(awayStatsAg)
    if winStatsAg != []:
        avStats.extend(winStatsAg)
    if lostStatsAg != []:
        avStats.extend(lostStatsAg)
    if easyStatsAg != []:
        avStats.extend(easyStatsAg)
    if toughStatsAg != []:
        avStats.extend(toughStatsAg)
    if target1StatsAg != []:
        avStats.extend(target1StatsAg)
    if target2StatsAg != []:
        avStats.extend(target2StatsAg)

    if sLang == 'Castellano':
        headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'Reb. Ofensiuss', 'Reb. Defensiuss', 'Rebots', 'Assist', 'Recuperacions', 'Pèrdues', 'Taps', 'Taps Rebuts', 'Mates', 'Faltes Comeses', 'Faltes Rebudes', 'Val', 'Possesions', 'Ritme', 'OER', '% TC Efec', '% Jugada', 'Frec. TL', '% Reb Def', '% Reb Of', '% Assis', '% Perd','Perd Mal Pase','Perd Pilota Controlada','Altres Perd','Faltes de Tiro','Faltes No de Tir','Tecn','Antieportives','Faltes Ofensives','% Perd pase','%Perd pil control','%Perd altres','ORB_wt','AssistFT','Assist2P','Assist3P','% AssistFT','%Assist2P','%Assist3P','Punts amb assist','OER amb Asistència','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR',  'Possessions', 'Pace', 'OER', 'eFG%', 'Play%', 'FTA Rate', 'DRB%', 'ORB%', 'Assist%', 'TOV%','Pérdidas Mal Pase','Perdidas Balón Controlado','Otras Perdidas','Faltas de Tiro','Faltas No de Tiro','Técnicas','Antideportivas','Ofensivas','% Perd pase','%Perd balon','%Perd others','ORB_wt','AssistFT','Assist2P','Assist3P','% AssistFT','%Assist2P','%Assist3P','Puntos tras Assistencia','OER tras Asistencia','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC']

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Cond'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(2,len(headers)):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csvTeam_reduced(avStats,csvFile,sLang):

    avStats = get_stats_reduced_team(avStats)

    if sLang == 'Castellano':
        headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'FC', 'Poss', 'Ritme', 'OER', '% TC Efec', '% Jugada', 'Frec. TL','UsT3']
    else:
        headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'FC', 'Poss', 'Ritme', 'OER', '% TC Efec', '% Jugada', 'Frec. TL','UsT3']

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Cond'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(2,len(headers)):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csvFaseTeam(avStatsT,avStatsAg,csvFile, bAddition, sLang):
    avStatsT.extend(avStatsAg)

    if sLang == 'Castellano':
        headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'Reb. Ofensiuss', 'Reb. Defensiuss', 'Rebots', 'Assist', 'Recuperacions', 'Pèrdues', 'Taps', 'Taps Rebuts', 'Mates', 'Faltes Comeses', 'Faltes Rebudes', 'Val', 'Possesions', 'Ritme', 'OER', '% TC Efec', '% Jugada', 'Frec. TL', '% Reb Def', '% Reb Of', '% Assis', '% Perd','Perd Mal Pase','Perd Pilota Controlada','Altres Perd','Faltes de Tiro','Faltes No de Tir','Tecn','Antieportives','Faltes Ofensives','% Perd pase','%Perd pil control','%Perd altres','ORB_wt','AssistFT','Assist2P','Assist3P','% AssistFT','%Assist2P','%Assist3P','Punts amb assist','OER amb Asistència','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC','Local', 'Visitant','Victoria','Diferencia']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR',  'Possessions', 'Pace', 'OER', 'eFG%', 'Play%', 'FTA Rate', 'DRB%', 'ORB%', 'Assist%', 'TOV%','Pérdidas Mal Pase','Perdidas Balón Controlado','Otras Perdidas','Faltas de Tiro','Faltas No de Tiro','Técnicas','Antideportivas','Ofensivas','% Perd pase','%Perd balon','%Perd others','ORB_wt','AssistFT','Assist2P','Assist3P','% AssistFT','%Assist2P','%Assist3P','Puntos tras Assistencia','OER tras Asistencia','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC','Local', 'Away','Win','Difference']

    if bAddition == False:
        headers = headers[:-4]

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Cond'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStatsT, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    if bAddition:
        iFac = 4
    else:
        iFac = 0
    for iStat in range(2,int(len(headers)-iFac)):
        substBrackets(df,headers[iStat])


    df.sort_values([sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csv(avStats,last3Stats,homeStats,awayStats,titStats,benchStats,winStats,lostStats,easyStats,toughStats,target1Stats,target2Stats,csvFile,sLang):
    if last3Stats != []:
        avStats.extend(last3Stats)
    if homeStats != []:
        avStats.extend(homeStats)
    if awayStats != []:
        avStats.extend(awayStats)
    avStats.extend(titStats)
    avStats.extend(benchStats)
    if winStats != []:
        avStats.extend(winStats)
    if lostStats != []:
        avStats.extend(lostStats)
    if easyStats != []:
        avStats.extend(easyStats)
    if toughStats != []:
        avStats.extend(toughStats)
    if target1Stats != []:
        avStats.extend(target1Stats)
    if target2Stats != []:
        avStats.extend(target2Stats)
    if sLang == 'Castellano':
        headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'Reb. Ofensius', 'Reb. Defensius', 'Rebots', 'Assist', 'Recuperacions', 'Pèrdues', 'Taps', 'Taps Rebuts', 'Mates', 'Faltes Comeses', 'Faltas Rebudes', 'Val', '% Asist', '% Tir Efectiu', '% Tir Verdader', 'GScore', 'TLR', 'Possesions Anotades', 'Possesions No Anotades', 'Floor Percentage', 'Punts per Tir', '% Rebots', '% Rebots Def', '% Rebots Of', '% Recuperacions', 'Tocs', 'Us', 'Versatilitat', 'Win Scores', 'Eficiencia Ofensiva', 'Eficiencia Defensiva', 'Diferencia eficiencia','Pèrdues Mal Pase','Pèrdues Pilota Controlada','Altres Pèrdues','Faltes de Tir','Faltes No de Tir','Tecn','Antieportives','Faltes Ofensives','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC','Num']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR', 'AST%', 'eFG%', 'TS%', 'GScore', 'FTR', 'Scored Poss.', 'Non-scored Poss.', 'Floor Percentage', 'PPS', 'TRB%', 'DRB%', 'ORB%', 'STL%', 'Touches', 'Usage', 'Versatility', 'Win Scores', 'OER', 'DER', 'Net','TurnBP','TurnBall','TurnOthers','FShoot','FNoShoot','Tec','U','Off','Reb. Of 2p', 'Reb. Of 3p', '% Reb. Of 2p', '% Reb. Of 3p','UsT3','TC Anot','TC Fets','%TC','Num']

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Cond'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(2,int(len(headers))):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def get_stats_reduced(avStats):

    av_stats_reduced = []

    for i in range(0,len(avStats)):
        av_stats_reduced_player = []
        av_stats_reduced_player.append(avStats[i][62])
        for j in range(0,14):
            av_stats_reduced_player.append(avStats[i][j])
        av_stats_reduced_player.append(avStats[i][23])
        av_stats_reduced_player.append(avStats[i][27])
        av_stats_reduced_player.append(avStats[i][28])
        av_stats_reduced_player.append(avStats[i][30])
        av_stats_reduced_player.append(avStats[i][58])
        av_stats_reduced_player.append(avStats[i][34])
        av_stats_reduced_player.append(avStats[i][33])
        av_stats_reduced_player.append(avStats[i][40])
        av_stats_reduced_player.append(avStats[i][29])

        av_stats_reduced.append(av_stats_reduced_player)

    return  av_stats_reduced


def get_stats_reduced_team(avStats):

    av_stats_reduced = []

    for i in range(0,len(avStats)):
        av_stats_reduced_player = []
        for j in range(0,14):
            av_stats_reduced_player.append(avStats[i][j])
        av_stats_reduced_player.append(avStats[i][23])
        for j in range(26,32):
            av_stats_reduced_player.append(avStats[i][j])
        av_stats_reduced_player.append(avStats[i][60])

        av_stats_reduced.append(av_stats_reduced_player)

    return av_stats_reduced

def stats2csv_reduced(avStats,csvFile,sLang):

    avStats = get_stats_reduced(avStats)

    if sLang == 'Castellano':
        headers = ['Nom', 'Num', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3','T1 Anot', 'T1 Fets', '% T1', 'FC', '% Tir Ef', '% Tir Ver', 'FqTL', '%UsT3', 'Pt/TC', '%PosAnot', 'Us', 'GScore']
    else:
        headers = ['Nom', 'Num', 'Condition', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3','T1 Anot', 'T1 Fets', '% T1', 'FC', '% Tir Ef', '% Tir Ver', 'FqTL', '%UsT3', 'Pt/TC', '%PosAnot', 'Us', 'GScore']

    if sLang == 'Castellano':
        sCon1 = 'Nom'
        sCon2 = 'Cond'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(3,int(len(headers))):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)


def stats2csvTwice(avStats,csvFile):
    headers = ['Nom', 'Cond', 'Partits', 'Minuts', 'Punts', 'T2 Anot', 'T2 Fets', '% T2', 'T3 Anot', 'T3 Fets', '% T3', 'T1 Anot', 'T1 Fets', '% T1', 'Reb. Ofensius', 'Reb. Defensius', 'Rebots', 'Assist', 'Recuperacions', 'Pèrdues', 'Taps', 'Taps Rebuts', 'Mates', 'Faltas Comeses', 'Faltas Rebudes', 'Val', '% Asist', '% Tir Efec', '% True Shooting', 'GScore', 'TLR', 'Possesions Anotades', 'Possesiones No Anotades', 'Floor Percentage', 'Punts per Tir', '% Rebots', '% Rebots Def', '% Rebots Of', '% Recuperacions', 'Tocs', 'Us', 'Versatilitat', 'Win Scores', 'OER', 'DER', 'Net']

    df = DataFrame(avStats, columns=headers)
    df.sort_values(['Nom'], inplace=True)
    df.sort_values(['Cond'], inplace=True)

    df['Nom'] = df['Nom'].str[0]
    df['Cond'] = df['Cond'].str[0]
    for iStat in range(2,int(len(headers)-5)):
        substBrackets(df,headers[iStat])

    df.sort_values(['Nom', 'Cond'], inplace=True)
    df.to_csv(csvFile, index=False)



def getAvStats(statsPlayers, bHome, tipusPartit, bAgainst, bAgainst2, targetTeam,season, jorFirst, jorLast,sDir, strFase, bTeam, bProj, statsHome=None, statsAway=None, statsWin=None, statsLost=None, statsLast3=None, statsTop=None, statsBot=None, statsEasy=None, statsTough=None, sMinGames=None, sLang=None):
    players = []
    avStats = []
    playersT = []
    playersTAg = []
    teamStats = []
    teamStatsAg = []

    playersHome = []
    homeStats = []
    playersHomeT = []
    playersHomeTAg = []
    teamHomeStats = []
    teamHomeStatsAg = []

    playersAway = []
    awayStats = []
    playersAwayT = []
    playersAwayTAg = []
    teamAwayStats = []
    teamAwayStatsAg = []

    playersTit = []
    titStats = []

    playersBench = []
    benchStats = []

    playersLast3 = []
    last3Stats = []
    playersLast3T = []
    playersLast3TAg = []
    teamLast3Stats = []
    teamLast3StatsAg = []

    playersLost = []
    lostStats = []
    playersLostT = []
    playersLostTAg = []
    teamLostStats = []
    teamLostStatsAg = []

    playersWin = []
    winStats = []
    playersWinT = []
    playersWinTAg = []
    teamWinStats = []
    teamWinStatsAg = []

    playersEasy = []
    easyStats = []
    playersEasyT = []
    playersEasyTAg = []
    teamEasyStats = []
    teamEasyStatsAg = []

    playersTough = []
    toughStats = []
    playersToughT = []
    playersToughTAg = []
    teamToughStats = []
    teamToughStatsAg = []

    playersTarget1 = []
    target1Stats = []
    playersTarget1T = []
    playersTarget1TAg = []
    teamTarget1Stats = []
    teamTarget1StatsAg = []

    playersTarget2 = []
    target2Stats = []
    playersTarget2T = []
    playersTarget2TAg = []
    teamTarget2Stats = []
    teamTarget2StatsAg = []

    statsBench = []
    statsTit = []

    bCorrect = []
    for iGame in range(0, int(len(statsPlayers))):
        if statsPlayers[iGame][0] == []:
            bCorrect.append(False)
        else:
            bCorrect.append(True)

    if sLang == "Castellano":
        sGame = 'Partit'
        strAv = '1 Mitjana'
        sWin = '2 Victoria'
        sLost = '2 Derrota'
        sLocal = '3 Local'
        sAway = '3 Visitant'
        sEasy = '5 Facil'
        sEasyt = '4 Facil'
        sTough = '5 Dificil'
        sTought = '4 Dificil'
        sTop = '6 Equips Top'
        sTopt = '5 Equips Top'
        sBottom = '6 Equips Cua'
        sBottomt = '5 Equips Cua'
        sLast3 = '7 Ultims 3'
        sLast3t = '6 Ultims 3'
        strAvT = 'Mitjana'
        sCon = ' Rival'
    else:
        sGame = 'Game'
        strAv = '1 Average'
        sWin = '2 Win'
        sLost = '2 Lost'
        sLocal = '3 Local'
        sAway = '3 Away'
        sEasy = '5 Easy'
        sEasyt = '4 Easy'
        sTough = '5 Tough'
        sTought = '4 Tough'
        sTop = '6 Top Teams'
        sTopt = '5 Top Teams'
        sBottom = '6 Bot. Teams'
        sBottomt = '5 Bot. Teams'
        sLast3 = '7 Last 3'
        sLast3t = '6 Last 3'
        strAvT = 'Average'
        strAvTag = 'Average'
        sCon = ' Against'

    for iGame in range(0, int(len(statsPlayers)/3)):
        if bCorrect[iGame]:
            print(sGame + ' (' + str(iGame+1) + '/' + str(int(len(statsPlayers)/3)) + ')')
            #############################################
            iGame = iGame*3
            parseGameData(iGame, players, avStats, strAv,statsPlayers, False)
            if bHome[iGame] == True:
                parseGameData(iGame, playersHome, homeStats, sLocal,statsPlayers, False)
            else:
                parseGameData(iGame, playersAway, awayStats, sAway,statsPlayers, False)

            titStatsAux, benchStatsAux = parseGameDataTit(iGame, playersTit, titStats, playersBench, benchStats, statsPlayers, statsPlayers, sLang)

            statsTit.append(titStatsAux)
            statsTit.append(statsPlayers[iGame+1])
            statsTit.append(statsPlayers[iGame+2])
            statsBench.append(benchStatsAux)
            statsBench.append(statsPlayers[iGame + 1])
            statsBench.append(statsPlayers[iGame + 2])
#            if ((len(statsPlayers)/3)-(iGame/3)) < 4:
#                parseGameData(iGame, playersLast3, last3Stats, sLast3,statsPlayers, False)
            try:
                if tipusPartit[iGame][1] == 'L':
                    parseGameData(iGame, playersLost, lostStats,sLost,statsPlayers, False)
                else:
                    parseGameData(iGame, playersWin, winStats,sWin,statsPlayers, False)
            except:
                pass

            if tipusPartit[iGame][0] == 'E':
                parseGameData(iGame, playersEasy, easyStats,sEasy,statsPlayers, False)
            else:
                parseGameData(iGame, playersTough, toughStats,sTough,statsPlayers, False)

            if bAgainst[iGame] == True:
                parseGameData(iGame, playersTarget1, target1Stats,sTop,statsPlayers, False)

            if bAgainst2[iGame] == True:
                parseGameData(iGame, playersTarget2, target2Stats,sBottom,statsPlayers, False)

            #############################################
            iGameTeam = iGame+1
            parseGameData(iGameTeam, playersT, teamStats, strAv, statsPlayers, True)

            try:
                if bHome[iGameTeam] == True:
                    parseGameData(iGameTeam, playersHomeT, teamHomeStats, sLocal,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersAwayT, teamAwayStats, sAway,statsPlayers, True)

                if bAgainst[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget1T, teamTarget1Stats, sTopt,statsPlayers, True)

                if bAgainst2[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget2T, teamTarget2Stats, sBottomt,statsPlayers, True)

                if ((len(statsPlayers) / 3) - (iGame / 3)) < 4:
                    parseGameData(iGameTeam, playersLast3T, teamLast3Stats, sLast3t,statsPlayers, True)

                if tipusPartit[iGameTeam][1] == 'L':
                    parseGameData(iGameTeam, playersLostT, teamLostStats, sLost,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersWinT, teamWinStats, sWin,statsPlayers, True)

                if tipusPartit[iGameTeam][0] == 'E':
                    parseGameData(iGameTeam, playersEasyT, teamEasyStats, sEasyt,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersToughT, teamToughStats, sTought,statsPlayers, True)
            except:
                pass

            iGameTeam = iGame + 2
            parseGameData(iGameTeam, playersTAg, teamStatsAg, strAv + sCon,statsPlayers, True)
            try:
                if bHome[iGameTeam] == True:
                    parseGameData(iGameTeam, playersHomeTAg, teamHomeStatsAg, sLocal + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersAwayTAg, teamAwayStatsAg, sAway + sCon,statsPlayers, True)

                if bAgainst[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget1TAg, teamTarget1StatsAg, sTopt + sCon,statsPlayers, True)

                if bAgainst2[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget2TAg, teamTarget2StatsAg, sBottomt + sCon,statsPlayers, True)

                if ((len(statsPlayers) / 3) - (iGame / 3)) < 4:
                    parseGameData(iGameTeam, playersLast3TAg, teamLast3StatsAg, sLast3t + sCon,statsPlayers, True)

                if tipusPartit[iGameTeam][1] == 'L':
                    parseGameData(iGameTeam, playersLostTAg, teamLostStatsAg, sLost + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersWinTAg, teamWinStatsAg, sWin + sCon,statsPlayers, True)

                if tipusPartit[iGameTeam][0] == 'E':
                    parseGameData(iGameTeam, playersEasyTAg, teamEasyStatsAg, sEasyt + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersToughTAg, teamToughStatsAg, sTought + sCon,statsPlayers, True)
            except:
                pass

    computeAdvStats(statsPlayers, avStats, teamStats, teamStatsAg)
    if statsHome != None:
        if homeStats != []:
            computeAdvStats(statsHome, homeStats, teamHomeStats, teamHomeStatsAg)
        if awayStats != []:
            computeAdvStats(statsAway, awayStats, teamAwayStats, teamAwayStatsAg)
        computeAdvStats(statsTit, titStats)
        computeAdvStats(statsBench, benchStats)
        if lostStats != []:
            computeAdvStats(statsLost, lostStats, teamLostStats, teamLostStatsAg)
        if winStats != []:
            computeAdvStats(statsWin, winStats, teamWinStats, teamWinStatsAg)
        if easyStats != []:
            computeAdvStats(statsEasy, easyStats, teamEasyStats, teamEasyStatsAg)
        if toughStats != []:
            computeAdvStats(statsTough, toughStats, teamToughStats, teamToughStatsAg)
        if last3Stats != []:
            computeAdvStats(statsLast3, last3Stats, teamLast3Stats, teamLast3StatsAg)
        if target1Stats != []:
            computeAdvStats(statsTop,  target1Stats, teamTarget1Stats, teamTarget1StatsAg)
        if target2Stats != []:
            computeAdvStats(statsBot,  target2Stats, teamTarget2Stats, teamTarget2StatsAg)

    for iPlayer in range(0, len(avStats)):
        tryAppend(avStats, iPlayer)
        if homeStats != []:
            tryAppend(homeStats, iPlayer)
        if awayStats != []:
            tryAppend(awayStats, iPlayer)
        tryAppend(titStats, iPlayer)
        tryAppend(benchStats, iPlayer)
        if last3Stats != []:
            tryAppend(last3Stats, iPlayer)
        if lostStats != []:
            tryAppend(lostStats, iPlayer)
        if winStats != []:
            tryAppend(winStats, iPlayer)
        if easyStats != []:
            tryAppend(easyStats, iPlayer)
        if toughStats != []:
            tryAppend(toughStats, iPlayer)
        if target1Stats != []:
            tryAppend(target1Stats, iPlayer)
        if target2Stats != []:
            tryAppend(target2Stats, iPlayer)

    tryAppendTeam(teamStats, 0)
    if homeStats != []:
        tryAppendTeam(teamHomeStats, 0)
    if awayStats != []:
        tryAppendTeam(teamAwayStats, 0)
    if last3Stats != []:
        tryAppendTeam(teamLast3Stats, 0)
    if lostStats != []:
        tryAppendTeam(teamLostStats, 0)
    if winStats != []:
        tryAppendTeam(teamWinStats, 0)
    if easyStats != []:
        tryAppendTeam(teamEasyStats, 0)
    if toughStats != []:
        tryAppendTeam(teamToughStats, 0)
    if target1Stats != []:
        tryAppendTeam(teamTarget1Stats, 0)
    if target2Stats != []:
        tryAppendTeam(teamTarget2Stats, 0)
    tryAppendTeam(teamStatsAg, 0)
    if homeStats != []:
        tryAppendTeam(teamHomeStatsAg, 0)
    if awayStats != []:
        tryAppendTeam(teamAwayStatsAg, 0)
    if last3Stats != []:
        tryAppendTeam(teamLast3StatsAg, 0)
    if lostStats != []:
        tryAppendTeam(teamLostStatsAg, 0)
    if winStats != []:
        tryAppendTeam(teamWinStatsAg, 0)
    if easyStats != []:
        tryAppendTeam(teamEasyStatsAg, 0)
    if toughStats != []:
        tryAppendTeam(teamToughStatsAg, 0)
    if target1Stats != []:
        tryAppendTeam(teamTarget1StatsAg, 0)
    if target2Stats != []:
        tryAppendTeam(teamTarget2StatsAg, 0)

    avStatsArr = np.copy(np.array(avStats))
    stats2csv(avStats, last3Stats, homeStats, awayStats, titStats, benchStats, winStats, lostStats, easyStats, toughStats, target1Stats, target2Stats, sDir + '/p'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + strFase + '.csv', sLang)
    if bTeam:
        stats2csvTeam(teamStats, teamLast3Stats, teamHomeStats, teamAwayStats, teamWinStats, teamLostStats, teamEasyStats, teamToughStats, teamTarget1Stats, teamTarget2Stats, teamStatsAg, teamLast3StatsAg, teamHomeStatsAg, teamAwayStatsAg, teamWinStatsAg, teamLostStatsAg, teamEasyStatsAg, teamToughStatsAg, teamTarget1StatsAg, teamTarget2StatsAg, sDir + '/t'+targetTeam+season+ 'J' + str(jorFirst) + 'J' + str(jorLast) +  strFase + '.csv', sLang)

    stats2csv_reduced(avStats, sDir + '/rp'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + strFase + '.csv', sLang)
    if bTeam:
        stats2csvTeam_reduced(teamStats, sDir + '/rt'+targetTeam+season+ 'J' + str(jorFirst) + 'J' + str(jorLast) +  strFase + '.csv', sLang)


    namesArr = np.array(avStatsArr[:, 0])
    namesArr = np.array([str(x)[2:-2] for x in namesArr])
    gamesArr = np.array(avStatsArr[:, 2])
    gamesArr = np.array([int(x) for x in gamesArr])

    topStats = []

#TODO

    t1r, t2r, t3r, ut3, efg, fft, t1m = getShotStats(teamStats[0])
    barChart.shotsStats(targetTeam,t1r,t2r,t3r,ut3,efg,fft)
    barChart.shotsStats2(targetTeam,t1r,t2r,t3r,ut3,efg,fft)
    points, tc, oer, pointsAg, tcAg, der = getGlobalStats(teamStats[0],teamStatsAg)
    barChart.globalStats(targetTeam,points,tc,oer,pointsAg,tcAg,der)
    barChart.globalStats2(targetTeam,points,tc,oer,pointsAg,tcAg,der)
    barChart.globalStats3(targetTeam, points, tc, oer, pointsAg, tcAg, der, t1m, t1r)

    if sMinGames != None and sMinGames != '':
        iMinGames = int(sMinGames)
    else:
        iMinGames = np.max(gamesArr) / 2

    for iStat in range(3, len(avStats[0])):
        statArr = np.array(avStatsArr[:, iStat])
        statArr = np.array([float(x) for x in statArr])
        statArr = statArr*(gamesArr>iMinGames)
        inds = statArr.argsort()[::-1]
        sortedPlayers = namesArr[inds]
        topStats.append(sortedPlayers)
        sortedVal = statArr[inds]
        topStats.append(sortedVal)

    ranking2csv(topStats, sDir + '/r'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + strFase + '.csv', sLang)

def ranking2csv(topStats, csvFile, sLang):
    if sLang == 'Castellano':
        headers = ['Minuts (jugador)', 'Minuts (valor)', 'Punts (jugador)', 'Punts (valor)', 'T2 Anot (jugador)', 'T2 Anot (valor)', 'T2 Fets (jugador)', 'T2 Fets (valor)', '% T2 (jugador)', '% T2 (valor)', 'T3 Anot (jugador)', 'T3 Anot (valor)', 'T3 Fets (jugador)', 'T3 Fets (valor)', '% T3 (jugador)', '% T3 (valor)', 'T1 Anot (jugador)','T1 Anot (valor)', 'T1 Fets (jugador)','T1 Fets (valor)', '% T1 (jugador)','% T1 (valor)', 'Reb. Ofensius (jugador)', 'Reb. Ofensius (valor)', 'Reb. Defensius (jugador)', 'Reb. Defensius (valor)', 'Rebots (jugador)', 'Rebots (valor)', 'Asistencies (jugador)', 'Asistencies (valor)', 'Recuperades (jugador)', 'Recuperades (valor)', 'Perdues (jugador)', 'Perdues (valor)', 'Taps (jugador)', 'Taps (valor)', 'Taps Rebuts (jugador)', 'Taps Rebuts (valor)', 'Mates (jugador)', 'Mates (valor)', 'Faltes Comeses (jugador)', 'Faltes Comeses (valor)', 'Faltas Rebudes (jugador)', 'Faltas Rebudes (valor)', 'Val (jugador)', 'Val (valor)',  '% Asist (jugador)', '% Asist (valor)', '% Tir Efectiu (jugador)', '% Tiro Efectiu (valor)', '% Tir Verdader (jugador)', '% Tir Verdader (valor)', 'GScore (jugador)', 'GScore (valor)', 'TLR% (jugador)', 'TLR% (valor)', 'Possesions Anotades (jugador)', 'Possesiones Anotades (valor)', 'Possesions No Anotades (jugador)', 'Possesions No Anotades (valor)', 'Floor Percentage (jugador)', 'Floor Percentage (valor)', 'Punts per Tir (jugador)', 'Punts per Tir (valor)',  '% Rebots (jugador)', '% Rebots (valor)', '% Rebots Def (jugador)', '% Rebots Def (valor)',  '% Rebots Of (jugador)', '% Rebots Of (valor)',  '% Recuperacions (jugador)', '% Recuperacions (valor)',  'Tocs (jugador)', 'Tocs (valor)',  'Us (jugador)', 'Us (valor)', 'Versatilitat (jugador)', 'Versatilitat (valor)', 'Win Scores (jugador)',  'Win Scores (valor)', 'Eficiencia Ofensiva (jugador)', 'Eficiencia Ofensiva (valor)', 'Eficiencia Defensiva (jugador)', 'Eficiencia Defensiva (valor)', 'Diferencia Eficiencia (jugador)', 'Diferencia Eficiencia (valor)', 'Perdues Mal Pase (Jugador)','Perdues Mal Pase (Valor)','Perdues Pilota Controlada (jugador)','Perdues Pilota Controlada (valor)','Altres Perdues (jugador)','Altres Perdues (valor)','Faltes de Tir (jugador)','Faltas de Tir (valor)','Faltes No de Tir (jugador)','Faltes No de Tir (valor)','Tecn (jugador)','Tecn (valor)','Antieportives (jugador)','Antieportives (valor)','Faltes Ofensives (jugador)','Faltes Ofensives (valor)','Reb. Of 2p (jugador)','Reb. Of 2p (valor)', 'Reb. Of 3p (jugador)', 'Reb. Of 3p (valor)','% Reb. Of 2p (jugador)','% Reb. Of 2p (valor)','% Reb. Of 3p (jugador)','% Reb. Of 3p (valor)','UsT3 (jugador)','UsT3 (valor)','TC Anot (jugador)','TC Anot (valor)','TC Fets (jugador)','TC Fets (valor)','%TC (jugador)','%TC (valor)','Num (jugador)','Num (valor)']
    else:
        headers = ['Minutes (player)', 'Minutes (value)', 'Points (player)', 'Points (value)', '2PM (player)', '2PM (value)', '2PA (player)', '2PA (value)', '% 2P (player)', '% 2P (value)', '3PM (player)', '3PM (value)', '3PA (player)', '3PA (value)', '% 3P (player)', '% 3P (value)', 'FTM (player)','FTM (value)', 'FTA (player)','FTA (value)', '% FT (player)','% FT (value)', 'ORB (player)', 'ORB (value)', 'DRB (player)', 'DRB (value)', 'REB (player)', 'REB (value)', 'ASS (player)', 'ASS (value)', 'STL (player)', 'STL (value)', 'TOV (player)', 'TOV (value)', 'BLK (player)', 'BLK (value)', 'BLKr (player)', 'BLKr (value)', 'Dunks (player)', 'Dunks (value)', 'PF (player)', 'PF (value)', 'PFr (player)', 'PFr (value)', 'PIR (player)', 'PIR (value)',  'ASS% (player)', 'ASS% (value)', 'eFG% (player)', 'eFG% (value)', 'TS% (player)', 'TS% (value)', 'GScore (player)', 'GScore (value)', 'FTr (player)', 'FTr (value)', 'Scored Poss. (player)', 'Scored Poss. (value)', 'Non-scored Poss. (player)', 'Non-scored Poss. (value)', 'Floor Percentage (player)', 'Floor Percentage (value)', 'PPS (player)', 'PPS (value)',  'REB% (player)', 'REB% (value)', 'DRB% (player)', 'DRB% (value)',  'ORB% (player)', 'ORB% (value)',  'STL% (player)', 'STL% (value)',  'Touches (player)', 'Touches (value)',  'Usage (player)', 'Usage (value)', 'Versatility (player)', 'Versatility (value)', 'Win Scores (player)',  'Win Scores (value)', 'OER (player)', 'OER (value)', 'DER (player)', 'DER (value)', 'Net (player)', 'Net (value)','Pérdidas Mal Pase (Jugador)','Pérdidas Mal Pase (Valor)','Perdidas Balón Controlado (jugador)','Perdidas Balón Controlado (valor)','Otras Perdidas (jugador)','Otras Perdidas (valor)','Faltas de Tiro (jugador)','Faltas de Tiro (valor)','Faltas No de Tiro (jugador)','Faltas No de Tiro (valor)','Técnicas (jugador)','Técnicas (valor)','Antideportivas (jugador)','Antideportivas (valor)','Ofensivas (jugador)','Ofensivas (valor)','Reb. Of 2p (jugador)','Reb. Of 2p (valor)', 'Reb. Of 3p (jugador)', 'Reb. Of 3p (valor)','% Reb. Of 2p (jugador)','% Reb. Of 2p (valor)','% Reb. Of 3p (jugador)','% Reb. Of 3p (valor)','UsT3 (jugador)','UsT3 (valor)','TC Anot (jugador)','TC Anot (valor)','TC Fets (jugador)','TC Fets (valor)','%TC (jugador)','%TC (valor)','Num (jugador)','Num (valor)']

    df = DataFrame(np.transpose(topStats), columns=headers)
    df.to_csv(csvFile, index=False)

def filterPlayers(inPlayers,sPlayers):
    outPlayers = []
    aTrans = np.transpose(np.array(inPlayers))
    for p in range(0, aTrans.shape[0]):
        try:
            playInd = str(aTrans[p][0].replace('\n','').replace(',','')).split(' ')
            for iPlay in range(0, len(sPlayers)):
                if sPlayers[iPlay].replace(' ','') in playInd:
            # if len([i for i in sPlayers if i in playInd]) > 0:
                    outPlayers.append(aTrans[p])
        except:
            pass
    outPlayers = list(np.transpose(outPlayers))
    return outPlayers

def getShotStats(teamStats):

    t1r = teamStats[13][0]*100.0
    t2r = teamStats[7][0]*100.0
    t3r = teamStats[10][0]*100.0
    t1m = float(teamStats[12][0])
    ut3 = 100.0*float(teamStats[9][0])/(float(teamStats[6][0])+float(teamStats[9][0]))
    fft = teamStats[31][0]
    efg = teamStats[29][0]

    return  t1r,t2r,t3r,ut3,efg,fft,t1m

def getGlobalStats(teamStats,teamStatsAg):

    points = float(teamStats[4][0])
    tc = 0.96*(float(teamStats[6][0])+float(teamStats[9][0])+0.44*float(teamStats[12][0]))
    #tc = (float(teamStats[6][0])+float(teamStats[9][0]))
    oer = teamStats[28][0]
    teamStatsAg2 = teamStatsAg[0]
    pointsAg = float(teamStatsAg2[4][0])
    tcAg = float(teamStatsAg2[6][0])+float(teamStatsAg2[9][0])
    der = teamStatsAg2[28][0]

    return  points,tc,oer, pointsAg, tcAg, der