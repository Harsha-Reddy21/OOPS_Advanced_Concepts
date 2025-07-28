import random
from typing import Dict, List

class TradingAccount:
    def __init__(self, account_id: str, owner_name: str, balance: float):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class RiskManagement:
    def assess_portfolio_risk(self) -> str:

        risk_score = random.uniform(0, 1)
        if risk_score < 0.3:
            return 'Low'
        elif risk_score < 0.7:
            return 'Medium'
        else:
            return 'High'

class AnalyticsEngine:
    def analyze_market_trend(self, symbol: str) -> Dict[str, str]:
        trends = ['upward', 'downward', 'sideways']
        return {
            "trend": random.choice(trends),
            "confidence": f"{random.randint(70, 99)}%"
        }

class NotificationSystem:
    def __init__(self):
        self.alerts = []

    def set_price_alert(self, asset: str, target_price: float, condition: str) -> bool:
        self.alerts.append({
            "asset": asset,
            "target_price": target_price,
            "condition": condition
        })
        return True

    def get_pending_notifications(self) -> List[Dict]:
        return self.alerts

class StockTrader(TradingAccount, RiskManagement, AnalyticsEngine):
    def __init__(self, account_id: str, owner_name: str, balance: float):
        super().__init__(account_id, owner_name, balance)

    def calculate_position_size(self, symbol: str, price: float) -> int:
        max_allocation = 0.1 * self.balance  # max 10% per stock
        return int(max_allocation // price)

class CryptoTrader(TradingAccount, RiskManagement, NotificationSystem):
    def __init__(self, account_id: str, owner_name: str, balance: float):
        TradingAccount.__init__(self, account_id, owner_name, balance)
        NotificationSystem.__init__(self)

class ProfessionalTrader(StockTrader, CryptoTrader):
    def __init__(self, account_id: str, owner_name: str, balance: float):
        StockTrader.__init__(self, account_id, owner_name, balance)
        NotificationSystem.__init__(self)  

    def execute_diversified_strategy(self, strategy: Dict) -> Dict:
        stocks = strategy.get("stocks", [])
        crypto = strategy.get("crypto", [])
        allocation = strategy.get("allocation", {"stocks": 0.5, "crypto": 0.5})
        positions = []

        stock_allocation = self.balance * allocation.get("stocks", 0.5)
        crypto_allocation = self.balance * allocation.get("crypto", 0.5)

        for s in stocks:
            pos_size = int((stock_allocation / len(stocks)) // 100)
            positions.append({"asset": s, "type": "stock", "size": pos_size})

        for c in crypto:
            pos_size = int((crypto_allocation / len(crypto)) // 500)
            positions.append({"asset": c, "type": "crypto", "size": pos_size})

        return {
            "status": "executed",
            "positions": positions
        }



stock_trader = StockTrader("ST001", "John Doe", 50000.0)
crypto_trader = CryptoTrader("CT001", "Jane Smith", 25000.0)
pro_trader = ProfessionalTrader("PT001", "Mike Johnson", 100000.0)

mro_names = [cls.__name__ for cls in ProfessionalTrader.__mro__]
assert "ProfessionalTrader" in mro_names
assert "StockTrader" in mro_names
assert "CryptoTrader" in mro_names

assert stock_trader.account_id == 'ST001'
assert stock_trader.balance == 50000.0

deposit_result = stock_trader.deposit(10000.0)
assert stock_trader.balance == 60000.0
assert deposit_result == True

withdraw_result = stock_trader.withdraw(20000.0)
assert stock_trader.balance == 40000.0

risk_level = stock_trader.assess_portfolio_risk()
assert risk_level in ['Low', 'Medium', 'High']

position_size = stock_trader.calculate_position_size("AAPL", 150.0)
assert isinstance(position_size, int)
assert position_size > 0

market_data = stock_trader.analyze_market_trend("AAPL")
assert isinstance(market_data, dict)
assert "trend" in market_data
assert "confidence" in market_data

alert_set = crypto_trader.set_price_alert("BTC", 45000, "above")
assert alert_set == True

notifications = crypto_trader.get_pending_notifications()
assert isinstance(notifications, list)
assert len(notifications) > 0


assert hasattr(pro_trader, 'assess_portfolio_risk')
assert hasattr(pro_trader, 'analyze_market_trend')
assert hasattr(pro_trader, 'set_price_alert')

strategy_result = pro_trader.execute_diversified_strategy({
    "stocks": ["AAPL", "GOOG"],
    "crypto": ["BTC", "ETH"],
    "allocation": {
        "stocks": 0.7,
        "crypto": 0.3
    }
})

assert strategy_result['status'] == 'executed'
assert len(strategy_result['positions']) > 0

print("All tests passed!")
