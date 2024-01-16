import random

class LABS:
    def __init__(self, problem=None, solution_length=10):
        if problem is not None and isinstance(problem, LABS):
            self.solution_length = problem.solution_length
            self.solution_array = problem.solution_array.copy()
            self.autocorrelation_products = problem.autocorrelation_products.copy()
            self.autocorrelations = problem.autocorrelations.copy()
        else:
            self.solution_length = solution_length
            self.solution_array = []
            self.autocorrelation_products = []
            self.autocorrelations = []

    def calculate_fitness(self):
        self.calculate_aperiodic_autocorrelation()
        return sum(c * c for c in self.autocorrelations)

    def generate_random_solution(self):
        self.solution_array = [random.choice([-1, 1]) for _ in range(self.solution_length)]

    def calculate_aperiodic_autocorrelation(self):
        self.autocorrelation_products = []
        self.autocorrelations = []
        for k in range(1, self.solution_length):
            products = [self.solution_array[i] * self.solution_array[i + k] for i in range(self.solution_length - k)]
            self.autocorrelation_products.append(products)
            self.autocorrelations.append(sum(products))

