# This is a sample Python script.

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

def shots4(teams, t2a, t3a, t2r, t3r, poss, team_loc, team_visitor, team3, team4):
    poss_sorted = [x for _, x in sorted(zip(poss, teams))][::-1]
    t2a_sorted = [x for _, x in sorted(zip(t2a, teams))][::-1]
    t3a_sorted = [x for _, x in sorted(zip(t3a, teams))][::-1]
    t2r_sorted = [x for _, x in sorted(zip(t2r, teams))][::-1]
    t3r_sorted = [x for _, x in sorted(zip(t3r, teams))][::-1]

    poss_position = []
    t2a_position = []
    t3a_position = []
    t2r_position = []
    t3r_position = []

    n_teams = len(teams)

    for team in teams:
        poss_position.append(n_teams - poss_sorted.index(team))
        t2a_position.append(n_teams - t2a_sorted.index(team))
        t3a_position.append(n_teams - t3a_sorted.index(team))
        t2r_position.append(n_teams - t2r_sorted.index(team))
        t3r_position.append(n_teams - t3r_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'Possessions de Tir': poss_position,
        'T2': t2a_position,
        '%T2': t2r_position,
        'T3': t3a_position,
        '%T3': t3r_position
    })
    # ------- PART 1: Create background

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    index_local = -1
    index_visitor = -1

    team_loc_split = team_loc.split('-')
    team_loc_subname = team_loc_split[0]
    team_loc_color = 'red'
    if len(team_loc_split)>1:
        team_loc_color = team_loc_split[1]

    team_visitor_split = team_visitor.split('-')
    team_visitor_subname = team_visitor_split[0]
    team_visitor_color = 'blue'
    if len(team_visitor_split)>1:
        team_visitor_color = team_visitor_split[1]

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

        color_plot = 'blue'
        #for i in range(0, n_teams):
        if teams.__getitem__(i).__contains__(team_loc_subname):
            index_local = i
            color_plot = team_loc_color
        elif teams.__getitem__(i).__contains__(team_visitor_subname):
            index_visitor = i
            color_plot = team_visitor_color
        elif teams.__getitem__(i).__contains__(team3_subname):
            color_plot = team3_color
        elif teams.__getitem__(i).__contains__(team4_subname):
            color_plot = team4_color

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)

        # Draw y labels
        ax.set_rlabel_position(0)
        plt.yticks([1, 5, 8, 11, 14], ["14", "10", "7", "4", "1"], color="grey", size=7)
        # plt.yticks(n_teams_list, ["12","11","10","9","8","7","6","5","4","3","2","1"], color="grey", size=7)
        #plt.yticks([1, 3, 6, 8], ["8", "6", "3", "1"], color="grey", size=7)
        plt.ylim(0, n_teams)

        # ------- PART 2: Add plots

        # Ind1
        values = df.loc[i].drop('Team').values.flatten().tolist()
        values += values[:1]
        team_name_visitor = df.loc[i][0].removesuffix(" Equipo")
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=team_name_visitor, color=color_plot)
        ax.fill(angles, values, color_plot, alpha=0.1)

        # Ind2
        #values = df.loc[index_artes].drop('Team').values.flatten().tolist()
        #values += values[:1]
        #ax.plot(angles, values, linewidth=1, linestyle='solid', label=df.loc[index_artes][0].removesuffix(" Equip"))
        #ax.fill(angles, values, 'r', alpha=0.1)

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
        plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shoots_" + str(i) + ".png", dpi=300, bbox_inches='tight')
        plt.close()

