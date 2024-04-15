# This is a sample Python script.

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np


def shotsStats(teamName, t1r, t2r, t3r, ut3, efg, fft):
    legend = ['%TL', '%T2', '%T3', '%UsT3', 'eFG', 'FqTL']
    values = []
    values.append(t1r)
    values.append(t2r)
    values.append(t3r)
    values.append(ut3)
    values.append(efg)
    values.append(fft)

    values2 = []
    values2.append(65)
    values2.append(43)
    values2.append(27)
    values2.append(40.8)
    values2.append(41.8)
    values2.append(20.8)

    values3 = []
    values3.append(61)
    values3.append(42)
    values3.append(27)
    values3.append(38)
    values3.append(41.4)
    values3.append(16)

    values4 = []
    values4.append(71)
    values4.append(48)
    values4.append(31)
    values4.append(41)
    values4.append(47.1)
    values4.append(20.4)

    valuesMean = [64, 44, 28, 40, 43, 18.1]

    y_err_max = []
    y_err_min = []

    for i in range(0, len(valuesMean)):
        y_err_max.append(values4[i] - valuesMean[i])
        y_err_min.append(valuesMean[i] - values3[i])

    y_err = [y_err_min, y_err_max]

    local = 'CB Artés'

    m1 = pd.DataFrame({
        local: values2,
        teamName: values,
        'C': values3,
    })

    width = .8
    m1[[local, teamName]].plot(kind='bar', width=width, color=['red', 'green'])
    m1['C'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend)

    # yPos = np.arange(len(legend))

    # plt.bar(yPos, values)
    # plt.xticks(yPos,legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shotsTest2.png")
    plt.close()


def shotsStats2(teamName, t1r, t2r, t3r, ut3, efg, fft):
    legend = ['%TL', '%T2', '%T3', '%UsT3']
    values = []
    values.append(t1r)
    values.append(t2r)
    values.append(t3r)
    values.append(ut3)

    values2 = []
    values2.append(65)
    values2.append(43)
    values2.append(27)
    values2.append(40.8)

    values3 = []
    values3.append(61)
    values3.append(42)
    values3.append(27)
    values3.append(38)

    values4 = []
    values4.append(71)
    values4.append(48)
    values4.append(31)
    values4.append(41)

    valuesMean = [64, 44, 28, 40]

    y_err_max = []
    y_err_min = []

    for i in range(0, len(valuesMean)):
        y_err_max.append(values4[i] - valuesMean[i])
        y_err_min.append(valuesMean[i] - values3[i])

    y_err = [y_err_min, y_err_max]

    local = 'CB Artés'

    m1 = pd.DataFrame({
        local: values2,
        teamName: values,
        'C': values3,
    })

    width = .8
    m1[[local, teamName]].plot(kind='bar', width=width, color=['red', 'green'])
    m1['C'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend)

    # yPos = np.arange(len(legend))

    # plt.bar(yPos, values)
    # plt.xticks(yPos,legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shotsTest3.png")
    plt.close()


