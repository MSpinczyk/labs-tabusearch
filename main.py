from plot import PlotGenerator
from problem import LABS
from tabu_search import TabuSearch
from runner import SearchRunner


def main():
    problem = LABS(solution_length=100) #length of sequence
    problem.generate_random_solution()
    search = TabuSearch(200, 20, 4)
    runner = SearchRunner()
    plot_generator = PlotGenerator()

    # Uncomment and implement these lines according to your actual algorithm and plotting logic
    # results = runner.run(100, problem, search, 200)
    # plot_generator.generate_single_box_and_whiskers(results, "results")

    algorithm_runs = 50
    time_limit_in_seconds = 10
    search_iterations = [100]
    multiple_results_iterations = runner.run_with_multiple_iterations(
        algorithm_runs, problem, search, search_iterations, 20, 4, time_limit_in_seconds)
    print(multiple_results_iterations)
    plot_generator.generate_multiple_box_and_whiskers(multiple_results_iterations, search_iterations, 
                                                      "Solution energy for different values of search iterations", 
                                                      "multiple results iterations")

if __name__ == "__main__":
    main()
