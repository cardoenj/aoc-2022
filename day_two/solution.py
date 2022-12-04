

def determine_outcome(opponent, state):
    opponent = ord(opponent) - 64
    state = ord(state) - 87
    
    if state == 1:
        # Lose
        if opponent == 1:
            return 3
        if opponent == 2:
            return 1
        if opponent == 3:
            return 2
    if state == 2:
        # Draw
        return 3 + opponent
    if state == 3:
        # Win
        if opponent == 1:
            return 6 + 2
        if opponent == 2:
            return 6 + 3
        if opponent == 3:
            return 6 + 1

def determine_score(opponent, user):
    # Individual scores
    # Rock = 1 (A, X)
    # Paper = 2 (B, Y)
    # Scissors = 3 (C, Z)
    # Round win = 6
    # Round lose = 0
    # Round draw = 3
    opponent = ord(opponent) - 64 # ascii A = 65
    user = ord(user) - 87 # ascii X = 88
    print(opponent)
    print(user)
    if opponent == user:
        return 3 + user
    # 1 defeated by 2, wins for 3
    # 2 defeated by 3, wins for 1

    if opponent == 1:
        if user == 2:
            return 6 + user
        return user
    if opponent == 2:
        if user == 3:
            return 6 + user
        return user
    if opponent == 3:
        if user == 1:
            return 6 + user
        return user

strategies = []
with open("input.dat") as fp: 
    strategies = fp.readlines()

total_score = 0
total_score_strategy = 0
for strategy in strategies:
    picks = strategy.split()
    print(picks)
    total_score += determine_score(picks[0], picks[1])
    total_score_strategy += determine_outcome(picks[0], picks[1])
print(total_score)
print(total_score_strategy)