def globalStats(teamName, points, tc, oer, pointsAg, tcAg, der):
    legend = ['PT', 'PT rival', 'TC', 'TC rival', 'PT/TC', 'PT/TC rival']
    values = []

    values.append(points)
    values.append(pointsAg)
    values.append(tc)
    values.append(tcAg)
    values.append(oer)
    values.append(der)

    values2 = []
    values2.append(60.9)
    values2.append(71.2)
    values2.append(58.3)
    values2.append(66.5)
    values2.append(104.5)
    values2.append(107)

    values3 = []
    values3.append(63.6)
    values3.append(64.5)
    values3.append(60.7)
    values3.append(60.1)
    values3.append(102.8)
    values3.append(104.2)

    values4 = []
    values4.append(71.7)
    values4.append(71.2)
    values4.append(66.2)
    values4.append(67.2)
    values4.append(111.6)
    values4.append(110.9)

    valuesMean = [66.7, 66.7, 64, 64, 94, 94]

    y_err_max = []
    y_err_min = []

    for i in range(0, len(valuesMean)):
        y_err_max.append(values4[i] - valuesMean[i])
        y_err_min.append(valuesMean[i] - values3[i])

    y_err = [y_err_min, y_err_max]

    local = 'CB Artés'

    m1 = pd.DataFrame({
        local: values2,
        teamName: values,
        'C': values3,
    })

    width = .8
    m1[[local, teamName]].plot(kind='bar', width=width, color=['red', 'green'])
    m1['C'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/globalStats.png")
    plt.close()


def globalStats2(teamName, points, tc, oer, pointsAg, tcAg, der):
    legend = ['PT', 'TC', 'PT/TC']
    values = []
    valuesAg = []

    values.append(points)
    valuesAg.append(pointsAg)
    values.append(tc)
    valuesAg.append(tcAg)
    values.append(oer)
    valuesAg.append(der)

    values2 = []
    values2Ag = []

    values2.append(68.5)
    values2Ag.append(73)
    values2.append(60.06)
    values2Ag.append(71)
    values2.append(129)
    values2Ag.append(103.89)

    values3 = []
    values3.append(63)
    values3.append(59.94)
    values3.append(91.98)

    values4 = []
    values4.append(71.06)
    values4.append(66.69)
    values4.append(103.89)

    valuesMean = [66.7, 64, 100]

    y_err_max = []
    y_err_min = []

    for i in range(0, len(valuesMean)):
        y_err_max.append(values4[i] - valuesMean[i])
        y_err_min.append(valuesMean[i] - values3[i])

    y_err = [y_err_min, y_err_max]

    local = 'CB Artés'

    m1 = pd.DataFrame({
        teamName: values,
        'Rival': valuesAg,
        # 'C' : values3,
    })

    width = .8
    m1[[teamName, 'Rival']].plot(kind='bar', width=width)
    # m1['C'].plot(color = 'black',marker='.',markersize=1,use_index = True,linestyle='',yerr=y_err,capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    plt.ylim([0, 130])
    ax.set_xticklabels(legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/globalStats3.png")
    plt.close()

    m2 = pd.DataFrame({
        local: values2,
        'Rival': values2Ag,
        # 'D': values3,
    })

    width = .8
    m2[[local, 'Rival']].plot(kind='bar', width=width)
    # m2['D'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    plt.ylim([0, 130])
    ax.set_xticklabels(legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/globalStatsArtes.png")
    plt.close()

    m3 = pd.DataFrame({
        local: values2,
        teamName: values,
        # 'D': values3,
    })

    width = .8
    m3[[local, teamName]].plot(kind='bar', width=width)
    # m2['D'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend)

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/globalStatsArtesRival.png")
    plt.close()


def globalStats3(teamName, points, tc, oer, pointsAg, tcAg, der, tla, tlRatio):
    legend = ['PT', 'TC', 'PT/TC']
    values = []
    valuesAg = []

    values.append(points)
    valuesAg.append(pointsAg)
    values.append(tc)
    valuesAg.append(tcAg)
    values.append(oer)
    valuesAg.append(der)

    values2 = []
    values2Ag = []

    values2.append(70.33)
    values2Ag.append(73)
    values2.append(66.17)
    values2Ag.append(71)
    values2.append(106.3)
    values2Ag.append(103.91)

    values3 = []
    values3.append(61.41)
    values3.append(65.89)
    values3.append(90.92)

    values4 = []
    values4.append(70.89)
    values4.append(71.78)
    values4.append(103.23)

    valuesMean = [69.7, 70, 102.5]

    y_err_max = []
    y_err_min = []

    for i in range(0, len(valuesMean)):
        y_err_max.append(values4[i] - valuesMean[i])
        y_err_min.append(valuesMean[i] - values3[i])

    y_err = [y_err_min, y_err_max]

    local = 'CB Artés'

    m3 = pd.DataFrame({
        local: values2,
        teamName: values,
        'D': valuesMean,
    })

    width = .8

    m3[[local, teamName]].plot(kind='bar', width=width, color=['#C94845', '#777777'])
    # m3[[local, teamName]].plot(kind='bar', width=width, color=['#b01e18', '#777777'])
    m3['D'].plot(color='black', marker='.', markersize=1, use_index=True, linestyle='', yerr=y_err, capsize=20)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend, rotation=45, ha='right')

    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/globalStatsArtesRival3.png")
    plt.close()


def shots(teams, t1a, t2a, t3a, t1_perc, t2_perc, t3_perc, local, against):
    t1a_sorted = [x for _, x in sorted(zip(t1a, teams))][::-1]
    t2a_sorted = [x for _, x in sorted(zip(t2a, teams))][::-1]
    t3a_sorted = [x for _, x in sorted(zip(t3a, teams))][::-1]
    t1_perc_sorted = [x for _, x in sorted(zip(t1_perc, teams))][::-1]
    t2_perc_sorted = [x for _, x in sorted(zip(t2_perc, teams))][::-1]
    t3_perc_sorted = [x for _, x in sorted(zip(t3_perc, teams))][::-1]

    t1a_position = []
    t2a_position = []
    t3a_position = []
    t1_perc_position = []
    t2_perc_position = []
    t3_perc_position = []

    n_teams = len(teams)

    for team in teams:
        t1a_position.append(n_teams - t1a_sorted.index(team))
        t2a_position.append(n_teams - t2a_sorted.index(team))
        t3a_position.append(n_teams - t3a_sorted.index(team))
        t1_perc_position.append(n_teams - t1_perc_sorted.index(team))
        t2_perc_position.append(n_teams - t2_perc_sorted.index(team))
        t3_perc_position.append(n_teams - t3_perc_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'T1': t1a_position,
        '%T1': t1_perc_position,
        'T2': t2a_position,
        '%T2': t2_perc_position,
        'T3': t3a_position,
        '%T3': t3_perc_position
    })
    # ------- PART 1: Create background

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories)

    n_teams_list = [i for i in range(1, n_teams + 1)]
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1, 4, 7, 10, 12], ["12", "9", "6", "3", "1"], color="grey", size=7)
    # plt.yticks(n_teams_list, ["12","11","10","9","8","7","6","5","4","3","2","1"], color="grey", size=7)
    plt.ylim(0, n_teams)

    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

    for i in range(0, n_teams):
        if teams.__getitem__(i).__contains__(local):
            index_artes = i
        elif teams.__getitem__(i).__contains__(against):
            index_visitor = i

    # Ind1
    values = df.loc[index_visitor].drop('Team').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=df.loc[index_visitor][0].removesuffix(" Equipo"))
    ax.fill(angles, values, 'b', alpha=0.1)

    # Ind2
    values = df.loc[index_artes].drop('Team').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=df.loc[index_artes][0].removesuffix(" Equipo"))
    ax.fill(angles, values, 'r', alpha=0.1)

    # Add legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.8])

    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))

    # Go through labels and adjust alignment based on where
    # it is in the circle.
    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    # Show the graph
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shots.png")
    plt.close()


