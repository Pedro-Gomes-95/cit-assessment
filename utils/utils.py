from matplotlib.pyplot import figure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

def plot_categorical_feature(
    data_frame,
    column,
    figsize=(5, 4),
    sort=True,
    normalize=True,
    plot_h_line=False,
    h_threshold=0.05,
):
    """Plots a bar chart to analyse a categorical feature.

    Args:
        data_frame (pd.DataFrame): the data under analysis.
        column (str): the categorical column to be analysed.
        figsize (tuple, optional): the figure size. Defaults to (5, 4).
        sort (bool, optional): if the bar chart is to be sorted or not. Defaults to True.
        normalize (bool, optional): if true, show the frequency; if false, shows the count. Defaults to True.
        plot_h_line (bool, optional): if true, plots an horizontal line. Defaults to False.
        h_threshold (float, optional): the value at which to plot the horizontal line. Defaults to 0.05.
    """

    figure(figsize=figsize)

    if column in data_frame.columns:
        data_frame[column].value_counts(sort=sort, normalize=normalize).plot(kind="bar")

    if plot_h_line:
        plt.axhline(y=h_threshold, color="r", linestyle="--")

    plt.xlabel(column)

    if normalize:
        plt.ylabel("Frequency")
    else:
        plt.ylabel("Count")

    plt.show()

def plot_numerical_feature(data_frame: pd.DataFrame, column: str, figsize=(10, 4), bins=15, plot_qq=False):
    """Auxilary function for plotting numerical variables. Plots a histogram,
    box plot and QQ plot.

    Args:
        data_frame (pd.DataFrame): the data under analysis.
        column (str): the numerical column to be analysed.
        figsize (tuple, optional): the figure size. Defaults to (10, 4).
        bins (int, optional): the number of bins in the histogram. Defaults to 15.
        plot_qq (bool, optional): if the QQ plot is to be plotted or not. Defaults to False.
    """

    if plot_qq:
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=figsize)
    else:
        fig, axs = plt.subplots(
            nrows=1, ncols=2, figsize=figsize, constrained_layout=True
        )

    if column in data_frame.columns:
        data_frame[column].plot(kind="hist", bins=bins, ax=axs[0])
        data_frame[column].plot(kind="box", ax=axs[1])

    if plot_qq:
        sm.qqplot(data_frame[column].dropna(), line="45", fit=True, ax=axs[2])

    axs[0].set_xlabel(column)

    plt.tight_layout()
    plt.show()
   
def get_outlier_records(data_frame: pd.DataFrame, column: str):
    """Function to get the outlier records of a certain variable.

    Args:
        data_frame (pd.DataFrame): the data under analysis.
        column (str): the variable to analyze.

    Returns:
        pd.DataFrame: the subset of data_frame containing only
        the records concerning outliers.
    """

    if column not in data_frame.columns:
        print(f"The column {column} is not present in the data.")
        return None
    else:
        q1 = data_frame[column].quantile(0.25)
        q3 = data_frame[column].quantile(0.75)
        iqr = q3 - q1

        threshold = 1.5

        return data_frame.loc[
            (data_frame[column] < (q1 - iqr * threshold))
            | (data_frame[column] > (q3 + iqr * threshold))
        ]