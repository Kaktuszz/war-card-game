
import subprocess
import re

def run_game():
    # Run game and captre the output
    result = subprocess.run(['python', 'game.py'], capture_output=True, text=True)

    # Split the output into lines
    lines = result.stdout.strip().split('\n')
    # Check who won the game
    if "Player1 won!" in lines:
        return "Player1"
    elif "Player2 won!" in lines:
        return "Player2"
    else:
        return "Tie"
    # Count max rounds
     
     

# Run game 1000 times, count the wins
p1_wins = 0
p2_wins = 0
tie = 0
max_rounds = 0
max_war = 0

for i in range(100):
    winner = run_game()
    if winner == "Player1":
        p1_wins += 1
    elif winner == "Player2":
        p2_wins += 1
    else:
        tie += 1

    

# Print the results
print("Player1 won", p1_wins, "times")
print("Player2 won", p2_wins, "times")
print("Error: ", tie, "times")




