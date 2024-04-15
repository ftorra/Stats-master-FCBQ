import time

from bs4 import BeautifulSoup
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


def getStats(html_doc, sChrome, playersHome, playersAway):

    chrome_options = Options()
    # maximized window
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
    driver.get(html_doc)
    a = driver.find_element_by_link_text("Directo")
    a.click()
    time.sleep(4)
    to_soup = driver.page_source
    driver.close()

    soup = BeautifulSoup(to_soup, 'lxml')

    play_by_play = soup.text.splitlines()

    asistencies_home = [[0] * (len(playersHome)) for _ in range((len(playersHome)))]
    assis_t1_home = [0] * (len(playersHome))
    assis_t2_home = [0] * (len(playersHome))
    assis_t3_home = [0] * (len(playersHome))
    t1_assis_home = [0] * (len(playersHome))
    t2_assis_home = [0] * (len(playersHome))
    t3_assis_home = [0] * (len(playersHome))
    perdues_pilota_home = [0] * (len(playersHome))
    perdues_passe_home = [0] * (len(playersHome))
    perdues_altres_home = [0] * (len(playersHome))
    personals_tir_home = [0] * (len(playersHome))
    personals_no_tir_home = [0] * (len(playersHome))
    ofensives_home = [0] * (len(playersHome))
    tecniques_home = [0] * (len(playersHome))
    antiesportives_home = [0] * (len(playersHome))
    rebots_ofensius_t2_home = [0] * (len(playersHome))
    rebots_ofensius_t3_home = [0] * (len(playersHome))
    rebots_defensius_t2_home = [0] * (len(playersHome))
    rebots_defensius_t3_home = [0] * (len(playersHome))

    asistencies_away = [[0] * (len(playersAway)) for _ in range((len(playersAway)))]
    assis_t1_away = [0] * (len(playersAway))
    assis_t2_away = [0] * (len(playersAway))
    assis_t3_away = [0] * (len(playersAway))
    t1_assis_away = [0] * (len(playersAway))
    t2_assis_away = [0] * (len(playersAway))
    t3_assis_away = [0] * (len(playersAway))
    perdues_pilota_away = [0] * (len(playersAway))
    perdues_passe_away = [0] * (len(playersAway))
    perdues_altres_away = [0] * (len(playersAway))
    personals_tir_away = [0] * (len(playersAway))
    personals_no_tir_away = [0] * (len(playersAway))
    ofensives_away = [0] * (len(playersAway))
    tecniques_away = [0] * (len(playersAway))
    antiesportives_away = [0] * (len(playersAway))
    rebots_ofensius_t2_away = [0] * (len(playersAway))
    rebots_ofensius_t3_away = [0] * (len(playersAway))
    rebots_defensius_t2_away = [0] * (len(playersAway))
    rebots_defensius_t3_away = [0] * (len(playersAway))
    
    home = len(playersHome)-1
    away = len(playersAway)-1

    previous_line = ""

    for i in range(len(play_by_play)-1, -1, -1):
        line = play_by_play.__getitem__(i)
        previous_action = ""

        if line.startswith("("):
            actions = line.split(",")
            if line == previous_line:
                continue
            if line.__contains__("Comienzo"):
                continue
            elif line.__contains__("Entra"):
                continue
            elif line.__contains__("Sale"):
                continue
            else:
                previous_line = line
                first_action = actions.__getitem__(0)
                for action in actions:
                    if action == " ":
                        continue
                    current_player, team = player_position(action, playersHome, playersAway)
                    if action.__contains__("Asistencias"):
                        previous_player, previous_team = player_position(previous_action, playersHome, playersAway)
                        if previous_action.__contains__("3Pts"):
                            if team == 1:
                                asistencies_home[home][home] += 1
                                asistencies_home[current_player][previous_player] += 1
                                assis_t3_home[current_player] += 1
                                t3_assis_home[previous_player] += 1
                                t3_assis_home[home] += 1
                                assis_t3_home[home] += 1
                            elif team == 2:
                                asistencies_away[away][away] += 1
                                asistencies_away[current_player][previous_player] += 1
                                assis_t3_away[current_player] += 1
                                t3_assis_away[previous_player] += 1
                                t3_assis_away[away] += 1
                                assis_t3_away[away] += 1
                        elif previous_action.__contains__("Tiros libres"):
                            if team == 1:
                                asistencies_home[home][home] += 1
                                asistencies_home[current_player][previous_player] += 1
                                assis_t1_home[current_player] += 1
                                t1_assis_home[previous_player] += 1
                                t1_assis_home[home] += 1
                                assis_t1_home[home] += 1
                            elif team == 2:
                                asistencies_away[away][away] += 1
                                asistencies_away[current_player][previous_player] += 1
                                assis_t1_away[current_player] += 1
                                t1_assis_away[previous_player] += 1
                                t1_assis_away[away] += 1
                                assis_t1_away[away] += 1
                        else:
                            if team == 1:
                                asistencies_home[home][home] += 1
                                asistencies_home[current_player][previous_player] += 1
                                assis_t2_home[current_player] += 1
                                t2_assis_home[previous_player] += 1
                                t2_assis_home[home] += 1
                                assis_t2_home[home] += 1
                            elif team == 2:
                                asistencies_away[away][away] += 1
                                asistencies_away[current_player][previous_player] += 1
                                assis_t2_away[current_player] += 1
                                t2_assis_away[previous_player] += 1
                                t2_assis_away[away] += 1
                                assis_t2_away[away] += 1
                    elif action.__contains__("TotReb") and first_action is not action:
                        first_player_player, first_team = player_position(first_action, playersHome, playersAway)
                        if team == first_team:
                            if previous_action.__contains__("3Pts"):
                                if team == 1:
                                    rebots_ofensius_t3_home[current_player] += 1
                                    rebots_ofensius_t3_home[home] += 1
                                elif team == 2:
                                    rebots_ofensius_t3_away[current_player] += 1
                                    rebots_ofensius_t3_away[away] += 1
                            else:
                                if team == 1:
                                    rebots_ofensius_t2_home[current_player] += 1
                                    rebots_ofensius_t2_home[home] += 1
                                elif team == 2:
                                    rebots_ofensius_t2_away[current_player] += 1
                                    rebots_ofensius_t2_away[away] += 1
                        else:
                            if previous_action.__contains__("3Pts"):
                                if team == 1:
                                    rebots_defensius_t3_home[current_player] += 1
                                    rebots_defensius_t3_home[home] += 1
                                elif team == 2:
                                    rebots_defensius_t3_away[current_player] += 1
                                    rebots_defensius_t3_away[away] += 1
                            else:
                                if team == 1:
                                    rebots_defensius_t2_home[current_player] += 1
                                    rebots_defensius_t2_home[home] += 1
                                elif team == 2:
                                    rebots_defensius_t2_away[current_player] += 1
                                    rebots_defensius_t2_away[away] += 1
                    elif action.__contains__("Pérdida"):
                        if line.__contains__("Balón Controlado"):
                            if team == 1:
                                perdues_pilota_home[current_player] += 1
                                perdues_pilota_home[home] += 1
                            elif team == 2:
                                perdues_pilota_away[current_player] += 1
                                perdues_pilota_away[away] += 1
                        elif line.__contains__("Mal pase"):
                            if team == 1:
                                perdues_passe_home[current_player] += 1
                                perdues_passe_home[home] += 1
                            elif team == 2:
                                perdues_passe_away[current_player] += 1
                                perdues_passe_away[away] += 1
                        else:
                            if team == 1:
                                perdues_altres_home[current_player] += 1
                                perdues_altres_home[home] += 1
                            elif team == 2:
                                perdues_altres_away[current_player] += 1
                                perdues_altres_away[away] += 1
                    elif action.__contains__("Personal"):
                        if action.__contains__("No de tiro"):
                            if team == 1:
                                personals_no_tir_home[current_player] += 1
                                personals_no_tir_home[home] += 1
                            elif team == 2:
                                personals_no_tir_away[current_player] += 1
                                personals_no_tir_away[away] += 1
                        else:
                            if team == 1:
                                personals_tir_home[current_player] += 1
                                personals_tir_home[home] += 1
                            elif team == 2:
                                personals_tir_away[current_player] += 1
                                personals_tir_away[away] += 1
                    elif action.__contains__("Ofensiva"):
                        if team == 1:
                            ofensives_home[current_player] += 1
                            ofensives_home[home] += 1
                        elif team == 2:
                            ofensives_away[current_player] += 1
                            ofensives_away[away] += 1
                    elif action.__contains__("Técnica"):
                        if team == 1:
                            tecniques_home[current_player] += 1
                            tecniques_home[home] += 1
                        elif team == 2:
                            tecniques_away[current_player] += 1
                            tecniques_away[away] += 1
                    elif action.__contains__("Antideportiva"):
                        if team == 1:
                            antiesportives_home[current_player] += 1
                            antiesportives_home[home] += 1
                        elif team == 2:
                            antiesportives_away[current_player] += 1
                            antiesportives_away[away] += 1
                    previous_action = action

    return [perdues_passe_home, perdues_pilota_home, perdues_altres_home, personals_tir_home, personals_no_tir_home, tecniques_home, antiesportives_home, ofensives_home, assis_t1_home, assis_t2_home, assis_t3_home, t1_assis_home, t2_assis_home, t3_assis_home, rebots_ofensius_t2_home, rebots_ofensius_t3_home, rebots_defensius_t2_home, rebots_defensius_t3_home], \
           [perdues_passe_away, perdues_pilota_away, perdues_altres_away, personals_tir_away, personals_no_tir_away, tecniques_away, antiesportives_away, ofensives_away, assis_t1_away, assis_t2_away, assis_t3_away, t1_assis_away, t2_assis_away, t3_assis_away, rebots_ofensius_t2_away, rebots_ofensius_t3_away, rebots_defensius_t2_away, rebots_defensius_t3_away]


