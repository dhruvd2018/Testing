#pull stock price from yahoo finance and print as table

Path: StockPrice.py
import urllib2
import re
import MySQLdb
def getStockPrice(symbol):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=l1' % symbol
    data = urllib2.urlopen(url).read()
    return data
    
