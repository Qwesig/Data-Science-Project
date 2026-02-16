import yfinance as yf
import pandas as pd

# Define ticker
ticker = "EURUSD=X"

# Download data
data = yf.download(ticker, start="2000-01-01", end="2025-01-01")

# Save to CSV
data.to_csv("EURUSD_2000_2025.csv")

# Display first 10 rows
print(data.head(10))

