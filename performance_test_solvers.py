import copy
import time
from generate_sudoku import *
from solver_backtracking import SolverBacktracking
from solver_forward_checking import SolverForwardChecking


n_trials = 7
run_times = []

selected_difficulty = 2
puzzle = generate_puzzle(selected_difficulty)


backtrackSolver = SolverBacktracking()
forwardSolver = SolverForwardChecking()



def test(solver, solver_name):
    for i in range(n_trials):
        local_puzzle = copy.deepcopy(puzzle) # generating new puzzle for each run has the same time complexity
        start_time = time.time()
        if not solver.solve_game( local_puzzle ):
            print("\nNo solution")
        else:
            elapsed = time.time() - start_time
            
            print("\n",solver_name," took:", elapsed)
            run_times.append( elapsed )

    run_times
    print("Avg run time with (",n_trials," trial/s) :", sum(run_times)/n_trials,"\n\n",9*'-')


test(backtrackSolver, "Backstracking")
test(forwardSolver, "Forward Checking")