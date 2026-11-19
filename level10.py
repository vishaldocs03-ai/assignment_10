# Level 10 Assignment
# IS 303
# Lets the user pick a college football season and sorts the teams
# from that season into groups based on how many games they won

import pandas as pd

# read in the data
df = pd.read_csv("cfb.csv")

season = input("Enter a season to analyze: ")
season = season.strip()

# make a list of all the seasons in the file so I can check if the one they typed is in there
season_list = []
for s in df["Season"]:
    if str(s) not in season_list:
        season_list.append(str(s))

if season not in season_list:
    print("\nSorry, the season " + season + " was not found in the data.")
    print("Seasons available:")
    for s in season_list:
        print(" " + s)
else:
    # dictionary to hold the teams for each category
    results = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    # go through every row and only use the ones for the season they picked
    for index, row in df.iterrows():
        if str(row["Season"]) == season:
            team = row["Team"]
            wins = int(row["Win"])

            # the team names have the conference after them like "Alabama (SEC)"
            # so cut off the last set of parentheses to just get the name
            # (using the last one because of teams like "Miami (FL) (ACC)")
            spot = team.rfind("(")
            if spot != -1:
                team = team[0:spot]
            team = team.strip()

            if wins >= 10:
                results["10 or more wins"].append(team)
            elif wins >= 8:
                results["8-9 wins"].append(team)
            elif wins >= 6:
                results["6-7 wins"].append(team)
            else:
                results["Fewer than 6 wins"].append(team)

    # print everything out
    print("\nCollege Football Results for " + season)

    for category in results:
        print("\n" + category + ":")
        if len(results[category]) == 0:
            print(" No teams")
        else:
            for team in results[category]:
                print(" " + team)
