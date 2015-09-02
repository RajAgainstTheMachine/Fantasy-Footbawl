#!/usr/bin/python

import re

inputfile = '2015 Rankings and Projected Points'
ranked_players = {}
fantasy_team = {}
fantasy_team_positions = {}
fantasy_team_pfp = {}
positions = {'QB':1, 'WR':5, 'RB':4, 'TE':2, 'DST':0, 'K':0}
num_teams = 12
max_rounds = 12
test_round = 9
test_team = 5
test_position = 'QB'

for team in range(1, num_teams + 1):
	for position in positions:
		fantasy_team_positions[team, position] = 0
		fantasy_team_pfp[team] = 0


def asint(s):
    try: return int(s), ''
    except ValueError: return sys.maxint, s

firstline = True
with open(inputfile, 'r') as f:
	for line in f:
		if firstline:
			firstline = False
			continue
		#print line
		listofplayers = []
		listofplayers = line.split('\t')
		#print listofplayers
		ranked_players[ int(listofplayers[0]) ] = [ listofplayers[1], listofplayers[2], int(listofplayers[9]), float(listofplayers[10].splitlines()[0]) ]


# for draft_pick in sorted(ranked_players, key=asint):
# 	print draft_pick, "\t", ranked_players[draft_pick]


for draft_round in range(1, max_rounds + 1):
	#print "Draft round is", draft_round
	if draft_round % 2 == 0:
		for team in reversed(range(1, num_teams + 1)):
			#print "Team is", team
			for draft_pick in sorted(ranked_players, key=asint):
				#print "Draft pick is", draft_pick
				position_text = []
				position_text = re.match(r"([A-Z]+)([0-9]+)", ranked_players[draft_pick][1], re.I)
				if position_text:
					items = position_text.groups()
				#print items[0]
				if fantasy_team_positions[team, items[0]] < positions[items[0]]:
					if items[0] == test_position and draft_round < test_round and team == test_team:
						continue
					else:
						fantasy_team[team, draft_round] = ranked_players[draft_pick]
						fantasy_team_positions[team, items[0]] = fantasy_team_positions[team, items[0]] + 1
						del ranked_players[draft_pick]
						break
				else:
					continue

	else:
		for team in range(1, num_teams + 1):	
			#print "Team is", team
			for draft_pick in sorted(ranked_players, key=asint):
				#print "Draft pick is", draft_pick
				position_text = []
				position_text = re.match(r"([A-Z]+)([0-9]+)", ranked_players[draft_pick][1], re.I)
				if position_text:
					items = position_text.groups()
				#print items[0]
				if fantasy_team_positions[team, items[0]] < positions[items[0]]:
					if items[0] == test_position and draft_round < test_round and team == test_team:
						continue
					else:
						fantasy_team[team, draft_round] = ranked_players[draft_pick]
						fantasy_team_positions[team, items[0]] = fantasy_team_positions[team, items[0]] + 1
						del ranked_players[draft_pick]
						break
				else:
					continue


for key1, key2 in sorted(fantasy_team):
	print "Team", key1, "Pick", key2, fantasy_team[key1, key2]
	fantasy_team_pfp[key1] = fantasy_team_pfp[key1] + fantasy_team[key1, key2][3]

for team in sorted(fantasy_team_pfp):
	print "Team", team, "\t", fantasy_team_pfp[team]
