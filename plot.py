import matplotlib.pyplot as plt

class PlotGenerator:
    def generate_single_box_and_whiskers(self, results, plot_name="results"):
        ys = [r['fitness'] for r in results]

        plt.title("Solution Energy")
        plt.ylabel("Solution Energy")
        plt.boxplot(ys, labels=['Scores'])
        plt.savefig(f"{plot_name}.png")

    def generate_multiple_box_and_whiskers(self, all_results, x_values, plot_title, plot_name="results"):
        data = []
        for results in all_results:
            ys = [r['fitness'] for r in results]
            data.append(ys)

        plt.title(plot_title)
        plt.ylabel("Solution Energy")
        plt.boxplot(data, labels=[str(x) for x in x_values])
        plt.legend()
        plt.grid(linestyle=':', axis='y')

        plt.savefig(f"{plot_name}.png")