def getEmptyStats(playersHome, playersAway):

    assis_t1_home = [0] * (len(playersHome))
    assis_t2_home = [0] * (len(playersHome))
    assis_t3_home = [0] * (len(playersHome))
    t1_assis_home = [0] * (len(playersHome))
    t2_assis_home = [0] * (len(playersHome))
    t3_assis_home = [0] * (len(playersHome))
    perdues_pilota_home = [0] * (len(playersHome))
    perdues_passe_home = [0] * (len(playersHome))
    perdues_altres_home = [0] * (len(playersHome))
    personals_tir_home = [0] * (len(playersHome))
    personals_no_tir_home = [0] * (len(playersHome))
    ofensives_home = [0] * (len(playersHome))
    tecniques_home = [0] * (len(playersHome))
    antiesportives_home = [0] * (len(playersHome))
    rebots_ofensius_t2_home = [0] * (len(playersHome))
    rebots_ofensius_t3_home = [0] * (len(playersHome))
    rebots_defensius_t2_home = [0] * (len(playersHome))
    rebots_defensius_t3_home = [0] * (len(playersHome))

    assis_t1_away = [0] * (len(playersAway))
    assis_t2_away = [0] * (len(playersAway))
    assis_t3_away = [0] * (len(playersAway))
    t1_assis_away = [0] * (len(playersAway))
    t2_assis_away = [0] * (len(playersAway))
    t3_assis_away = [0] * (len(playersAway))
    perdues_pilota_away = [0] * (len(playersAway))
    perdues_passe_away = [0] * (len(playersAway))
    perdues_altres_away = [0] * (len(playersAway))
    personals_tir_away = [0] * (len(playersAway))
    personals_no_tir_away = [0] * (len(playersAway))
    ofensives_away = [0] * (len(playersAway))
    tecniques_away = [0] * (len(playersAway))
    antiesportives_away = [0] * (len(playersAway))
    rebots_ofensius_t2_away = [0] * (len(playersAway))
    rebots_ofensius_t3_away = [0] * (len(playersAway))
    rebots_defensius_t2_away = [0] * (len(playersAway))
    rebots_defensius_t3_away = [0] * (len(playersAway))

    return [perdues_passe_home, perdues_pilota_home, perdues_altres_home, personals_tir_home, personals_no_tir_home,
            tecniques_home, antiesportives_home, ofensives_home, assis_t1_home, assis_t2_home, assis_t3_home,
            t1_assis_home, t2_assis_home, t3_assis_home, rebots_ofensius_t2_home, rebots_ofensius_t3_home,
            rebots_defensius_t2_home, rebots_defensius_t3_home], \
           [perdues_passe_away, perdues_pilota_away, perdues_altres_away, personals_tir_away, personals_no_tir_away,
            tecniques_away, antiesportives_away, ofensives_away, assis_t1_away, assis_t2_away, assis_t3_away,
            t1_assis_away, t2_assis_away, t3_assis_away, rebots_ofensius_t2_away, rebots_ofensius_t3_away,
            rebots_defensius_t2_away, rebots_defensius_t3_away]


def player_position(action, playersHome, playersAway):
    for i in range(0, len(playersHome)-1, 1):
        player = playersHome.__getitem__(i).split(",").__getitem__(0)
        if action.__contains__(player):
            return i, 1
    for i in range(0, len(playersAway)-1, 1):
        player = playersAway.__getitem__(i).split(",").__getitem__(0)
        if action.__contains__(player):
            return i, 2
    return -1, -1
