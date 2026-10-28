
import os
import matplotlib

# Force a non-interactive backend to prevent window crashes
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# 1. Define your 5 favorite stock tickers
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]

print(f"Fetching historical data for: {', '.join(tickers)}...")

# Download Adjusted Close prices for the past 1 year
data = yf.download(tickers, period="1y", auto_adjust=False)["Adj Close"]

# Handle potential multi-index or empty data issues
if isinstance(data, pd.Series):
  data = data.to_frame()

if data.empty:
  raise ValueError(
      "No data fetched. Please check your ticker symbols or internet"
      " connection."
  )

# 2. Calculate daily percentage returns
daily_returns = data.pct_change().dropna()

# 3. Calculate cumulative returns (growth of a $1 investment) for fair comparison
cumulative_returns = (1 + daily_returns).cumprod() - 1

# 4. Plot the comparison chart
plt.figure(figsize=(12, 6))

for ticker in tickers:
  plt.plot(
      cumulative_returns.index,
      cumulative_returns[ticker] * 100,
      label=ticker,
      linewidth=2,
  )

plt.title(
    "Stock Portfolio Comparison - Cumulative Returns (Past 1 Year)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Cumulative Return (%)", fontsize=12)
plt.axhline(0, color="black", linestyle="--", linewidth=1, alpha=0.7)
plt.legend(title="Tickers", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

# 5. Robust saving mechanism with fallback
script_dir = os.path.dirname(os.path.abspath(__file__))
output_filename = os.path.join(script_dir, "portfolio_performance.png")

try:
  plt.savefig(output_filename, dpi=300)
  print(f"Success! Chart saved at: {output_filename}")
except Exception as e:
  print(f"Primary save failed due to: {e}")
  # Fallback to saving in the system temporary folder which is always writable
  fallback_filename = "/tmp/portfolio_performance.png"
  plt.savefig(fallback_filename, dpi=300)
  print(f"Fallback success! Chart saved at: {fallback_filename}")

# 6. Print a quick summary of key performance metrics
print("\n--- Performance Summary (Past Year) ---")
annualized_return = daily_returns.mean() * 252 * 100
annualized_volatility = daily_returns.std() * (252**0.5) * 100

summary_df = pd.DataFrame(
    {
        "Annualized Return (%)": annualized_return,
        "Annualized Volatility (Risk %)": annualized_volatility,
    }
)
print(summary_df.round(2))
