# StockTool

In the config.py, the reference date, NAV, and number of unit represent their corresponding value of a mutual fund at a particular date. stock_dict holds the stocks ticker and the corresponding percentage they take up in the mutual fund. Cash value represent percentage of money not put into any stock by the mutual fund. Ensure the date is in the format yyyy-mm-dd. Ensure tickers are capitalized and all percentage are shown with percentage sign omitted (ie. x.x is x.x% in config file).

## Installation
1. Ensure python 3.12.3 is installed
2. In terminal, cd to the root of the project folder and run
```
pip install -r requirements.txt
python main.py 
```
3. View result in result.txt