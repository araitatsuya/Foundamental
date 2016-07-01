import time
import urllib2
from urllib2 import urlopen
import csv

MAGICNUM_PBR_PE = 22.5
# https://youtu.be/_uQjGz6jp2E?t=13m2s
#sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']

def  yahooKeyStats(stock):
    try:
        sourceCode = urllib2.urlopen('http://finance.yahoo.com/q/ks?s='+stock).read()
        stock_p = sourceCode.split('<span class="time_rtq_ticker"><span id="yfs_l84_'+stock.lower()+'">')[1].split('</span>')[0]
        pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        per = sourceCode.split('Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        
        #print 'price to book ratio ', pbr
        #print 'Trailing P/E ', per
        #print  float(per) * float(pbr)
        if  float(per) * float(pbr) < MAGICNUM_PBR_PE:
            print stock, stock_p
            #P/E * P/BV < 22.5
    
    except Exception, e:
        #print 'failed in the main loop', str(e)
        pass

spamreader = csv.reader(open('SnP500_Wiki_May27th2016.csv', 'rU'), quotechar='"', delimiter = ',')
# https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
for row in spamreader:
    #print row
    yahooKeyStats(str(row[0]))

###################################################################################
#
# Foundamental #1
#      This little python code finds SNP 500 stock in which P/E * P/BV < 22.5
#
#   1. 5. Warren Buffett Stock Basics: Preston Pysh
#       https://www.youtube.com/watch?v=_uQjGz6jp2E
#   2. List of S&P 500 companies
#       https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
#   3. Yahoo Finance
#       http://finance.yahoo.com/q/ks?s=MMM
#
#
#                                                   May 27th 2016
#                                                       Tatsuya J. Arai
#
#
###################################################################################