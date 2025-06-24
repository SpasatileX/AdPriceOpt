import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

def plot_cost_vs_views(df: pd.DataFrame, path: str):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='total_views', y='unit_cost', hue='recommendation')
    plt.title("Ціна показу залежно від кількості переглядів")
    plt.xlabel("Кількість показів")
    plt.ylabel("Вартість показу")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_cost_distribution(df: pd.DataFrame, path: str):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='unit_cost', hue='recommendation', kde=True)
    plt.title("Розподіл вартості показів реклами")
    plt.xlabel("Вартість показу")
    plt.ylabel("Кількість")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
