import csv

dragons = []
sharks= []
raptors = []
experienced_players = []
unexperienced_players = []

def dicty():
    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter= ',')
        player = list(csv_reader)
    return player

def experience():
    for d in dicty():
        if d['Soccer Experience'] == 'YES':
            experienced_players.append(d)
        else:
            unexperienced_players.append(d)

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


def dragons_roster():
    names ='dragons' \
            '\n'
    for rosters in dragons:
        tikooo = (rosters['Name'], rosters['Soccer Experience'], rosters['Guardian Name(s)'])
        names += ", ".join(tikooo)
        names += '\n'
    return names

def sharks_roster():
    names = '\n' \
            'sharks' \
            '\n'
    for rosters in sharks:
        tikooo = (rosters['Name'], rosters['Soccer Experience'], rosters['Guardian Name(s)'])
        names += ", ".join(tikooo)
        names += '\n'
    return names

def raptors_roster():
    names = '\n' \
            'raptors' \
            '\n'
    for rosters in raptors:
        tikooo = (rosters['Name'], rosters['Soccer Experience'], rosters['Guardian Name(s)'])
        names += ", ".join(tikooo)
        names += '\n'
    return names

def write_to_text():
    file = open("teams.txt", "w")
    file.write(dragons_roster())
    file.write(sharks_roster())
    file.write(raptors_roster())

if __name__ == '__main__':

    dicty()
    experience()
    sort_experienced_players()
    sort_unexperienced_players()
    write_to_text()