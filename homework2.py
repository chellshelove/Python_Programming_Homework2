# Importing necessary modules
import random

# Function to simulate rolling three dice and check if all dice are the same
def roll_three_dice(n_trials):
    same_count = 0
    for _ in range(n_trials):
        dice = [random.randint(1, 6) for _ in range(3)]
        if dice[0] == dice[1] == dice[2]:
            same_count += 1
    return same_count / n_trials

# Number of trials for approximation
n_trials = 1000000
probability = roll_three_dice(n_trials)

# Writing the result to a file
output_file_path = '/mnt/data/dice_probability_output.txt'
with open(output_file_path, 'w') as f:
    f.write(f'Approximated probability: {probability}\n')

# Returning the file path for download
output_file_path