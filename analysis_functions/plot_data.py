from matplotlib import pyplot as plt

def plot_data(df, col_x, col_y, filename="default.png"):

    df_plot = df[[col_x, col_y]].groupby([col_x]).agg(["sum", "count"]).reset_index()
    print(df_plot.columns)
    
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.bar(df_plot[col_x] - 0.3, df_plot[("Survived", "sum")], width=0.25)
    ax.bar(df_plot[col_x]+0.05, df_plot[("Survived", "count")], width=0.25)
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)

    plt.savefig(filename)