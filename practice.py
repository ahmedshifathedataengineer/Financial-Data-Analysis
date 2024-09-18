import pandas as pd 

#Create series for stock closing prices
closing_prices = pd.Series([150, 152, 148, 149, 153], name='Closing')

#Display series
print("Series of Opening Prices")
print(closing_prices)

#Create a pandas dataFrame
stock_data = pd.DataFrame({
     'Open': [149, 151, 147, 148, 152],
    'Close': [150, 152, 148, 149, 153],
    'High': [151, 153, 149, 150, 154],
    'Low': [148, 150, 146, 147, 151],
    'Volume': [1000, 1100, 900, 1050, 1200]
})

print("DataFrame of Stock Data")
print(stock_data)

#Selecting Close column
closing_prices = stock_data['Close']
print('Closing Prices:')
print(closing_prices)