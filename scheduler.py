import random
#these are all FBS clubs, FCS not included...yet ;)
cfb = {'ACC': ['Boston College', 'Clemson', 'Duke', 'Florida State', 'Georgia Tech', 'Louisville', 'Miami', 'NC State', 'North Carolina', 'Pittsburgh', 'Syracuse', 'Virginia', 'Virginia Tech', 'Wake Forest'],
       'Big Ten': ['Illinois', 'Indiana', 'Iowa', 'Maryland', 'Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin'],
       'Big 12': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
       'SEC': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Missouri', 'Mississippi State', 'Ole Miss', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
       'Pac 12': ['Arizona', 'Arizona State', 'Cal', 'Colorado', 'Oregon', 'Oregon State', 'Stanford', 'UCLA', 'USC', 'Utah', 'Washington', 'Washington State'],
       'Mountain West': ['Air Force', 'Boise State', 'Colorado State', 'Fresno State', 'Hawaii', 'Nevada', 'New Mexico', 'San Diego State', 'San Jose State', 'UNLV', 'Utah State', 'Wyoming'],
       'MAC': ['Northern Illinois', 'Western Michigan', 'Central Michigan', 'Eastern Michigan', 'Ball State', 'Toledo', 'Kent State', 'Ohio', 'Akron', 'Buffalo', 'Bowling Green', 'Miami OH'],
       'American': ['Cincinnati', 'East Carolina', 'Houston', 'Memphis', 'Navy', 'SMU', 'Temple', 'Tulane', 'Tulsa', 'UCF', 'USF',],
       'C-USA': ['Charlotte', 'FAU', 'FIU', 'Louisiana Tech', 'Marshall', 'Mid Tenn State', 'North Texas', 'Old Dominion', 'Rice', 'Southern Miss', 'UAB', 'UTEP', 'UTSA', 'Western Kentucky'],
       'Sun Belt': ['Appalachain State', 'Arkansas State', 'Coastal Carolina', 'Georgia Southern', 'Georgia State', 'South Alabama', 'Texas State', 'Troy', 'UL Lafayette', 'UL Monroe'],
       'Independents': ['Army', 'BYU', 'New Mexico State', 'Notre Dame', 'UConn', 'UMass', 'Liberty']
       }

cfb_team = str(input('Enter a college football team: '))
list_of_teams = []
for k, v in cfb.items():
    for index in v:
        list_of_teams.append(index)
while cfb_team not in list_of_teams:
    print('Invalid input, please try again.')
    cfb_team = str(input('Enter a college football team: '))

def get_dates():
    dates = ['Sep 3', 'Sep 10', 'Sep 17', 'Sep 24', 'Oct 1', 'Oct 8', 'Oct 15', 'Oct 22', 'Oct 29', 'Nov 5', 'Nov 12', 'Nov 19', 'Nov 26', 'Dec 3']
    return dates

def get_type():
    game_type = random.choices(['at', 'vs'], weights=None, k=12)
    bye = ['BYE', 'BYE']
    game_types = game_type + bye 
    random.shuffle(game_types)
    return game_types

def get_opponents(team):
    teams = []
    non_conf_opps = [t for t in list(cfb.values()) if team not in t]
    #find the key-value pair of team and remove it from random selection of team1, team2, team3
    choice_1 = random.choice(non_conf_opps)
    team1 = random.choice(choice_1)
    #remove team1 to not get duplicate
    choice_1.remove(team1)
    choice_2 = random.choice(non_conf_opps)
    team2 = random.choice(choice_2)
    #remove team2 to not get duplicate
    choice_2.remove(team2)
    choice_3 = random.choice(non_conf_opps)
    team3 = random.choice(choice_3)
    all_teams = list(cfb.values())
    in_conf_teams = [index for index in all_teams if team in index]
    for items in in_conf_teams:
        items.remove(team)
        for item in items:
            teams.append(item)
    new_teams = random.sample(teams, 9)
    new_teams.append(team1)
    new_teams.append(team2)
    new_teams.append(team3)
    #for BYE weeks, just put '--':
    new_teams.append('--')
    new_teams.append('--')
    random.shuffle(new_teams)
    return new_teams

def sort_byes(type, opponent):
    #using this function to sort BYEs and opponents so that no opponents show up next to BYE
    #compare index of each list and have the 'BYE' and '--' indeces equal
    type_i = [bye for (bye, i) in enumerate(type) if i == 'BYE']
    for i in range(len(opponent)):
        if '--' in opponent:
            opponent.remove('--')
    opponent.insert(type_i[0], '--')
    opponent.insert(type_i[1], '--')
    return opponent

def display_schedule(date, type, opponent):
    sort_byes(type, opponent)
    print("Let's go, {}".format(cfb_team))
    print('these are your gamedays:')
    for d, t, o in zip(date, type, opponent):
        print('{} {} {}'.format(d, t, o), end="\n")

display_schedule(get_dates(), get_type(), get_opponents(cfb_team))
