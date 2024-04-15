# encoding: utf-8
from tkinter import *
from tkinter import ttk
import GetAllGamesCommon
import GetAllLeagueCommon
import GetAllLeagueBothPlata
import unicodedata
from importlib import reload
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

system = platform.system()

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.TeamLabel = Label(self)
        self.text_team = ''
        self.SeasonLabel = Label(self)
        self.text_season = ''
        self.jFirstLabel = Label(self)
        self.text_jFirst = ''
        self.jLastLabel = Label(self)
        self.text_jLast = ''
        self.tTopLabel = Label(self)
        self.text_equiposTop = ''
        self.tBotLabel = Label(self)
        self.text_equiposBott = ''
        self.divisionLabel = Label(self)
        self.text_division = ''
        self.territorialLabel = Label(self)
        self.text_territorial = ''
        self.genderLabel = Label(self)
        self.text_gender = ''
        self.groupLabel = Label(self)
        self.text_group = ''
        self.folderLabel = Label(self)
        self.text_folder = ''
        self.perLabel = Label(self)
        self.text_periodos = ''
        self.confLabel = Label(self)
        self.text_conf = ''
        self.text_chrome = ''
        self.jugadoresLabel = Label(self)
        self.text_jugadores = ''
        self.minPartidosLabel = Label(self)
        self.text_minPartidos = ''
        self.chEquipoLabel = Label(self)
        self.checkEquipo = IntVar(value=1)
        self.chAllLabel = Label(self)
        self.checkAll = IntVar(value=1)
        self.checkProj = IntVar(value=0)
        self.chRankLabel = Label(self)
        self.checkRank = IntVar(value=1)
        self.language = StringVar(value="Castellano")
        #self.Options = ["Castellano", "English"]
        self.create_widgets()

    def create_widgets(self):
        self.create_season_widget()
        self.create_rounds_widget()
        self.create_target_widget()
        self.create_against1_widget()
        self.create_against2_widget()
        self.create_gender_widget()
        self.create_territorial_widget()
        self.create_division_widget()
        self.create_group_widget()
        self.create_conf_button()
        self.create_export_widget()
        self.create_folder()
        self.create_periodos_widget()
        self.create_conf_widget()
        self.create_players_widget()
        self.create_boxTeam_widget()
        self.create_boxGames_widget()
        self.create_language_widget()
        ###self.create_proj_widget()
        self.create_rank_widget()

    def create_target_widget(self):
        self.TeamLabel['text'] = '1. Equip:'
        self.TeamLabel.grid(row=1, column=0, sticky=W)
        #Label(self, text="1. Equipo:").grid(row=1, column=0, sticky=W)
        #self.LabelTeam.grid(row=1, column=0, sticky=W)
        self.text_team = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_team.grid(row=1, column=1, columnspan=1, sticky=W)
        self.text_team.insert(END, "LLIGA,BADAL,HOSPI")
        # self.text_team.configure(state="disabled")

    def create_season_widget(self):
        self.SeasonLabel['text'] = '2. Temporada:'
        self.SeasonLabel.grid(row=2, column=0, sticky=W)
        #self.SeasonLabel = Label(self, text="2. Temporada:").grid(row=2, column=0, sticky=W)
        self.text_season = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_season.grid(row=2, column=1, columnspan=1, sticky=W)
        self.text_season.insert(END, "2023")
        # self.text_season.configure(state="disabled")

    def create_gender_widget(self):
        self.genderLabel['text'] = '3. Gènere:'
        self.genderLabel.grid(row=3, column=0, sticky=W)
        self.text_gender = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_gender.grid(row=3, column=1, columnspan=1, sticky=W)
        self.text_gender.insert(END, "Masc")
        # self.text_division.configure(state="disabled")

    def create_territorial_widget(self):
        self.territorialLabel['text'] = '4. Territorial:'
        self.territorialLabel.grid(row=4, column=0, sticky=W)
        self.text_territorial = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_territorial.grid(row=4, column=1, columnspan=1, sticky=W)
        self.text_territorial.insert(END, "Catalunya")
        # self.text_division.configure(state="disabled")

    def create_division_widget(self):
        self.divisionLabel['text'] = '5. Categoria:'
        self.divisionLabel.grid(row=5, column=0, sticky=W)
        self.text_division = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_division.grid(row=5, column=1, columnspan=1, sticky=W)
        self.text_division.insert(END, "Copa Catalunya")
        # self.text_division.configure(state="disabled")

    def create_group_widget(self):
        self.groupLabel['text'] = '6. Grup:'
        self.groupLabel.grid(row=6, column=0, sticky=W)
        self.text_group = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_group.grid(row=6, column=1, columnspan=1, sticky=W)
        self.text_group.insert(END, "Pr,1")
        # self.text_division.configure(state="disabled")

    def create_rounds_widget(self):
        self.jFirstLabel['text'] = "7. Primera Jornada:"
        self.jFirstLabel.grid(row=7, column=0, sticky=W)
        self.jLastLabel['text'] = "8. Ultima Jornada:"
        self.jLastLabel.grid(row=8, column=0, sticky=W)

        self.text_jFirst = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jFirst.grid(row=7, column=1, columnspan=1, sticky=W)
        self.text_jFirst.insert(END, "1")
        # self.text_jFirst.configure(state="disabled")

        self.text_jLast = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jLast.grid(row=8, column=1, columnspan=1, sticky=W)
        self.text_jLast.insert(END, "1")
        # self.text_jLast.configure(state="disabled")

    def create_against1_widget(self):
        self.tTopLabel['text'] = "9. Equips Top:"
        self.tTopLabel.grid(row=9, column=0, sticky=W)
        self.text_equiposTop = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_equiposTop.grid(row=9, column=1, columnspan=1, sticky=W)
        self.text_equiposTop.insert(END, "")
        # self.text_equiposTop.configure(state="disabled")

    def create_against2_widget(self):
        self.tBotLabel['text'] = '10. Equips Cua:'
        self.tBotLabel.grid(row=10, column=0, sticky=W)
        self.text_equiposBott = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_equiposBott.grid(row=10, column=1, columnspan=1, sticky=W)
        self.text_equiposBott.insert(END, "")
        # self.text_equiposBott.configure(state="disabled")

    def create_periodos_widget(self):
        self.perLabel['text'] = "11. Intervals:"
        self.perLabel.grid(row=11, column=0, sticky=W)
        self.text_periodos = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_periodos.grid(row=11, column=1, columnspan=1, sticky=W)
        self.text_periodos.insert(END, "5")
        # self.text_periodos.configure(state="disabled")

    def create_players_widget(self):
        self.jugadoresLabel['text'] = "12. Jugadors:"
        self.jugadoresLabel.grid(row=12, column=0, sticky=W)
        self.text_jugadores = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jugadores.grid(row=12, column=1, columnspan=1, sticky=W)
        self.text_jugadores.insert(END, "")
        # self.text_jugadores.configure(state="disabled")

    def create_boxTeam_widget(self):
        self.chEquipoLabel['text'] = "Extreure Estadistístiques d'Equip:"
        self.chEquipoLabel.grid(row=15, column=0, sticky=W)
        self.checkButtonTeam = ttk.Checkbutton()
        #self.checkButtonTeam.configure(width=12, var=self.checkEquipo,height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonTeam.configure(width=2, var=self.checkEquipo)
        self.checkButtonTeam.grid(row=15, column=0, columnspan=1, sticky=W)
        if system == 'Windows':
            self.checkButtonTeam.place(x=290, y = 285)
        else:
            self.checkButtonTeam.place(x=305, y = 245)

    def create_boxGames_widget(self):
        self.chAllLabel['text'] = "Extraer Totes les Jornades:"
        self.chAllLabel.grid(row=14, column=0, sticky=W)
        self.checkButtonGames = ttk.Checkbutton()
        #self.checkButtonGames.configure(width=12, var=self.checkAll,height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonGames.configure(width=2, var=self.checkAll)
        # self.checkButtonGames.grid(row=11, column=0, columnspan=1, sticky=W)
        if system == 'Windows':
            self.checkButtonGames.place(x=290, y = 265)
        else:
            self.checkButtonGames.place(x=305, y = 225)

    def create_proj_widget(self):
        Label(self, text="Extreure Projeccions:").grid(row=13, column=0, sticky=W)
        self.checkButtonProj = ttk.Checkbutton()
        #self.checkButtonProj.configure(width=12, var=self.checkProj, height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonProj.configure(width=2, var=self.checkProj)
        self.checkButtonProj.grid(row=13, column=0, columnspan=1, sticky=W)
        self.checkButtonProj.place(x=305, y=265)

    def create_rank_widget(self):
        self.chRankLabel['text'] = "Extreure Rankings:"
        self.chRankLabel.grid(row=16, column=0, sticky=W)
        self.checkButtonRank = ttk.Checkbutton()
        if system == 'Linux':
            #self.checkButtonRank.configure(width=12, var=self.checkRank, height=1, relief=RIDGE, borderwidth=2)
            self.checkButtonRank.configure(width=12, var=self.checkRank)
        else:
            #self.checkButtonRank.configure(width=2, var=self.checkRank, height=1, relief=RIDGE, borderwidth=2)
            self.checkButtonRank.configure(width=2, var=self.checkRank)
        self.checkButtonRank.grid(row=16, column=0, sticky=W)
        if system == 'Windows':
            self.checkButtonRank.place(x=290, y=305)
        else:
            self.checkButtonRank.place(x=305, y=265)

        if system == 'Linux':
            self.minPartidosLabel['text'] = "Mínim Partits:"
            self.minPartidosLabel.place(x=350, y=267)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=460, y=265)
            self.text_minPartidos.insert(END, "")
        elif system == 'Windows':
            self.minPartidosLabel['text'] = "Mínim Partits:"
            self.minPartidosLabel.place(x=300, y=290)
            # Label(self, text="Minimo Partidos:").place(x=300, y=265)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=410, y=290)
            self.text_minPartidos.insert(END, "")
        else:
            self.minPartidosLabel['text'] = "Mínim Partits:"
            self.minPartidosLabel.place(x=300, y=265)
            #Label(self, text="Minimo Partidos:").place(x=300, y=265)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=410, y=265)
            self.text_minPartidos.insert(END, "")

    def create_export_widget(self):
        self.button_compare = ttk.Button()
        self.button_compare.configure(text="Extreure Estadístiques")
        self.button_compare.grid(row=21, column=1, sticky=W)
        self.button_compare["command"] = self.save_stats
        # self.button_compare.configure(state="disabled")
        # self.button_compare.place(x = 100, y = 320)

    def create_conf_button(self):
        self.button_conf = ttk.Button()
        self.button_conf.configure(text="Carregar Configuració")
        self.button_conf.grid()
        if system == 'Linux':
            self.button_conf.place(x=80, y=405)
        else:
            self.button_conf.place(x=110, y=400)
        # self.button_conf.place(x=110, y=400)
        self.button_conf["command"] = self.load_conf
        # self.button_conf.place(x = 100, y = 350)

    def create_conf_widget(self):
        self.confLabel['text'] = "Carpeta Configuració:"
        self.confLabel.grid(row=19, column=0, sticky=W)
        self.text_conf = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_conf.grid(row=19, column=1, columnspan=1, sticky=W)
        self.text_conf.insert(END, os.path.dirname(os.path.abspath(__file__)) + "/ValoresDefectoPLATA2.txt")

    def create_folder(self):
        self.folderLabel['text'] = 'Carpeta Destí:'
        self.folderLabel.grid(row=21, column=0, sticky=W)
        self.text_folder = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_folder.grid(row=21, column=1, columnspan=1, sticky=W)
        self.text_folder.insert(END, os.path.dirname(os.path.abspath(__file__)) + "/Reports")
        # self.text_folder.configure(state="disabled")

    def create_language_widget(self):
        # self.language_drop = ttk.OptionMenu(self,self.language,*self.Options).grid(row=24, column=0, sticky=W)
        # # self.language_drop.pack()
        self.changeLang = ttk.Button()
        self.changeLang.configure(text="Change Language")
        self.changeLang.grid()
        if system == 'Linux':
            self.changeLang.place(x=80, y=375)
        else:
            self.changeLang.place(x=112, y=365)
        self.changeLang["command"] = self.change_language

    def change_language(self):
        if self.language.get() == "Castellano":
            self.language = StringVar(value="English")
        else:
            self.language = StringVar(value="Castellano")

        if self.language.get() == "Castellano":
            #self.create_labels_cast()
            self.TeamLabel['text'] = '1. Equipo:'
            self.SeasonLabel['text'] = '2. Temporada:'
            self.genderLabel['text'] = '3. Gènere:'
            self.territorialLabel['text'] = '4. Territorial:'
            self.divisionLabel['text'] = '5. Categoria:'
            self.groupLabel['text'] = '6. Grup:'
            self.jFirstLabel['text'] = "7. Primera Jornada:"
            self.jLastLabel['text'] = "8. Ultima Jornada:"
            self.tTopLabel['text'] = "9. Equipos Top:"
            self.tBotLabel['text'] = '10. Equipos Cola'
            self.perLabel['text'] = "11. Intervalos:"
            self.jugadoresLabel['text'] = "12. Jugadores"
            self.chEquipoLabel['text'] = "Extraer Estadisticas de Equipo:"
            self.chAllLabel['text'] = "Extraer Todas las Jornadas:"
            self.chRankLabel['text'] = "Extraer Rankings:"
            self.minPartidosLabel['text'] = "Min. Partidos:"
            self.confLabel['text'] = "Carpeta Configuracion:"
            self.folderLabel['text'] = 'Carpeta Destino:'

            self.button_conf.configure(text="Cargar Configuracion")
            self.button_compare.configure(text="Extraer Estadisticas")
            self.changeLang.configure(text="Change Language")
        else:
            self.TeamLabel['text'] = '1. Team:'
            self.SeasonLabel['text'] = '2. Season:'
            self.genderLabel['text'] = '3. Gènere:'
            self.territorialLabel['text'] = '4. Territorial:'
            self.divisionLabel['text'] = '5. Categoria:'
            self.groupLabel['text'] = '6. Grup:'
            self.jFirstLabel['text'] = "7. First Round:"
            self.jLastLabel['text'] = "8. Last Round:"
            self.tTopLabel['text'] = "9. Top Teams:"
            self.tBotLabel['text'] = '10. Bottom Teams:'
            self.perLabel['text'] = "11. Intervals:"
            self.jugadoresLabel['text'] = "12. Players"
            self.chEquipoLabel['text'] = "Extract Team Stats:"
            self.chAllLabel['text'] = "Extract Stats from All Games:"
            self.chRankLabel['text'] = "Extract Player Rankings:"
            self.minPartidosLabel['text'] = "Minimum Games:"
            self.confLabel['text'] = "Configuration Folder:"
            self.folderLabel['text'] = 'Output Folder:'
            self.button_conf.configure(text="Load Configuration")
            self.button_compare.configure(text="Extract Statistics")
            self.changeLang.configure(text="Cambiar Idioma")

    def load_conf(self):
        f = open(str(unicodedata.normalize('NFKD', self.text_conf.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[2:-3], "r")
        text = f.read()
        parts = text.split('\n')[:-1]
        for part in range(0, len(parts)):
            if len(parts[part]) > 0:
                parts[part] = parts[part].split('=')[1]

        self.text_season.configure(state="normal")
        self.text_season.delete('1.0',END)
        self.text_season.insert(END, parts[1])

        self.text_periodos.configure(state="normal")
        self.text_periodos.delete('1.0',END)
        self.text_periodos.insert(END, parts[7])

        self.text_division.configure(state="normal")
        self.text_division.delete('1.0',END)
        self.text_division.insert(END, parts[1])

        self.text_gender.configure(state="normal")
        self.text_gender.delete('1.0',END)
        self.text_gender.insert(END, parts[1])

        self.text_territorial.configure(state="normal")
        self.text_territorial.delete('1.0',END)
        self.text_territorial.insert(END, parts[1])

        self.text_group.configure(state="normal")
        self.text_group.delete('1.0',END)
        self.text_group.insert(END, parts[2])

        self.text_equiposBott.configure(state="normal")
        self.text_equiposBott.delete('1.0', END)
        self.text_equiposBott.insert(END, parts[6])

        self.text_equiposTop.configure(state="normal")
        self.text_equiposTop.delete('1.0', END)
        self.text_equiposTop.insert(END, parts[5])

        self.text_team.configure(state="normal")
        self.text_team.delete('1.0', END)
        self.text_team.insert(END,parts[0])

        self.text_jFirst.configure(state="normal")
        self.text_jFirst.delete('1.0', END)
        self.text_jFirst.insert(END,parts[3])

        self.text_jLast.configure(state="normal")
        self.text_jLast.delete('1.0', END)
        self.text_jLast.insert(END, parts[4])

        self.text_jugadores.configure(state="normal")
        self.text_jugadores.delete('1.0', END)
        self.text_jugadores.insert(END, parts[8])

        self.button_compare.configure(state="normal")

    def save_stats(self):
        self.text_chrome = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'

        if self.checkAll.get() == 1:
            bAll = 1
        else:
            bAll = 0

        if self.checkEquipo.get() == 1:
            bTeam = 1
        else:
            bTeam = 0

        if self.checkProj.get() == 1:
            bProj = True
        else:
            bProj = False

        iBenIn = 2
        iEndIn = -3

        if iEndIn != 0:
            season = str(unicodedata.normalize('NFKD', self.text_season.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            gender = str(unicodedata.normalize('NFKD', self.text_gender.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            territorial = str(unicodedata.normalize('NFKD', self.text_territorial.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            division = str(unicodedata.normalize('NFKD', self.text_division.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            group = str(unicodedata.normalize('NFKD', self.text_group.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn].split(",")
        else:
            season = str(unicodedata.normalize('NFKD', self.text_season.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            division = str(unicodedata.normalize('NFKD', self.text_division.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()

        bUnaFase = False

        sLang = self.language.get()

        season_int = int(season)

        chrome_options = Options()
        # maximized window
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(self.text_chrome, chrome_options=chrome_options)

        phase = group[0]
        ngroup = group[1]

        if(season_int == 2023):
            html_doc = "https://www.basquetcatala.cat/competicions/resultats"

            driver.get(html_doc)
            popup=driver.find_element_by_partial_link_text("Accept")
            popup.click()
            a = driver.find_element_by_link_text("Resultats, Classificacions i Calendaris")
            a.click()
            select_g = Select(driver.find_element_by_id("genere"))
            options_g = select_g.options
            for option in options_g:
                if option.text.__contains__(gender):
                    option_selected = option.text
                    break

            select_g.select_by_visible_text(option_selected)
            time.sleep(1)

            select_t = Select(driver.find_element_by_id("territorial"))
            options_t = select_t.options
            for option in options_t:
                if option.text.__contains__(territorial):
                    option_selected = option.text
                    break
            select_t.select_by_visible_text(option_selected)
            time.sleep(1)

            select_d = Select(driver.find_element_by_id("categoria"))
            options_d = select_d.options
            for option in options_d:
                if option.text.__contains__(division):
                    option_selected = option.text
                    break

            select_d.select_by_visible_text(option_selected)
            time.sleep(1)

            select_gr = Select(driver.find_element_by_id("competicio"))
            options_gr = select_gr.options
            for option in options_gr:
                if option.text.__contains__(phase):
                    if option.text.__contains__(ngroup):
                        option_selected = option.text
                        break

            select_gr.select_by_visible_text(option_selected)
            time.sleep(1)

            c = driver.find_element_by_xpath('//*[@id="group-finder"]/div[6]/div/div/input')
            c.click()
            time.sleep(1)

            html_doc = driver.current_url + "/0"
        else:
            html_doc = "https://www.basquetcatala.cat/llistatCompeticions/temporades"

            driver.get(html_doc)
            popup=driver.find_element_by_partial_link_text("Accept")
            #popup=driver.find_element_by_xpath('//*[@id="cmpbntyestxt"]')
            popup.click()
            a = driver.find_element_by_partial_link_text(season)
            a.click()
            time.sleep(1)

            b = driver.find_element_by_partial_link_text(gender)
            b.click()
            time.sleep(1)

            c = driver.find_element_by_partial_link_text(territorial)
            c.click()
            time.sleep(1)

            d = driver.find_element_by_partial_link_text(division)
            d.click()
            time.sleep(1)

            e = driver.find_element_by_partial_link_text(phase)
            e.click()
            time.sleep(1)

            f = driver.find_element_by_partial_link_text(ngroup)
            f.click()
            time.sleep(1)

            html_doc = driver.current_url

        driver.close()

        if iEndIn != 0:
            targetTeam = str(unicodedata.normalize('NFKD', self.text_team.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()[iBenIn:iEndIn]
            againstTeams1 = str(unicodedata.normalize('NFKD', self.text_equiposTop.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn].split(',')
            againstTeams2 = str(unicodedata.normalize('NFKD', self.text_equiposBott.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn].split(',')
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').replace("\\\\","/")[iBenIn:iEndIn]
            sPeriodos = str(unicodedata.normalize('NFKD', self.text_periodos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            sPlayers = str(unicodedata.normalize('NFKD', self.text_jugadores.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            sMinGames = str(unicodedata.normalize('NFKD', self.text_minPartidos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
        else:
            targetTeam = str(unicodedata.normalize('NFKD', self.text_team.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()
            againstTeams1 = str(unicodedata.normalize('NFKD', self.text_equiposTop.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').split(',')
            againstTeams2 = str(unicodedata.normalize('NFKD', self.text_equiposBott.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').split(',')
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sPeriodos = str(unicodedata.normalize('NFKD', self.text_periodos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sPlayers = str(unicodedata.normalize('NFKD', self.text_jugadores.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sMinGames = str(unicodedata.normalize('NFKD', self.text_minPartidos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')

        targetTeams = targetTeam.replace(' ', '').split(',')
        if targetTeams[0] == 'Lliga' or targetTeams[0] == 'LLIGA':
            GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, season, jorFirst, jorLast, sDir, self.text_chrome, bTeam, sPlayers, bProj, "Copa", '', sMinGames, sLang, False, targetTeams)
            reload(GetAllLeagueCommon)
        else:
            for k in range(0, len(targetTeams)):
                if sDir[-1] == '/':
                    sDir = sDir[:-1]
                GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, ngroup, sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)
            reload(GetAllGamesCommon)

#if __name__ == '__main__':
root = Tk()
root.title("FCBQStats")
root.geometry("950x450")
root.columnconfigure(0, weight=1)
root.resizable(0, 0)

app = Application(root)
app.mainloop()
