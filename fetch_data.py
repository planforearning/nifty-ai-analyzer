import yfinance as yf
import json

df = yf.download("^NSEI", period="3mo", interval="1d", progress=False)
closes = df["Close"].squeeze().dropna()

data = {
    "dates": [d.strftime("%d %b") for d in closes.index],
    "prices": [round(float(p), 2) for p in closes.values],
}

with open("data.json", "w") as f:
    json.dump(data, f)