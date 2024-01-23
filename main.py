from plot import PlotGenerator
from problem import LABS
from tabu_search import TabuSearch
from runner import SearchRunner


def main():
    solver = TabuSearch(200, 20, 4)
    runner = SearchRunner()


    sol_lengths = [100, 150, 200]
    extra_tabu_list = [1, 2, 3, 4, 6, 8]
    runner.run_extra_tabu_experiment(15, sol_lengths, solver, 200, 20, extra_tabu_list, 1, 'data.pkl')

if __name__ == "__main__":
    main()
