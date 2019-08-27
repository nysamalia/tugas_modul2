import numpy as np
import pandas as pd

dfTlkm = pd.read_csv(
    'SahamTLKM.csv',
    parse_dates=['Tanggal'],
    index_col=False
)
dfTlkm.set_index('Tanggal', inplace=True)
dfTlkm.sort_index(inplace=True)


dfIsat = pd.read_csv(
    'SahamISAT.csv',
    parse_dates=['Tanggal'],
    index_col=False
)
dfIsat.set_index('Tanggal', inplace=True)
dfIsat.sort_index(inplace=True)


dfExcl = pd.read_csv(
    'SahamEXCL.csv',
    parse_dates=['Tanggal'],
    index_col=False
)
dfExcl.set_index('Tanggal', inplace=True)
dfExcl.sort_index(inplace=True)

dfFren = pd.read_csv(
    'SahamFREN.csv',
    parse_dates=['Tanggal'],
    index_col=False
)
dfFren.set_index('Tanggal', inplace=True)
dfFren.sort_index(inplace=True)

import matplotlib.pyplot as plt
import matplotlib.dates as md

# plt.style.use('seaborn')
# plt.plot(
#     dfTlkm.index, dfTlkm['Close'], 'r',
#     dfIsat.index, dfIsat['Close'], 'y',
#     dfExcl.index, dfExcl['Close'], 'b',
#     dfFren.index, dfFren['Close'], 'g',
# )
# # set axis
# ax = plt.gca()
# ax.xaxis.set_major_locator(md.MonthLocator(
#     interval=3
# ))
# ax.xaxis.set_major_formatter(md.DateFormatter(
#     '%b %y'
# ))
# plt.xlabel('Bulan')
# plt.ylabel('Rupiah')
# plt.xticks(rotation=65)
# plt.legend(['TLKM', 'ISAT', 'EXCL', 'FREN'])
# plt.grid(True)
# plt.show()

# Nasdaq
import requests
url = 'https://kurs.web.id/api/v1/bni'
data = (requests.get(url))
kurs = float(data.json()['jual'])

dfAapl = pd.read_csv(
    'SahamAAPL.csv',
    parse_dates=['Date'],
    index_col=False
)
dfAapl.set_index('Date', inplace=True)
dfAapl.sort_index(inplace=True)
dfAapl = dfAapl*kurs


dfFb = pd.read_csv(
    'SahamFB.csv',
    parse_dates=['Date'],
    index_col=False
)
dfFb.set_index('Date', inplace=True)
dfFb.sort_index(inplace=True)
dfFb = dfFb*kurs

dfGoog = pd.read_csv(
    'SahamGOOG.csv',
    parse_dates=['Date'],
    index_col=False
)
dfGoog.set_index('Date', inplace=True)
dfGoog.sort_index(inplace=True)
dfGoog = dfGoog*kurs

dfMsft = pd.read_csv(
    'SahamMSFT.csv',
    parse_dates=['Date'],
    index_col=False
)
dfMsft.set_index('Date', inplace=True)
dfMsft.sort_index(inplace=True)
dfMsft = dfMsft*kurs

import matplotlib.pyplot as plt
import matplotlib.dates as md

plt.style.use('seaborn')
plt.plot(
    dfTlkm.index, dfTlkm['Close'], 'r',
    dfIsat.index, dfIsat['Close'], 'y',
    dfExcl.index, dfExcl['Close'], 'b',
    dfFren.index, dfFren['Close'], 'g',
    dfAapl.index, dfAapl['Close'], 'K',
    dfFb.index, dfFb['Close'], 'purple',
    dfGoog.index, dfGoog['Close'], 'pink',
    dfMsft.index, dfMsft['Close'], 'silver'
)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MonthLocator(
    interval=3
))
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%b %y'
))
plt.xlabel('Bulan')
plt.ylabel('Rupiah')
plt.xticks(rotation=65)
plt.legend(['TLKM', 'ISAT', 'EXCL', 'FREN','AAPL', 'FB', 'GOOG', 'MSFT'])
plt.grid(True)
plt.yscale('log')
plt.show()