import random

class TabuSearch:
    def __init__(self, max_iterations=200, min_tabu=None, extra_tabu=None):
        self.max_iterations = max_iterations
        if min_tabu:
            self.min_tabu = min_tabu # max_iterations/10
        else:
            self.min_tabu = self.max_iterations // 10

        if extra_tabu:
            self.extra_tabu = extra_tabu # max_iterations/50
        else:
            self.extra_tabu = self.max_iterations // 50

    def solve(self, problem):
        rand = random.Random()
        tabu_list = [0] * len(problem.solution_array)

        solution = problem.solution_array[:]
        fitness = problem.calculate_fitness()

        for k in range(1, self.max_iterations + 1):
            best_move = self.find_best_move(problem, k, tabu_list, fitness)
            problem.solution_array = best_move['best_solution_in_iteration']
            problem.calculate_fitness()
            tabu_list[best_move['best_index_in_iteration'] - 1] = k + self.min_tabu + rand.randint(0, self.extra_tabu)

            if best_move['best_fitness_in_iteration'] < fitness:
                solution = best_move['best_solution_in_iteration']
                fitness = best_move['best_fitness_in_iteration']

        problem.solution_array = solution

        return {'solution': solution, 'fitness': fitness}

    def find_best_move(self, problem, iteration, tabu_list, fitness):
        best_fitness_in_iteration = float('inf')
        best_solution_in_iteration = problem.solution_array[:]
        best_index_in_iteration = 1

        for i in range(1, len(best_solution_in_iteration) + 1):
            possible_solution = self.flip(problem, i)
            possible_fitness = self.value_flip(problem, i)

            if iteration < tabu_list[i - 1] and not possible_fitness < fitness:
                continue

            if possible_fitness < best_fitness_in_iteration:
                best_fitness_in_iteration = possible_fitness
                best_solution_in_iteration = possible_solution
                best_index_in_iteration = i

        return {
            'best_fitness_in_iteration': best_fitness_in_iteration,
            'best_solution_in_iteration': best_solution_in_iteration,
            'best_index_in_iteration': best_index_in_iteration
        }

    def flip(self, problem, index):
        flipped_solution = problem.solution_array[:]
        flipped_solution[index - 1] *= -1
        return flipped_solution

    def value_flip(self, problem, value_index):
        fitness = 0.0
        for p in range(len(problem.solution_array) - 1):
            value = problem.autocorrelations[p]
            if p < len(problem.solution_array) - value_index:
                value -= 2 * problem.autocorrelation_products[p][value_index - 1]

            if p < value_index - 1:
                value -= 2 * problem.autocorrelation_products[p][value_index - 1 - p - 1]

            fitness += value ** 2
        return fitness
