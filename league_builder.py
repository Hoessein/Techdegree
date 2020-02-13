import csv

# Several empty lists which I can use to append items too
dragons = []
sharks= []
raptors = []
experienced_players = []
inexperienced_players = []


# In this method I made a list from the csv file
def csv_to_list():
    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        player = list(csv_reader)
    return player


# In this method I loop through the player list and check if they are experienced
# The player gets appended to the experienced or unexperienced list accordingly
def filter_experience():
    for player in csv_to_list():
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        if player['Soccer Experience'] == 'NO':
            inexperienced_players.append(player)


# In this method the experienced and inexperienced players are divided into the three team lists
def sort_players():

    for experienced_player, inexperienced_player in zip(experienced_players[:3], inexperienced_players[:3]):
        dragons.append(experienced_player)
        dragons.append(inexperienced_player)

    for experienced_player, inexperienced_player in zip(experienced_players[3:6], inexperienced_players[3:6]):
        sharks.append(experienced_player)
        sharks.append(inexperienced_player)

    for experienced_player, inexperienced_player in zip(experienced_players[6:9], inexperienced_players[6:9]):
        raptors.append(experienced_player)
        raptors.append(inexperienced_player)


# In this method a readable format of the teams are returned
def teams_roster(team, title):

    team_group = title + '\n'

    for player in team:
        team_keys = (player['Name'], player['Soccer Experience'], player['Guardian Name(s)'])
        team_group += ", ".join(team_keys)
        team_group += '\n'
    team_group += '\n'

    return team_group


# This is a method which writes the rosters to a new text file which is called team.txt.
def write_to_text_file():
    file = open("teams.txt", "w")
    file.write(teams_roster(raptors, 'Raptors'))
    file.write(teams_roster(dragons, 'Dragons'))
    file.write(teams_roster(sharks, 'Sharks'))


if __name__ == '__main__':
    filter_experience()
    sort_players()
    write_to_text_file()