def shots(teams, t2a, t3a, t2r, t3r, poss, team_loc, team_visitor):
    poss_sorted = [x for _, x in sorted(zip(poss, teams))][::-1]
    t2a_sorted = [x for _, x in sorted(zip(t2a, teams))][::-1]
    t3a_sorted = [x for _, x in sorted(zip(t3a, teams))][::-1]
    t2r_sorted = [x for _, x in sorted(zip(t2r, teams))][::-1]
    t3r_sorted = [x for _, x in sorted(zip(t3r, teams))][::-1]

    poss_position = []
    t2a_position = []
    t3a_position = []
    t2r_position = []
    t3r_position = []

    n_teams = len(teams)

    for team in teams:
        poss_position.append(n_teams - poss_sorted.index(team))
        t2a_position.append(n_teams - t2a_sorted.index(team))
        t3a_position.append(n_teams - t3a_sorted.index(team))
        t2r_position.append(n_teams - t2r_sorted.index(team))
        t3r_position.append(n_teams - t3r_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'Possessions de Tir': poss_position,
        'T2': t2a_position,
        '%T2': t2r_position,
        'T3': t3a_position,
        '%T3': t3r_position
    })
    # ------- PART 1: Create background

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    index_local = -1
    index_visitor = -1

    team_loc_split = team_loc.split('-')
    team_loc_subname = team_loc_split[0]
    team_loc_color = 'red'
    if len(team_loc_split)>1:
        team_loc_color = team_loc_split[1]

    team_visitor_split = team_visitor.split('-')
    team_visitor_subname = team_visitor_split[0]
    team_visitor_color = 'blue'
    if len(team_visitor_split)>1:
        team_visitor_color = team_visitor_split[1]

    for i in range(0, n_teams):

        #for i in range(0, n_teams):
        if teams.__getitem__(i).__contains__(team_loc_subname):
            index_local = i
        elif teams.__getitem__(i).__contains__(team_visitor_subname):
            index_visitor = i

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)

        # Draw y labels
        ax.set_rlabel_position(0)
        plt.yticks([1, 5, 8, 11, 14], ["14", "10", "7", "4", "1"], color="grey", size=7)
        # plt.yticks(n_teams_list, ["12","11","10","9","8","7","6","5","4","3","2","1"], color="grey", size=7)
        plt.ylim(0, n_teams)

        # ------- PART 2: Add plots

        # Ind1
        values = df.loc[i].drop('Team').values.flatten().tolist()
        values += values[:1]
        team_name_visitor = df.loc[i][0].removesuffix(" Equipo")
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=team_name_visitor)
        ax.fill(angles, values, 'b', alpha=0.1)

        # Ind2
        #values = df.loc[index_artes].drop('Team').values.flatten().tolist()
        #values += values[:1]
        #ax.plot(angles, values, linewidth=1, linestyle='solid', label=df.loc[index_artes][0].removesuffix(" Equip"))
        #ax.fill(angles, values, 'r', alpha=0.1)

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
        plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shoots_" + str(i) + ".png")
        plt.close()

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories)

    # Draw y labels
    ax.set_rlabel_position(0)
    plt.yticks([1, 5, 8, 11, 14], ["14", "10", "7", "4", "1"], color="grey", size=7)
    #plt.yticks([1, 3, 6, 8], ["8", "6", "3", "1"], color="grey", size=7)
    # plt.yticks(n_teams_list, ["12","11","10","9","8","7","6","5","4","3","2","1"], color="grey", size=7)
    plt.ylim(0, n_teams)

    # ------- PART 2: Add plots

    # Ind1
    values = df.loc[index_visitor].drop('Team').values.flatten().tolist()
    values += values[:1]
    team_name_visitor = df.loc[index_visitor][0].removesuffix(" Equipo")
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=team_name_visitor, color=team_visitor_color)
    ax.fill(angles, values, team_visitor_color, alpha=0.1)

    # Ind2
    values = df.loc[index_local].drop('Team').values.flatten().tolist()
    values += values[:1]
    team_name_local = df.loc[index_local][0].removesuffix(" Equipo")
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=team_name_local, color=team_loc_color)
    ax.fill(angles, values, team_loc_color, alpha=0.1)

    # Add legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.8])

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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/shootsComparison_" + str(index_local) + "_" + str(index_visitor) + ".png", dpi=300, bbox_inches='tight')
    plt.close()

