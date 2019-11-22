import keyring
from tradingview import TradingView


TRADINGVIEW_USERNAME = "TTesseract"
TRADINGVIEW_PASSWORD = keyring.get_password("tradingview.com", TRADINGVIEW_USERNAME)

DEGIRO_USERNAME = "CodeArtha"
DEGIRO_PASSWORD = keyring.get_password("degiro.nl", DEGIRO_USERNAME)

tv = TradingView(TRADINGVIEW_USERNAME, TRADINGVIEW_PASSWORD)
tv.connect()