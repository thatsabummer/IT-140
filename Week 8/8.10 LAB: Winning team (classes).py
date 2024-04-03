# Author: Caleb Smith
# Date: 10.20.2023

# Lab 8.10

# Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
# team_wins / (team_wins + team_losses)

# Winning team (classes)

# Define the Team Class

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

# Get a win percentage
    
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


# Call the functions

if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

  # print

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
