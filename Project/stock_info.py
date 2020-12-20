# libraries
import urllib.request
from bs4 import BeautifulSoup


class Stock_Object:
    def __init__(self, stockname):
        self.stockname = stockname
        self.url = 'https://ca.finance.yahoo.com/quote/' + self.stockname + '?p=' + self.stockname + '&.tsrc=fin-srch'
        self.price = ""
        self.prev_close = ""
        self.open = ""
        self.bid = ""
        self.ask = ""
        self.volume = ""
        self.avg_volume = ""
        self.marketcap = ""
        self.beta = ""
        self.PE_ratio = ""
        self.EPS_value = ""
        self.oneytarget = ""

    def Update(self):
        # Fetching the html
        request = urllib.request.Request(self.url)
        content = urllib.request.urlopen(request)
        parse = BeautifulSoup(content, 'html.parser')

        #Stock Price
        stockprice = parse.find_all(attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        stockprice_value = stockprice[0].contents # grab first value of resultset and get its contents
        stockprice_str = stockprice_value[0]
        self.price = stockprice_str

        #Data
        pdata = parse.find_all(attrs={'class': 'Trsdu(0.3s)'})
        prev_close_value = pdata[11].contents
        prev_close_str = prev_close_value[0]
        self.prev_close = prev_close_str

        open_value = pdata[12].contents
        open_str = open_value[0]
        self.open = open_str

        bid_value = pdata[13].contents
        bid_str = bid_value[0]
        self.bid = bid_str

        ask_value = pdata[14].contents
        ask_str = ask_value[0]
        self.ask = ask_str

        volume_value = pdata[15].contents
        volume_str = volume_value[0]
        self.volume = volume_str

        avg_volume_value = pdata[16].contents
        avg_volume_str = avg_volume_value[0]
        self.avg_volume = avg_volume_str

        marketcap_value = pdata[17].contents
        marketcap_str = marketcap_value[0]
        self.marketcap = marketcap_str

        beta_value = pdata[18].contents
        beta_str = beta_value[0]
        self.beta = beta_str

        PE_ratio_value = pdata[19].contents
        PE_ratio_str = PE_ratio_value[0]
        self.PE_ratio = PE_ratio_str

        EPS_value = pdata[20].contents
        EPS_str = EPS_value[0]
        self.EPS_value = EPS_str

        oneytarget_value = pdata[21].contents
        oneytarget_str = oneytarget_value[0]
        self.oneytarget = oneytarget_str
