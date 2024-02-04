import seaborn as sns
import matplotlib.pyplot as plt
import json

def plot_data(df, plot, x_var, y_var, hue_var, chart_kargs):
    plot_args = {}
    if x_var:
        plot_args["x"] = x_var
    if y_var:
        plot_args["y"] = y_var
    if hue_var:
        plot_args["hue"] = hue_var
    
    chart_kargs_dict = {}
    plt_kargs = {}
    sns_kargs = {}
    if chart_kargs:
        chart_kargs_dict = json.loads(chart_kargs)
        if "plt" in chart_kargs_dict:
            plt_kargs = chart_kargs_dict["plt"]
        if "sns" in chart_kargs_dict:
            sns_kargs = chart_kargs_dict["sns"]
            plot_args.update(sns_kargs)

    fig, ax = plt.subplots(figsize=(10, 2))
    if plot == "Bar Plot":
        sns.barplot(data=df, ax=ax, **plot_args)
    elif plot == "Line Plot":
        sns.lineplot(data=df, ax=ax, **plot_args)
    elif plot == "Scatter Plot":
        sns.scatterplot(data=df, ax=ax, **plot_args)
    ax.set(**plt_kargs)
    # ax.grid(plt_kargs.get("grid", False))
    
    return fig
