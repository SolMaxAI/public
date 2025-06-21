
import matplotlib.pyplot as plt

def plot_scores(score_list):
    plt.figure(figsize=(10, 6))
    plt.plot(score_list, color='blue', marker='o', linestyle='--')
    plt.title("Token Score Trend")
    plt.xlabel("Token #")
    plt.ylabel("Score")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/images/score_graph.png")
    plt.close()
