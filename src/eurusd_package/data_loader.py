import pandas as pd
import os


class DataLoader:
    """
    A data loader class for loading and preprocessing the data.

    This class handles reading a CSV file containing data, performing initial
    preprocessing, and setting the DataFrame index to a datetime index sorted
    in ascending order.

    Attributes:
        filename (str): The name of the file to load.
        Defaults to 'EURUSD_data.csv'.
        base_path (str): The base directory path where the data
        file is located.
        filepath (str): The full path to the data file.
        data (pd.DataFrame): The loaded data after preprocessing.

    Methods:
        load_data: Loads data from a CSV file into a DataFrame.
        preprocess_data: Performs data cleaning and preprocessing.
        get_data: Returns the preprocessed data.
    """

    def __init__(self, filename="EURUSD_data.csv"):
        """
        Initializes the DataLoader with a specific filename.

        Args:
            filename (str): Name of the CSV file to load.
            Defaults to 'EURUSD_data.csv'.

        Raises:
            FileNotFoundError: If the CSV file is not found in the specified
            path.
        """
        assert isinstance(filename, str), "Filename must be a string."
        self.base_path = os.getcwd()  # Gets the current working directory
        self.filepath = os.path.join(self.base_path, "data", filename)
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(
                f"File '{self.filepath}' not found. Please check the path."
            )
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Loads data from the specified CSV file into a pandas DataFrame.

        Raises:
            Exception: An error occurred accessing the CSV file.
        """
        try:
            self.data = pd.read_csv(self.filepath)
            assert not self.data.empty, "Data loaded is empty."
        except Exception as e:
            print(f"Error loading data: {e}")

    def preprocess_data(self):
        """
        Preprocesses the loaded data, including converting date columns
        to datetime, dropping entirely NaN columns, and normalizing
        column names.

        It sets the 'Date' column as the DataFrame index and
        sorts it in ascending order.
        """
        if self.data is None:
            print("No data to preprocess.")
            return
        assert 'Date' in self.data.columns, "Data must have a 'Date' column."
        # Convert 'Date' to datetime
        self.data["Date"] = pd.to_datetime(self.data["Date"], dayfirst=True)

        # Drop columns that are completely NaN
        columns_with_all_nans = [
            col for col in self.data.columns if self.data[col].isna().all()
        ]
        self.data.drop(columns=columns_with_all_nans, inplace=True)

        # Standardize column names
        self.data.columns = (
            self.data.columns.str.strip()
            .str.lower()
            .str.replace(r"[^\w\s]", "", regex=True)
            .str.replace(" ", "")
        )

        # Convert 'change' column to 'change_percentage' and remove '%'
        if "change" in self.data.columns:
            self.data.rename(
                columns={"change": "change_in_percentage"},
                inplace=True
            )
            self.data["change_in_percentage"] = (
                self.data["change_in_percentage"]
                .astype(str)
                .str.rstrip("%")
                .astype(float)
            )

        # Set 'Date' as index
        self.data.set_index("date", inplace=True)
        self.data.sort_index(inplace=True)

    def get_data(self):
        """
        Returns the preprocessed data as a pandas DataFrame.
        """
        return self.data


# Test the class
if __name__ == "__main__":
    loader = DataLoader()  # Initialize DataLoader (loads data automatically)
    # print("Before preprocessing:")
    # print(loader.get_data().head())  # Check raw data

    loader.preprocess_data()  # Apply preprocessing
    print("\nAfter preprocessing:")
    print(loader.get_data().head())  # Check cleaned data