def global_stats_comparison(teams, points, points_ag, tc, tc_ag, etc, etc_ag, tl_ratio, tl_ratio_ag, us_t3, us_t3_ag,
                            team_loc, team_visitor):
    n_teams = len(teams)

    points_mean = np.mean(points)
    points_ag_mean = np.mean(points_ag)
    tc_mean = np.mean(tc)
    tc_ag_mean = np.mean(tc_ag)
    etc_mean = np.mean(etc)
    etc_ag_mean = np.mean(etc_ag)
    tl_ratio_mean = np.mean(tl_ratio)
    tl_ratio_ag_mean = np.mean(tl_ratio_ag)
    us_t3_mean = np.mean(us_t3)
    us_t3_ag_mean = np.mean(us_t3_ag)

    points_std = np.std(points)
    points_ag_std = np.std(points_ag)
    tc_std = np.std(tc)
    tc_ag_std = np.std(tc_ag)
    etc_std = np.std(etc)
    etc_ag_std = np.std(etc_ag)
    tl_ratio_std = np.std(tl_ratio)
    tl_ratio_ag_std = np.std(tl_ratio_ag)
    us_t3_std = np.std(us_t3)
    us_t3_ag_std = np.std(us_t3_ag)

    team_loc_split = team_loc.split('-')
    team_loc_subname = team_loc_split[0]
    team_loc_color = 'red'
    if len(team_loc_split) > 1:
        team_loc_color = team_loc_split[1]

    team_visitor_split = team_visitor.split('-')
    team_visitor_subname = team_visitor_split[0]
    team_visitor_color = 'blue'
    if len(team_visitor_split) > 1:
        team_visitor_color = team_visitor_split[1]

    for i in range(0, n_teams):

        if teams.__getitem__(i).__contains__(team_loc_subname):
            index_local = i
        elif teams.__getitem__(i).__contains__(team_visitor_subname):
            index_visitor = i

    legend = ['PT', 'PT rival', 'Pos.Tir', 'Pos.Tir rival', '%eTC', '%eTC rival', 'FqTL', 'FqTL rival', 'UsT3',
              'UsT3 rival']
    values = []
    values.append(points[index_local])
    values.append(points_ag[index_local])
    values.append(tc[index_local])
    values.append(tc_ag[index_local])
    values.append(etc[index_local])
    values.append(etc_ag[index_local])
    values.append(tl_ratio[index_local])
    values.append(tl_ratio_ag[index_local])
    values.append(us_t3[index_local])
    values.append(us_t3_ag[index_local])

    values2 = []
    values2.append(points[index_visitor])
    values2.append(points_ag[index_visitor])
    values2.append(tc[index_visitor])
    values2.append(tc_ag[index_visitor])
    values2.append(etc[index_visitor])
    values2.append(etc_ag[index_visitor])
    values2.append(tl_ratio[index_visitor])
    values2.append(tl_ratio_ag[index_visitor])
    values2.append(us_t3[index_visitor])
    values2.append(us_t3_ag[index_visitor])

    values_mean = []
    values_mean.append(points_mean)
    values_mean.append(points_ag_mean)
    values_mean.append(tc_mean)
    values_mean.append(tc_ag_mean)
    values_mean.append(etc_mean)
    values_mean.append(etc_ag_mean)
    values_mean.append(tl_ratio_mean)
    values_mean.append(tl_ratio_ag_mean)
    values_mean.append(us_t3_mean)
    values_mean.append(us_t3_ag_mean)

    values_std = []
    values_std.append(points_std)
    values_std.append(points_ag_std)
    values_std.append(tc_std)
    values_std.append(tc_ag_std)
    values_std.append(etc_std)
    values_std.append(etc_ag_std)
    values_std.append(tl_ratio_std)
    values_std.append(tl_ratio_ag_std)
    values_std.append(us_t3_std)
    values_std.append(us_t3_ag_std)

    y_err = [values_std, values_std]

    team_local_name = teams[index_local].removesuffix(" Equipo")
    team_visitor_name = teams[index_visitor].removesuffix(" Equipo")

    team_local_subname = ''
    if len(team_local_name) > 40:
        team_local_name_split = team_local_name.split(' ')
        for i in range(2, len(team_local_name_split)):
            team_local_subname += team_local_name_split[i] + ' '
    else:
        team_local_subname = team_local_name

    team_visitor_subname = ''
    if len(team_visitor_name) > 40:
        team_visitor_name_split = team_visitor_name.split(' ')
        for i in range(2, len(team_visitor_name_split)):
            team_visitor_subname += team_visitor_name_split[i] + ' '
    else:
        team_visitor_subname = team_visitor_name

    m1 = pd.DataFrame({
        team_local_subname: values,
        team_visitor_subname: values2,
        'Mean': values_mean,
    })

    width = 0.8
    m1[[team_local_subname, team_visitor_subname]].plot(kind='bar', width=width, color=[team_loc_color, team_visitor_color])
    m1['Mean'].plot(color='black', marker='_', markersize=4, use_index=True, linestyle='', yerr=y_err, capsize=2,
                    capthick=2)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend, rotation=45, ha='right')

    # plt.show()
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/global_stats_comparison_" + str(index_local) + "_" + str(
        index_visitor) + ".png", dpi=300, bbox_inches='tight')
    plt.close()

