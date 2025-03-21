import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


class DataVisualizer:
    def __init__(self, data):
        """
        Initialize the DataVisualizer with data and perform
        seasonal decomposition.

        Args:
        data (DataFrame): The dataset containing at least
        a 'price' column with numerical values.

        Decomposes the 'price' column into its trend, seasonal, and
        residual components using an additive model.
        """
        # Assertion checks for the input data
        assert isinstance(data, pd.DataFrame), "Input must be PD DataFrame."
        assert "price" in data.columns, "DataFrame must have 'price' column."
        assert pd.api.types.is_numeric_dtype(data["price"]), "Numeric required"

        self.data = data
        # This uses an additive model with a periodicity
        # of 365 days (assuming daily data).
        self.decomposition = seasonal_decompose(
            self.data["price"], model="additive", period=365
        )

    # Method to plot the original time series data.
    def plot_time_series(self):
        """
        Plot the original time series data from the 'price' column.

        Uses Seaborn to create a line plot with the 'whitegrid' style for
        better readability.
        """
        sns.set_style("whitegrid")
        plt.figure(figsize=(14, 10))
        # Plot the 'price' data as a line plot, labeling it as 'Original'.
        sns.lineplot(
            data=self.data,
            x=self.data.index,
            y="price",
            label="Original",
            linewidth=2.5,
        )
        # Add a legend to the upper left corner of the plot.
        plt.legend(loc="upper left")
        # Set the title of the plot.
        plt.title("Original Time Series")
        # Display the plot.
        plt.show()

    # Method to plot the Trend component extracted by seasonal decomposition.
    def plot_Trend_Component(self):
        """
        Plot the Trend component of the time series data extracted from
        seasonal decomposition.

        The plot visualizes the underlying trend in the 'price' data which can
        highlight long-term patterns.
        """
        plt.figure(figsize=(10, 6))
        # Plot the trend component, label it as 'Trend'.
        plt.plot(self.decomposition.trend, label="Trend")
        plt.legend(loc="upper left")
        plt.title("Trend Component")
        plt.show()

    # Method to plot the Seasonal component extracted by
    # seasonal decomposition.
    def plot_Seasonal_Component(self):
        """
        Plot the Seasonal component of the time series data extracted
        from seasonal decomposition.

        This plot helps visualize the regular patterns or cycles in
        the 'price' data across a typical year.
        """
        plt.figure(figsize=(10, 6))
        # Plot the seasonal component, label it as 'Seasonality'.
        plt.plot(self.decomposition.seasonal, label="Seasonality")
        plt.legend(loc="upper left")
        plt.title("Seasonal Component")
        plt.show()

    # Method to plot the Residual component extracted by
    # seasonal decomposition.
    def plot_Residual_Component(self):
        """
        Plot the Residual component of the time series data extracted
        from seasonal decomposition.

        Residuals are the differences between observed values and the values
        predicted by the model, indicating randomness or anomalies.
        """
        plt.figure(figsize=(10, 6))
        # Plot the residual component, label it as 'Residual'.
        plt.plot(self.decomposition.resid, label="Residual")
        plt.legend(loc="upper left")
        plt.title("Residual Component")
        plt.show()
