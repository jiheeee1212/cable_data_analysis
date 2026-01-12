
import pandas as pd
import matplotlib.pyplot as plt

def plot_bar(df,col1,col2,figure_path):
    crosstab = pd.crosstab(df[col1], df[col2], normalize='index')
    ax = crosstab.plot(kind='bar', figsize=(6,4))
    plt.title(f"{col1} vs {col2}")
    plt.ylabel("Proportion")
    plt.xticks(rotation=0)
    plt.ylim(0,0.15)
    plt.tight_layout()
    plt.savefig(figure_path, dpi=150)
    plt.close()

def boxplot_by_group(df, num_col, cat_col, figure_path):
    ax = df.boxplot(column=num_col, by=cat_col, grid=False, figsize=(6,4))
    plt.title(f"{num_col} by {cat_col}")
    plt.suptitle("")
    plt.tight_layout()
    plt.savefig(figure_path, dpi=150)
    plt.close()

def plot_hist(df, col, figure_path, bins=30):
    plt.figure(figsize=(6,4))
    df[col].hist(bins=bins)
    plt.title(col)
    plt.tight_layout()
    plt.savefig(figure_path, dpi=150)
    plt.close()
