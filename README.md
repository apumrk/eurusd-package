# 📌 EURUSD Package

[![PyPI - Version](https://img.shields.io/pypi/v/eurusd-package.svg)](https://pypi.org/project/eurusd-package)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/eurusd-package.svg)](https://pypi.org/project/eurusd-package)

---
## 📖 Overview
EURUSD Package is a Python package for analyzing and forecasting the EUR/USD exchange rate using various statistical and machine learning methods. It integrates data loading, preprocessing, visualization, and prediction functionalities tailored to financial time series data. The completion of such project is the task of the course "[Introduction to Python](https://github.com/florence-bockting/python-class-25)"

-----

## 📚 Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
  - [Data Loading](#data-loading)
  - [Data Analysis](#data-analysis)
  - [Forecasting](#forecasting)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## ⚙️ Installation

Install the latest version of EURUSD Package directly from the GitHub repository:

```console
pip install git+https://github.com/apumrk/eurusd-package
```
Ensure your environment is set up with Python 3.6+ to use the package effectively.

## 🌟 Features

- 📂 **Data Loader**: Simplifies the process of loading and preprocessing EUR/USD exchange rate data.
- 🔍 **Data Analyzer**: Provides tools to perform detailed exploratory analysis, including statistical summaries and graphical representations.
- 📊 **Visualization**: Integrated visualization tools to plot time series data, trends, and model predictions.
- 📉 **Forecasting**: Leverages advanced algorithms like Facebook's Prophet to forecast future movements in the EUR/USD exchange rate.

## 🛠 Usage

### 📂 Data Loading

To load your data:

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
