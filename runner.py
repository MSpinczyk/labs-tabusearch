import time
from problem import LABS

class SearchRunner:
    def run(self, iterations, problem, solver, search_iterations, min_tabu, extra_tabu, time_limit_in_seconds):
        results = []
        solver.max_iterations = search_iterations
        solver.min_tabu = min_tabu
        solver.extra_tabu = extra_tabu
        best_result = None
    
        for i in range(iterations):
            start_time = time.time()
            print(f"Algorithm run number {i}")
            number_of_tries = 0
    
            while time.time() - start_time < time_limit_in_seconds:
                number_of_tries += 1
                result = solver.solve(LABS(problem))
                
                # print(f'Current number of tries: {number_of_tries}\nCurrent result: {result}')
                if best_result is None or result['fitness'] > best_result['fitness']:
                    best_result = result
    
            print(f"Number of tries {number_of_tries} for max iterations {search_iterations}")
            results.append(best_result)
    
        return results


    def run_with_multiple_iterations(self, iterations, problem, solver, search_iterations_list, min_tabu, extra_tabu, time_limit_in_seconds):
        output = []
        for search_iterations in search_iterations_list:
            results = self.run(iterations, problem, solver, search_iterations, min_tabu, extra_tabu, time_limit_in_seconds)
            output.append(results)
        return output


    def run_with_multiple_min_tabu(self, iterations, problem, solver, search_iteration, min_tabu_list, extra_tabu, time_limit_in_seconds):
        output = []
        for min_tabu in min_tabu_list:
            results = self.run(iterations, LABS(problem), solver, search_iteration, min_tabu, extra_tabu, time_limit_in_seconds)
            output.append(results)
        return output

    def run_with_multiple_extra_tabu(self, iterations, problem, solver, search_iteration, min_tabu, extra_tabu_list, time_limit_in_seconds):
        output = []
        for extra_tabu in extra_tabu_list:
            results = self.run(iterations, LABS(problem), solver, search_iteration, min_tabu, extra_tabu, time_limit_in_seconds)
            output.append(results)
        return output
