import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from prophet import Prophet


class AnalyzeForecast:
    """
    A class to analyze and forecast time series data specifically
    designed for EUR/USD data.
    This class provides methods to visualize data trends,
    plot moving averages, and forecast using Facebook's Prophet model.

    Attributes:
        data (pd.DataFrame): A DataFrame containing the time series data.
    """

    def __init__(self, data):
        # Assertion checks for the input data
        assert isinstance(data, pd.DataFrame), "Input must be a PD DataFrame."
        assert pd.api.types.is_numeric_dtype(
            data["price"]
        ), "The 'price' column must contain numeric data."
        self.data = data

    # Method to ensure the DataFrame has 'date' as a datetime index.
    def setup_date_index(self):
        """
        Ensures 'date' is the DataFrame index and converts it to a
        datetime index if necessary.
        """
        if "date" not in self.data.columns:
            self.data.reset_index(inplace=True)
        # Convert the 'date' column to datetime type and set it
        # as the DataFrame index.
        self.data["date"] = pd.to_datetime(self.data["date"])
        self.data.set_index("date", inplace=True)

    # Method to extract features and prepare data for analysis.
    def extract_features(self):
        """
        Prepares data for analysis by setting up the index,
        interpolating missing values, and calculating moving averages.
        """
        # Prepare the DataFrame index.
        self.setup_date_index()
        # Extract the year from the 'date' index for later grouping by year.
        self.data["year"] = self.data.index.year
        # Interpolate missing values in 'price' to prepare
        # clean data for decomposition.
        self.data["price"].interpolate(inplace=True)
        # Perform seasonal decomposition on 'price' to separate trend and
        # other components.
        self.decomposition = seasonal_decompose(
            self.data["price"], model="additive", period=365
        )
        assert self.decomposition is not None, "Seasonal decomposition failed."
        # Store the trend component in the DataFrame.
        self.data["trend"] = self.decomposition.trend
        # Calculate and store 360-day and 180-day moving averages of 'price'.
        self.data["MA360"] = self.data["price"].rolling(window=360).mean()
        self.data["MA180"] = self.data["price"].rolling(window=180).mean()

    # Method to plot time series data along with the trend component.
    def plot_time_series_trend(self):
        """
        Plots the initial time series data along with the trend component,
        and initializes animation frames to display data changes over years.
        """
        # Call the method to extract features and prepare the data.
        self.extract_features()
        # Identify the initial year from the data for the initial plot setup.
        initial_year = self.data["year"].min()
        initial_data = self.data[self.data["year"] == initial_year]
        # Initialize a figure object for plotting.
        fig = go.Figure()
        # Add a line trace for the 'price' data.
        fig.add_trace(
            go.Scatter(
                x=initial_data.index,
                y=initial_data["price"],
                mode="lines",
                name="Price",
            )
        )
        # Add a line trace for the 'trend' data.
        fig.add_trace(
            go.Scatter(
                x=initial_data.index,
                y=initial_data["trend"],
                mode="lines",
                name="Trend",
            )
        )
        # Call a custom method to update the plot layout.
        self._update_plot_layout(fig)
        # Set the overall title of the plot.
        fig.update_layout(title="EUR/USD Price with Trend Over Time")
        # Prepare animation frames for each year, showing cumulative
        # data up to that year.
        frames = []
        for year in sorted(self.data["year"].unique()):
            year_data = self.data[self.data["year"] <= year]
            frames.append(
                go.Frame(
                    data=[
                        go.Scatter(
                            x=year_data.index,
                            y=year_data["price"],
                            mode="lines",
                            name="Price",
                        ),
                        go.Scatter(
                            x=year_data.index,
                            y=year_data["trend"],
                            mode="lines",
                            name="Trend",
                        ),
                    ],
                    name=str(year),
                )
            )
        # Assign the prepared frames to the figure for animation.
        fig.frames = frames
        fig.show()

    # Method to plot the moving average crossover trend.
    def plot_ma_crossover_trend(self):
        # Extract features and ensure the data is ready for
        # plotting, moving averages.
        self.extract_features()
        # Retrieve the minimum year from the data to establish the
        # starting point for the plot.
        initial_year = self.data["year"].min()
        # Fetch the initial year's data for plotting the starting frame.
        initial_data = self.data[self.data["year"] == initial_year]
        # Initialize a plotly figure for interactive plotting.
        fig = go.Figure()
        # Add a trace for the original price data.
        fig.add_trace(
            go.Scatter(
                x=initial_data.index,
                y=initial_data["price"],
                mode="lines",
                name="Price",
            )
        )
        # Add a trace for the 360-day moving average to visualize
        # long-term trends.
        fig.add_trace(
            go.Scatter(
                x=initial_data.index,
                y=initial_data["MA360"],
                mode="lines",
                name="360-Day MA",
            )
        )
        # Add a trace for the 180-day moving average to visualize
        # medium-term trends.
        fig.add_trace(
            go.Scatter(
                x=initial_data.index,
                y=initial_data["MA180"],
                mode="lines",
                name="180-Day MA",
            )
        )
        # Call a custom method to update the plot layout, setting labels,
        # and styles.
        self._update_plot_layout(fig)
        # Update the layout of the figure to set a title.
        fig.update_layout(
            title="EUR/USD Price with Two Moving Average Crossover Trend"
        )
        # Initialize a list to store frames for animation, showing
        # data evolution over years.
        frames = []
        # Loop through each unique year, appending data up to that
        # year to the frames for animation.
        for year in sorted(self.data["year"].unique()):
            year_data = self.data[self.data["year"] <= year]
            frames.append(
                go.Frame(
                    data=[
                        go.Scatter(
                            x=year_data.index,
                            y=year_data["price"],
                            mode="lines",
                            name="Price",
                        ),
                        go.Scatter(
                            x=year_data.index,
                            y=year_data["MA360"],
                            mode="lines",
                            name="360-Day MA",
                        ),
                        go.Scatter(
                            x=year_data.index,
                            y=year_data["MA180"],
                            mode="lines",
                            name="180-Day MA",
                        ),
                    ],
                    name=str(year),
                )
            )
        # Assign the frames to the figure for animation.
        fig.frames = frames
        fig.show()

    # Method to perform forecasting using the Prophet library.
    def perform_forecasting(self):
        """
        Perform forecasting using the Prophet library, plot the forecast,
        and show it with proper labeling and titling.
        """
        # Assertion checks for the input data
        assert (
            "price" in self.data.columns
        ), "DataFrame must 'price' columns."
        # Reset the DataFrame index to ensure 'date' is
        # a column which is needed for Prophet.
        self.data.reset_index(inplace=True)
        # Rename the columns for compatibility with Prophet, which
        # requires 'ds' for dates and 'y' for values.
        self.data.rename(columns={"date": "ds", "price": "y"}, inplace=True)
        # Initialize a Prophet model.
        model = Prophet()
        # Fit the model using historical data.
        model.fit(self.data)
        # Generate future date data frame for the next 365 days to forecast.
        future = model.make_future_dataframe(periods=365)
        # Use the model to make predictions based on the future DataFrame.
        forecast = model.predict(future)
        # Plot the forecasts using Prophet's built-in plotting function.
        model.plot(forecast)
        # Set the title, x-label, and y-label for the plot.
        plt.title("Forecasting EUR/USD Price Trend Direction Using Prophet")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()

    # Method to update the layout of the plotly figure for
    # better visualization.
    def _update_plot_layout(self, fig):
        # Update the layout of the plotly figure to enhance
        # visual appeal and interactivity.
        fig.update_layout(
            xaxis=dict(
                title="Date",
                range=[self.data.index.min(), self.data.index.max()]
            ),
            # Configure the y-axis with a title and set the range
            # to cover all price values in the data.
            yaxis=dict(
                title="Price (USD)",
                range=[self.data["price"].min(), self.data["price"].max()],
            ),
            # Add interactive buttons to the plot to control the animation.
            updatemenus=[
                {
                    "type": "buttons",
                    "buttons": [
                        {
                            "label": "Play",
                            "method": "animate",
                            "args": [
                                # No specific frames to animate to,
                                # use all frames.
                                None,
                                {
                                    "frame": {
                                        "duration": 500,
                                        "redraw": True,
                                    },  # Frame transition options.
                                    # Start animation from the current frame.
                                    "fromcurrent": True,
                                    "transition": {
                                        "duration": 300
                                    },  # Transition duration.
                                },
                            ],
                        },
                        {
                            "label": "Pause",
                            "method": "animate",
                            "args": [
                                [None],
                                {
                                    "frame": {
                                        "duration": 0,
                                        "redraw": False,
                                    },  # No redraw while paused.
                                    "mode": "immediate",
                                    # Instant pause.
                                    "transition": {"duration": 0},
                                },
                            ],
                        },
                    ],
                }
            ],
            # Set the size of the figure for better visibility.
            width=1000,  # Width of the figure in pixels
            height=600,  # Height of the figure in pixels
        )
