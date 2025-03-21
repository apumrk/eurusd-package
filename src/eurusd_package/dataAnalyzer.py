import pandas as pd


class DataAnalyzer:
    def __init__(self, data):
        """
        Initialize the DataAnalyzer with a dataset.

        Args:
            data (pd.DataFrame): A pandas DataFrame containing the data
            to be analyzed.
        """
        # Assertion checks for the input data
        assert isinstance(data, pd.DataFrame), "Input must be a pd DataFrame."
        assert not data.empty, "Input DataFrame should not be empty."
        self.data = data

    # Method to return descriptive statistics of the DataFrame.
    def describe_data(self):
        """
        Return descriptive statistics of the dataset.

        These statistics include an aggregation of summary statistics
        such as mean, median, mode, standard deviation, etc., for each
        numeric column in the DataFrame.

        Returns:
            None: This method returns None
        """
        return self.data.describe()

    # Method to print a concise summary of the DataFrame.
    def describe_info(self):
        """
        Print a concise summary of the DataFrame.

        This method provides information about the DataFrame including
        the index dtype, column dtypes, non-null values, and memory usage.

        Returns:
            None: This method returns None, but prints the
            DataFrame information.
        """
        return self.data.info()