def global_stats_comparison4(teams, points, points_ag, tc, tc_ag, etc, etc_ag, tl_ratio, tl_ratio_ag, us_t3, us_t3_ag,
                             team1, team2, team3, team4):
    n_teams = len(teams)

    points_mean = np.mean(points)
    points_ag_mean = np.mean(points_ag)
    tc_mean = np.mean(tc)
    tc_ag_mean = np.mean(tc_ag)
    etc_mean = np.mean(etc)
    etc_ag_mean = np.mean(etc_ag)
    tl_ratio_mean = np.mean(tl_ratio)
    tl_ratio_ag_mean = np.mean(tl_ratio_ag)
    us_t3_mean = np.mean(us_t3)
    us_t3_ag_mean = np.mean(us_t3_ag)

    points_std = np.std(points)
    points_ag_std = np.std(points_ag)
    tc_std = np.std(tc)
    tc_ag_std = np.std(tc_ag)
    etc_std = np.std(etc)
    etc_ag_std = np.std(etc_ag)
    tl_ratio_std = np.std(tl_ratio)
    tl_ratio_ag_std = np.std(tl_ratio_ag)
    us_t3_std = np.std(us_t3)
    us_t3_ag_std = np.std(us_t3_ag)

    team1_split = team1.split('-')
    team1_subname = team1_split[0]
    team1_color = 'red'
    if len(team1_split) > 1:
        team1_color = team1_split[1]

    team2_split = team2.split('-')
    team2_subname = team2_split[0]
    team2_color = 'blue'
    if len(team2_split) > 1:
        team2_color = team2_split[1]

    team3_split = team3.split('-')
    team3_subname = team3_split[0]
    team3_color = 'red'
    if len(team3_split) > 1:
        team3_color = team3_split[1]

    team4_split = team4.split('-')
    team4_subname = team4_split[0]
    team4_color = 'blue'
    if len(team4_split) > 1:
        team4_color = team4_split[1]

    for i in range(0, n_teams):

        if teams.__getitem__(i).__contains__(team1_subname):
            index1 = i
        elif teams.__getitem__(i).__contains__(team2_subname):
            index2 = i
        elif teams.__getitem__(i).__contains__(team3_subname):
            index3 = i
        elif teams.__getitem__(i).__contains__(team4_subname):
            index4 = i

    legend = ['PT', 'PT rival', 'Pos.Tir', 'Pos.Tir rival', '%eTC', '%eTC rival', 'FqTL', 'FqTL rival', 'UsT3',
              'UsT3 rival']
    values = []
    values.append(points[index1])
    values.append(points_ag[index1])
    values.append(tc[index1])
    values.append(tc_ag[index1])
    values.append(etc[index1])
    values.append(etc_ag[index1])
    values.append(tl_ratio[index1])
    values.append(tl_ratio_ag[index1])
    values.append(us_t3[index1])
    values.append(us_t3_ag[index1])

    values2 = []
    values2.append(points[index2])
    values2.append(points_ag[index2])
    values2.append(tc[index2])
    values2.append(tc_ag[index2])
    values2.append(etc[index2])
    values2.append(etc_ag[index2])
    values2.append(tl_ratio[index2])
    values2.append(tl_ratio_ag[index2])
    values2.append(us_t3[index2])
    values2.append(us_t3_ag[index2])

    values3 = []
    values3.append(points[index3])
    values3.append(points_ag[index3])
    values3.append(tc[index3])
    values3.append(tc_ag[index3])
    values3.append(etc[index3])
    values3.append(etc_ag[index3])
    values3.append(tl_ratio[index3])
    values3.append(tl_ratio_ag[index3])
    values3.append(us_t3[index3])
    values3.append(us_t3_ag[index3])

    values4 = []
    values4.append(points[index4])
    values4.append(points_ag[index4])
    values4.append(tc[index4])
    values4.append(tc_ag[index4])
    values4.append(etc[index4])
    values4.append(etc_ag[index4])
    values4.append(tl_ratio[index4])
    values4.append(tl_ratio_ag[index4])
    values4.append(us_t3[index4])
    values4.append(us_t3_ag[index4])

    values_mean = []
    values_mean.append(points_mean)
    values_mean.append(points_ag_mean)
    values_mean.append(tc_mean)
    values_mean.append(tc_ag_mean)
    values_mean.append(etc_mean)
    values_mean.append(etc_ag_mean)
    values_mean.append(tl_ratio_mean)
    values_mean.append(tl_ratio_ag_mean)
    values_mean.append(us_t3_mean)
    values_mean.append(us_t3_ag_mean)

    values_std = []
    values_std.append(points_std)
    values_std.append(points_ag_std)
    values_std.append(tc_std)
    values_std.append(tc_ag_std)
    values_std.append(etc_std)
    values_std.append(etc_ag_std)
    values_std.append(tl_ratio_std)
    values_std.append(tl_ratio_ag_std)
    values_std.append(us_t3_std)
    values_std.append(us_t3_ag_std)

    y_err = [values_std, values_std]

    team1_name = teams[index1].removesuffix(" Equipo")
    team2_name = teams[index2].removesuffix(" Equipo")
    team3_name = teams[index3].removesuffix(" Equipo")
    team4_name = teams[index4].removesuffix(" Equipo")

    team1_subname = ''
    if len(team1_name) > 20:
        team_local_name_split = team1_name.split(' ')
        for i in range(2, len(team_local_name_split)):
            team1_subname += team_local_name_split[i] + ' '
    else:
        team1_subname = team1_name

    team2_subname = ''
    if len(team2_name) > 20:
        team_visitor_name_split = team2_name.split(' ')
        for i in range(2, len(team_visitor_name_split)):
            team2_subname += team_visitor_name_split[i] + ' '
    else:
        team2_subname = team2_name

    m1 = pd.DataFrame({
        team1_subname: values,
        team2_subname: values2,
        team3_name: values3,
        team4_name: values4,
        'Mean': values_mean,
    })

    width = 0.8
    m1[[team1_subname, team2_subname, team3_name, team4_name]].plot(kind='bar', width=width, color=[team1_color, team2_color, team3_color, team4_color])
    m1['Mean'].plot(color='black', marker='_', markersize=4, use_index=True, linestyle='', yerr=y_err, capsize=2,
                    capthick=2)

    ax = plt.gca()
    plt.xlim([-width, len(legend)])
    ax.set_xticklabels(legend, rotation=45, ha='right')

    # plt.show()
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/global_stats_comparison_" + str(index1) + "_" + str(
        index2) + '_' + str(index3) + "_" + str(index4) + ".png", dpi=300, bbox_inches='tight')
    plt.close()