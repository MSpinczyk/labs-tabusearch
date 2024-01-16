from plot import PlotGenerator
from problem import LABS
from tabu_search import TabuSearch
from runner import SearchRunner


def main():
    problem = LABS(solution_length=100) #length of sequence
    solver = TabuSearch(200, 20, 4)
    runner = SearchRunner()
    plot_generator = PlotGenerator()

    algorithm_runs = 2
    time_limit_in_seconds = 20
    search_iterations = [100]
    search_iteration = 100
    problems = [LABS(solution_length=l) for l in [27]]
    # multiple_results_iterations = runner.run_with_multiple_iterations(
    #     algorithm_runs, problem, solver, search_iterations, 20, 4, time_limit_in_seconds)
    multiple_problems_results = runner.run_with_multiple_problems(
        algorithm_runs, problems, solver, search_iteration, 20, 4, time_limit_in_seconds)

    print(r['fitness'] for r in multiple_problems_results)
    plot_generator.generate_multiple_box_and_whiskers(multiple_problems_results, [p.solution_length for p in problems], 
                                                      "Solution energy for different values of search iterations", 
                                                      "multiple results iterations")

if __name__ == "__main__":
    main()
