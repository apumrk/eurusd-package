# 📌 EURUSD Package

[![PyPI - Version](https://img.shields.io/pypi/v/eurusd-package.svg)](https://pypi.org/project/eurusd-package)

---
## 📖 Overview
EURUSD Package is a Python package for analyzing and forecasting the EUR/USD exchange rate using various statistical and machine learning methods. It integrates data loading, preprocessing, visualization, and prediction functionalities tailored to financial time series data. The completion of such project is the task of the course "[Introduction to Python](https://github.com/florence-bockting/python-class-25)"

-----

## 📚 Table of Contents

- Installation
- Dataset Overview
- Features
- Usage
  - Data Loading
  - Data Analysis
  - Forecasting
- View in Google Colab
- Contributors
- Contributing
- License
- Support

## ⚙️ Installation

Install the latest version of EURUSD Package directly from the GitHub repository:

```console
pip install git+https://github.com/apumrk/eurusd-package
```
Ensure your environment is set up with Python 3.6+ to use the package effectively.
## 🗂 Dataset Overview

**Source:** [Historical EUR/USD exchange rate data (2000–2025)](https://www.kaggle.com/datasets/saifansariai/euro-usd-price-2001-to-2025)

**Frequency:** Daily  
**Rows:** 11,284   
**Columns:** 7   
**Format:** CSV  
**Columns:**
- **Date** – Date of recorded exchange rate (Format: DD-MM-YYYY)
- **Price** – Closing price of EUR/USD
- **Open** – Opening price
- **High** – Highest price of the day
- **Low** – Lowest price of the day
- **Vol.** – Volume (all values are NaN)
- **Change %** – Percent change from previous day (as string with % sign)

## 🌟 Features

- 📂 **Data Loader**: Simplifies the process of loading and preprocessing EUR/USD exchange rate data.
- 🔍 **Data Analyzer**: Provides tools to perform detailed exploratory analysis, including statistical summaries and graphical representations.
- 📊 **Visualization**: Integrated visualization tools to plot time series data, trends, and model predictions.
- 📉 **Forecasting**: Leverages advanced algorithms like Facebook's Prophet to forecast future movements in the EUR/USD exchange rate.

## 🛠 Usage

### 📂 Data Loading

To ensure the `DataLoader` can successfully load your data, please follow these steps:

1. **Create a Directory**: Navigate to the working directory of your project where your scripts or Jupyter notebooks are located. Inside this directory, create a new folder named `data`.

2. **Add Data File**: Place your data file, which by default should be named `EURUSD_data.csv`, into the `data` folder. If you use a different filename or have multiple data sets, make sure to specify the correct file name when initializing the `DataLoader`.

3. **Initialize DataLoader**: When you set up `DataLoader` in your script or notebook, it will automatically look for the data file in the `data` subdirectory. Here’s how you can initialize the `DataLoader`:

```python
from eurusd_package.data_loader import DataLoader
data_loader = DataLoader() # By default it will Load the "EURUSD_data.csv" data
data = data_loader.get_data()
```

### 🔍 Data Analysis

Analyze your loaded data:

```python
from eurusd_package.dataAnalyzer import DataAnalyzer
analyzer = DataAnalyzer(data)
print(analyzer.describe_data())
print(analyzer.describe_info())
```

### 📉 Forecasting

Forecast future prices:

```python
from eurusd_package.analyzeForecast import AnalyzeForecast
forecast = AnalyzeForecast(data)
forecast.perform_forecasting()
```
## 🔗 View in Google Colab

Due to the size and complexity of the Jupyter Tutorial notebook, it is hosted on Google Colab for better accessibility and interactive experience. You can view and run the notebook by following this link:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ul4zb0sHtGhrSawCNCawKKDxeq3n_m_X?usp=sharing)

## 👥 Contributors

This project was developed by the following individuals of `Group K`:

- [Sumiya Akter Nisher](https://github.com/nisher07) 
- [Nandita Chakrobortty](https://github.com/Tithi07) 
- [Apu Kumar Saha](https://github.com/apumrk) 

## 🤝 Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

`eurusd-package` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## 🆘 Support

For support and inquiries, open an issue on the [GitHub](https://github.com/apumrk/eurusd-package/issues) repository.
