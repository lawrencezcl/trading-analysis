"""
获取市场数据的脚本
由于没有金融 API，这里会使用公开数据源或模拟数据
"""

import json
from datetime import datetime
import subprocess

# 尝试使用 yfinance 获取数据
def get_yahoo_data():
    try:
        import yfinance as yf
        
        # 标普500相关
        spy = yf.Ticker("SPY")
        spx = yf.Ticker("^GSPC")
        
        # 纳斯达克100相关
        qqq = yf.Ticker("QQQ")
        ndx = yf.Ticker("^NDX")
        
        # VIX
        vix = yf.Ticker("^VIX")
        
        data = {
            "timestamp": datetime.now().isoformat(),
            "SPY": {
                "current_price": spy.history(period="1d").iloc[-1]['Close'] if len(spy.history(period="1d")) > 0 else None,
                "info": spy.info
            },
            "QQQ": {
                "current_price": qqq.history(period="1d").iloc[-1]['Close'] if len(qqq.history(period="1d")) > 0 else None,
                "info": qqq.info
            },
            "VIX": {
                "current_price": vix.history(period="1d").iloc[-1]['Close'] if len(vix.history(period="1d")) > 0 else None,
            }
        }
        
        return data
        
    except ImportError:
        print("yfinance not installed")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # 首先尝试安装 yfinance
    try:
        import yfinance
    except ImportError:
        print("Installing yfinance...")
        subprocess.run(["pip", "install", "yfinance"], check=True)
    
    data = get_yahoo_data()
    if data:
        with open("market_data.json", "w") as f:
            json.dump(data, f, indent=2, default=str)
        print("Data saved to market_data.json")
    else:
        print("Failed to get market data")
