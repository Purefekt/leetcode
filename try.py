import datetime

trades = {
    "Trade1": {
        "date": "2022-03-15",
        "time": "9:01:00",
        "type": "Broker",
        "qty": -500,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "737acm",
        "product": "ABC"
    },
    "Trade2": {
        "date": "2022-03-15",
        "time": "9:00:24",
        "type": "Electronic",
        "qty": -200,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "w6c229",
        "product": "ABC"
    },
    "Trade3": {
        "date": "2022-03-15",
        "time": "9:03:45",
        "type": "Electronic",
        "qty": -100,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "tssrin",
        "product": "ABC"
    },
    "Trade4": {
        "date": "2022-03-15",
        "time": "9:00:53",
        "type": "Electronic",
        "qty": -500,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "lk451a",
        "product": "XYZ"
    },
    "Trade5": {
        "date": "2022-03-15",
        "time": "9:00:05",
        "type": "Electronic",
        "qty": -350,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "C",
        "exchange": "CBOE",
        "trade-id": "9numpr",
        "product": "ABC"
    },
    "Trade6": {
        "date": "2022-03-15",
        "time": "9:00:35",
        "type": "Electronic",
        "qty": 200,
        "strike": 1500,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "922v3g",
        "product": "ABC"
    },
    "Trade7": {
        "date": "2022-03-15",
        "time": "9:00:47",
        "type": "Electronic",
        "qty": -150,
        "strike": 1500,
        "expiry": "2022-04-21",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "bg54nm",
        "product": "ABC"
    },
    "Trade8": {
        "date": "2022-03-15",
        "time": "9:02:23",
        "type": "Electronic",
        "qty": -200,
        "strike": 1550,
        "expiry": "2022-04-28",
        "kind": "P",
        "exchange": "CBOE",
        "trade-id": "6y7fhm",
        "product": "ABC"
    }
}


class Trades:

    @ staticmethod
    # helper function to get timestamp from given date time
    def _get_timestamp(date: str, time: str):
        date_time_string = date + ' ' + time
        date_time_object = datetime.datetime.strptime(date_time_string, '%Y-%m-%d %H:%M:%S')
        return date_time_object.timestamp()

    def __init__(self, trades: dict) -> None:
        # split trades into electronic and broker. Change neg qty to sell and pos qty to buy. Add timestamps to the trades.
        self.electronic_trades = {}
        self.broker_trades = {}
        for trade in trades.keys():
            if trades[trade]["type"] == "Broker":
                self.broker_trades[trade] = trades[trade]
                self.broker_trades[trade]["timestamp"] = self._get_timestamp(date=trades[trade]["date"], time=trades[trade]["time"])
                if self.broker_trades[trade]["qty"] < 0:
                    self.broker_trades[trade]["qty"] = "Sell"
                elif self.broker_trades[trade]["qty"] > 0:
                    self.broker_trades[trade]["qty"] = "Buy"
            elif trades[trade]["type"] == "Electronic":
                self.electronic_trades[trade] = trades[trade]
                self.electronic_trades[trade]["timestamp"] = self._get_timestamp(date=trades[trade]["date"], time=trades[trade]["time"])
                if self.electronic_trades[trade]["qty"] < 0:
                    self.electronic_trades[trade]["qty"] = "Sell"
                elif self.electronic_trades[trade]["qty"] > 0:
                    self.electronic_trades[trade]["qty"] = "Buy"

    def __str__(self) -> str:
        return f"""
        Broker transactions info ==> \n{self.broker_trades}
        Electronic transactions info ==> {self.electronic_trades}
        """  

    def __repr__(self) -> str:
        return f'Trades(trades=trades)'

    def get_illegal_trades(self):
        # add valid pairs as tuples (electronic_timestamp, (broker_id, electronic_id))
        pairs_to_sort = []
        for electronic_trade in self.electronic_trades.keys():
            for broker_trade in self.broker_trades.keys():

                if self.electronic_trades[electronic_trade]["timestamp"] >= self.broker_trades[broker_trade]["timestamp"]-60 and self.electronic_trades[electronic_trade]["timestamp"] < self.broker_trades[broker_trade]["timestamp"] and self.electronic_trades[electronic_trade]["product"] == self.broker_trades[broker_trade]["product"] and self.electronic_trades[electronic_trade]["kind"] == self.broker_trades[broker_trade]["kind"] and self.electronic_trades[electronic_trade]["qty"] == self.broker_trades[broker_trade]["qty"] and self.electronic_trades[electronic_trade]["expiry"] == self.broker_trades[broker_trade]["expiry"] and self.electronic_trades[electronic_trade]["strike"] == self.broker_trades[broker_trade]["strike"]:
                    pairs_to_sort.append((self.electronic_trades[electronic_trade]["timestamp"], (self.broker_trades[broker_trade]["trade-id"], self.electronic_trades[electronic_trade]["trade-id"])))

        # sort the pairs according to electronic time
        pairs_to_sort.sort()

        # extract only the pairs without the timestamps
        pairs = []
        for _, pair in pairs_to_sort:
            pairs.append(pair)
        
        return pairs


T = Trades(trades)
print(T.get_illegal_trades())