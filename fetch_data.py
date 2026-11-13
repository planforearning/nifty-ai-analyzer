import json
import datetime
import yfinance as yf

def fetch_nifty_data():
    print("Fetching live NIFTY 50 data from Yahoo Finance...")
    
    # NIFTY 50 ticker on Yahoo Finance (^NSEI)
    nifty = yf.Ticker("^NSEI")
    
    # Last 3 months ka daily/intraday data nikalne ke liye
    df = nifty.history(period="3mo", interval="1d")
    
    if df.empty:
        print("Error: Data fetch nahi ho paya!")
        return

    # Dates aur Closing prices ki list taiyar karna
    dates = df.index.strftime('%d %b').tolist()
    prices = df['Close'].round(2).tolist()
    
    # JSON data structure
    data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": "NIFTY 50",
        "dates": dates,
        "prices": prices
    }
    
    # data.json file mein save karna
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
        
    print("Successfully updated data.json with live NIFTY data!")

if __name__ == "__main__":
    fetch_nifty_data()
