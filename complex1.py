import random
import math
from function_code import complex1

def stochastic_hill_climbing(bounds, max_iterations, step_size):
    # Generate an initial random candidate
    candidate = [random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1])]
    candidate_eval = complex1(candidate)
    
    for i in range(max_iterations):
        # Take a step in a random direction
        new_candidate = [
            candidate[0] + random.uniform(-step_size, step_size),
            candidate[1] + random.uniform(-step_size, step_size)
        ]
        
        # Ensure the new candidate is within bounds
        new_candidate[0] = max(bounds[0][0], min(bounds[0][1], new_candidate[0]))
        new_candidate[1] = max(bounds[1][0], min(bounds[1][1], new_candidate[1]))

        # Evaluate the new candidate
        new_candidate_eval = complex1(new_candidate)
        
        # Check if the new candidate is better
        if new_candidate_eval < candidate_eval:
            candidate, candidate_eval = new_candidate, new_candidate_eval
            # (Optinal) Print of the iterations
            #print(f"Iteration {i}, new best candidate: {candidate}, value: {candidate_eval}")
    
    return candidate, candidate_eval

if __name__ == "__main__":
    # Define the bounds of the search space
    bounds = [(-100, 100), (-100, 100)]
    # Define the maximum number of iterations
    max_iterations = 1000
    # Define the step size
    step_size = 1.0
    
    # Perform stochastic hill climbing
    best_candidate, best_value = stochastic_hill_climbing(bounds, max_iterations, step_size)
    print(f"Best candidate: {best_candidate}, Best value: {best_value}")
