from config import config
import yfinance as yf
import datetime

date = datetime.datetime.strptime(config.reference_date, '%Y-%m-%d')
tickers = list(config.stock_dict)

# Get stock data at reference date
df = yf.download(tickers, start=config.reference_date, end=date + datetime.timedelta(days=1), interval='1d', group_by='ticker')
# Get stock data at latest date
df_now = yf.download(tickers, interval='1d', group_by='ticker', period = '1d')

# Filter out data except Closing values
cols = []
cols_now = []
for i in range(len(df.columns)):
    if df.columns[i][1] == 'Close':
        cols.append(i)
    if df_now.columns[i][1] == 'Close':
        cols_now.append(i)
df = df[df.columns[cols]]
df_now = df_now[df_now.columns[cols_now]]

result_file = open("result.txt", "w")

# Compute current worth
total_money = config.reference_nav * config.reference_no_of_unit
current_worth = 0
for ticker in config.stock_dict.keys():
    shares = total_money * config.stock_dict[ticker] / float(df[ticker].iloc[0]) / 100.0
    value = shares * float(df_now[ticker].iloc[0])

    current_worth += value
    result_file.write(str(ticker) + "\n Number of shares: $" + "{:.2f}".format(round(shares,2)) + "\n Current Value: $" + "{:.2f}".format(round(value,2)) + "\n")

# Consider Cash
current_worth += config.cash * total_money / 100.0
result_file.write("Cash\n Current Value: $" + "{:.2f}".format(round(config.cash * total_money / 100.0), 2) + "\n")

result_file.write("\nCurrent estimated NAV: $" + "{:.2f}".format(round(current_worth / config.reference_no_of_unit, 2)))
result_file.close()