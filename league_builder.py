import csv

#Several empty lists which I can use to append items too
dragons = []
sharks= []
raptors = []
experienced_players = []
unexperienced_players = []

#In this method I made a list from the csv file
def csv_to_list():
    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter= ',')
        player = list(csv_reader)
    return player

#In this method I loop through the player list and check if they are experienced
#The player gets appended to the experienced or unexperienced list accordingly
def filter_experience():
    for player in csv_to_list():
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        else:
            unexperienced_players.append(player)

#In this method I use a while loop to loop through the experienced_players list until it's falsy
#Inside the loop I append the experienced players to the three empty lists: dragons, raptors and sharks
#After a player gets appended i delete that player from the experienced_players list using the 0 index position
#I use a try  block to break out of the loop when there are no experienced players left
def sort_experienced_players():
    while True:
        try:
            dragons.append(experienced_players[0])
            del experienced_players[0]

            sharks.append(experienced_players[0])
            del experienced_players[0]

            raptors.append(experienced_players[0])
            del experienced_players[0]
        except IndexError:
            break

#This time i append the players from the unexperienced list to the three empty lists: dragons, raptors and sharks
def sort_unexperienced_players():
    while True:
        try:
            dragons.append(unexperienced_players[0])
            del unexperienced_players[0]

            sharks.append(unexperienced_players[0])
            del unexperienced_players[0]

            raptors.append(unexperienced_players[0])
            del unexperienced_players[0]
        except IndexError:
            break

#In the following 3 methods I enter the dict key values to select which key values are relevant for this project
#I use the join method to comma separate the values
#I use some new lines formatting so it models the requirements
def dragons_roster():
    dragons_group ='dragons' \
            '\n'
    for dragon in dragons:
        dragon_keys = (dragon['Name'], dragon['Soccer Experience'], dragon['Guardian Name(s)'])
        dragons_group += ", ".join(dragon_keys)
        dragons_group += '\n'
    return dragons_group

def sharks_roster():
    sharks_group = '\n' \
            'sharks' \
            '\n'
    for shark in sharks:
        shark_keys = (shark['Name'], shark['Soccer Experience'], shark['Guardian Name(s)'])
        sharks_group += ", ".join(shark_keys)
        sharks_group += '\n'
    return sharks_group

def raptors_roster():
    raptors_group = '\n' \
            'raptors' \
            '\n'
    for raptor in raptors:
        raptor_keys = (raptor['Name'], raptor['Soccer Experience'], raptor['Guardian Name(s)'])
        raptors_group += ", ".join(raptor_keys)
        raptors_group += '\n'
    return raptors_group

#This is a method which writes the rosters to a new text file which is called team.txt.
def write_to_text_file():
    file = open("teams.txt", "w")
    file.write(dragons_roster())
    file.write(sharks_roster())
    file.write(raptors_roster())

if __name__ == '__main__':

    csv_to_list()
    filter_experience()
    sort_experienced_players()
    sort_unexperienced_players()
    write_to_text_file()