def stats_position(teams, oer, orb, perd, drb, der, assis, local, against):
    oer_sorted = [x for _, x in sorted(zip(oer, teams))][::-1]
    orb_sorted = [x for _, x in sorted(zip(orb, teams))][::-1]
    perd_sorted = [x for _, x in sorted(zip(perd, teams))]
    drb_sorted = [x for _, x in sorted(zip(drb, teams))][::-1]
    der_sorted = [x for _, x in sorted(zip(der, teams))]
    assis_sorted = [x for _, x in sorted(zip(assis, teams))][::-1]

    oer_position = []
    orb_position = []
    perd_position = []
    drb_position = []
    der_position = []
    assis_position = []

    n_teams = len(teams)

    for team in teams:
        oer_position.append(n_teams - oer_sorted.index(team))
        orb_position.append(n_teams - orb_sorted.index(team))
        perd_position.append(n_teams - perd_sorted.index(team))
        drb_position.append(n_teams - drb_sorted.index(team))
        der_position.append(n_teams - der_sorted.index(team))
        assis_position.append(n_teams - assis_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'No-Perdudes': perd_position,
        'Atac': oer_position,
        'Reb.Ofensiu': orb_position,
        'Assistències': assis_position,
        'Reb.Defensiu': drb_position,
        'Defensa': der_position
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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/stats.png")
    plt.close()


def stats3_position(teams, points, reb_of_tot, perd, reb_def_tot, points_against, assis, local, against):
    oer_sorted = [x for _, x in sorted(zip(points, teams))][::-1]
    orb_sorted = [x for _, x in sorted(zip(reb_of_tot, teams))][::-1]
    perd_sorted = [x for _, x in sorted(zip(perd, teams))]
    drb_sorted = [x for _, x in sorted(zip(reb_def_tot, teams))][::-1]
    der_sorted = [x for _, x in sorted(zip(points_against, teams))]
    assis_sorted = [x for _, x in sorted(zip(assis, teams))][::-1]

    oer_position = []
    orb_position = []
    perd_position = []
    drb_position = []
    der_position = []
    assis_position = []

    n_teams = len(teams)

    for team in teams:
        oer_position.append(n_teams - oer_sorted.index(team))
        orb_position.append(n_teams - orb_sorted.index(team))
        perd_position.append(n_teams - perd_sorted.index(team))
        drb_position.append(n_teams - drb_sorted.index(team))
        der_position.append(n_teams - der_sorted.index(team))
        assis_position.append(n_teams - assis_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'No-Perdudes': perd_position,
        'Atac': oer_position,
        'Reb.Ofensiu': orb_position,
        'Assistències': assis_position,
        'Reb.Defensiu': drb_position,
        'Defensa': der_position
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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/stats3.png")
    plt.close()


def stats2_position(teams, oer, orb, drb, der, local, against):
    oer_sorted = [x for _, x in sorted(zip(oer, teams))][::-1]
    orb_sorted = [x for _, x in sorted(zip(orb, teams))][::-1]
    drb_sorted = [x for _, x in sorted(zip(drb, teams))][::-1]
    der_sorted = [x for _, x in sorted(zip(der, teams))][::-1]

    oer_position = []
    orb_position = []
    drb_position = []
    der_position = []

    n_teams = len(teams)

    for team in teams:
        oer_position.append(n_teams - oer_sorted.index(team))
        orb_position.append(n_teams - orb_sorted.index(team))
        drb_position.append(n_teams - drb_sorted.index(team))
        der_position.append(n_teams - der_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        'Atac': oer_position,
        'Reb.Ofensiu': orb_position,
        'Defensa': der_position,
        'Reb.Defensiu': drb_position
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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/stats2.png")
    plt.close()


def fourfactors_position(teams, efg, orb, perd, fft, local, against):
    efg_sorted = [x for _, x in sorted(zip(efg, teams))][::-1]
    orb_sorted = [x for _, x in sorted(zip(orb, teams))][::-1]
    perd_sorted = [x for _, x in sorted(zip(perd, teams))][::-1]
    fft_sorted = [x for _, x in sorted(zip(fft, teams))][::-1]

    efg_position = []
    orb_position = []
    perd_position = []
    fft_position = []

    n_teams = len(teams)

    for team in teams:
        efg_position.append(n_teams - efg_sorted.index(team))
        orb_position.append(n_teams - orb_sorted.index(team))
        perd_position.append(n_teams - perd_sorted.index(team))
        fft_position.append(n_teams - fft_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        '%eFG': efg_position,
        'Reb.Ofensiu': orb_position,
        'Perdudes': perd_position,
        'Freq TL': fft_position,
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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/fourfactors.png")
    plt.close()


def eightfactors_position(teams, efg, orb, perd, fft, efg_againts, orb_againts, perd_againts, fft_againts, local,
                          against):
    efg_sorted = [x for _, x in sorted(zip(efg, teams))][::-1]
    orb_sorted = [x for _, x in sorted(zip(orb, teams))][::-1]
    perd_sorted = [x for _, x in sorted(zip(perd, teams))][::-1]
    fft_sorted = [x for _, x in sorted(zip(fft, teams))][::-1]

    efg_position = []
    orb_position = []
    perd_position = []
    fft_position = []

    efg_againts_sorted = [x for _, x in sorted(zip(efg_againts, teams))][::-1]
    orb_againts_sorted = [x for _, x in sorted(zip(orb_againts, teams))][::-1]
    perd_againts_sorted = [x for _, x in sorted(zip(perd_againts, teams))][::-1]
    fft_againts_sorted = [x for _, x in sorted(zip(fft_againts, teams))][::-1]

    efg_againts_position = []
    orb_againts_position = []
    perd_againts_position = []
    fft_againts_position = []

    n_teams = len(teams)

    for team in teams:
        efg_position.append(n_teams - efg_sorted.index(team))
        orb_position.append(n_teams - orb_sorted.index(team))
        perd_position.append(n_teams - perd_sorted.index(team))
        fft_position.append(n_teams - fft_sorted.index(team))

        efg_againts_position.append(n_teams - efg_againts_sorted.index(team))
        orb_againts_position.append(n_teams - orb_againts_sorted.index(team))
        perd_againts_position.append(n_teams - perd_againts_sorted.index(team))
        fft_againts_position.append(n_teams - fft_againts_sorted.index(team))

    df = pd.DataFrame({
        'Team': teams,
        '%eFG': efg_position,
        'Reb.Ofensiu': orb_position,
        'Perdudes': perd_position,
        'Freq TL': fft_position,
        '%eFG Rival': efg_againts_position,
        'Reb.Ofensiu Rival': orb_againts_position,
        'Perdudes Rival': perd_againts_position,
        'Freq TL Rival': fft_againts_position,
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
    plt.savefig("C:/Users/ferra/PycharmProjects/radarChart/eightfactors.png")
    plt.close()
