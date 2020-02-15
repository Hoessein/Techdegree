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
        players = list(csv_reader)
    return players


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


def write_letter(team_list, team_name):

    for player in team_list:
        filename = player['Name'].replace(" ", "_").lower() + ".txt"
        salutation = f"Dear {player['Guardian Name(s)']}, \n\n"
        letter_body = f"We are proud to inform you that {player['Name']}" \
            f" has been selected to play for {team_name} in the soccer league."

        file = open(filename, "w")
        file.write(salutation)
        file.write(letter_body)


# This is a method which writes the rosters to a new text file which is called team.txt.
def write_to_text_file():
    file = open("teams.txt", "w")

    file.write(teams_roster(raptors, 'Raptors'))
    file.write(teams_roster(dragons, 'Dragons'))
    file.write(teams_roster(sharks, 'Sharks'))

    write_letter(raptors, 'Raptors')
    write_letter(dragons, 'Dragons')
    write_letter(sharks, 'Sharks')


if __name__ == '__main__':
    filter_experience()
    sort_players()
    write_to_text_file()

