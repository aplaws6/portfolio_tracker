Stock Portfolio Tracker

A Python script that pulls historical price data for five stocks, calculates their daily returns, and plots a side-by-side comparison chart, so you can see at a glance how each holding has performed over time.

Data is retrieved for free using the yfinance library, which accesses Yahoo Finance market data.

Features
- Downloads historical daily price data for 5 stocks
- Calculates daily percentage returns for each stock
- Plots a comparison chart of the stocks' performance
- Easy to customise: change the tickers and date range at the top of the script

Example Output
<!-- Replace with a screenshot of your chart, e.g. save it as images/comparison_chart.png -->

Comparison chart

Tech Stack
Python 3.9+
yfinance: market data
pandas: data handling and return calculations
matplotlib: charting

Getting Started
1. Clone the repository
bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2. (Recommended) Create a virtual environment
bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3. Install dependencies
bash
pip install -r requirements.txt

If you don't have a requirements.txt yet, generate one with pip freeze > requirements.txt, or install directly:

bash
pip install yfinance pandas matplotlib
4. Run the script
bash
python portfolio_tracker.py

Configuration

Edit the settings near the top of the script to track different stocks or time periods:

python
TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]   # replace with your own five
START_DATE = "2023-01-01"
END_DATE = "2024-01-01"

Adjust the variable names above to match those in your code.

How It Works
Fetch data: yfinance downloads historical price data for each ticker over the chosen date range.
Calculate returns: daily returns are computed as the percentage change in closing price from one day to the next (pandas.DataFrame.pct_change()).
Visualise: the results are plotted on a single chart so the stocks can be compared directly.
Project Structure
.
├── portfolio_tracker.py     # Main script
├── requirements.txt         # Python dependencies
├── images/
│   └── comparison_chart.png # Example output
└── README.md

Possible Improvements
Add portfolio weighting to calculate overall portfolio returns
Include cumulative returns and volatility metrics
Export results to CSV or Excel
Accept tickers and dates as command-line arguments
Build an interactive version with Plotly or Streamlit

Disclaimer
This project is for learning and educational purposes only. It is not financial advice. Data comes from Yahoo Finance via yfinance, which is intended for personal use, so check Yahoo's terms of use before relying on it for anything else. Data accuracy and availability are not guaranteed.

About
Built as part of my journey learning Python. Feedback and suggestions are welcome, so feel free to open an issue or get in touch.

License
Released under the MIT License. <!-- Add a LICENSE file via GitHub's "Add file" > "Create new file" > type LICENSE for templates -->
