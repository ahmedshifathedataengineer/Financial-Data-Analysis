import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta

class FinancialAnalyzer:
    def __init__(self, data=None):
        if data is None or 'Sales Qtr - Crore' not in data.columns:
            print("No valid 'Sales Qtr - Crore' column found, generating synthetic data...")
            self.data = self.generate_synthetic_data()
        else:
            self.data = data
            self.data.set_index('Name', inplace=True)
        self.signals = pd.DataFrame(index=self.data.index)

    def calculate_moving_averages(self, short_window=40, long_window=100):
        self.data['Short_MA'] = self.data['Sales Qtr - Crore'].rolling(window=short_window, min_periods=1).mean()
        self.data['Long_MA'] = self.data['Sales Qtr - Crore'].rolling(window=long_window, min_periods=1).mean()

    def identify_buy_sell_signals(self):
        self.signals['Signal'] = 0.0
        self.signals['Short_MA'] = self.data['Short_MA']
        self.signals['Long_MA'] = self.data['Long_MA']
        self.signals['Signal'] = np.where(self.signals['Short_MA'] > self.signals['Long_MA'], 1.0, 0.0)
        self.signals['Position'] = self.signals['Signal'].diff()
        return self.signals

    def calculate_rsi(self, window=14):
        self.data['RSI'] = ta.momentum.RSIIndicator(self.data['Sales Qtr - Crore'], window=window).rsi()
        return self.data['RSI']

    def plot_data(self, short_window=40, long_window=100):
        plt.figure(figsize=(14, 7))

        # Plot Sales and Moving Averages
        plt.plot(self.data['Sales Qtr - Crore'], label='Sales Qtr - Crore', color='black')
        plt.plot(self.data['Short_MA'], label=f'Short MA ({short_window})', color='blue')
        plt.plot(self.data['Long_MA'], label=f'Long MA ({long_window})', color='red')

        # Plot Buy Signals
        plt.plot(self.signals[self.signals['Position'] == 1].index, 
                 self.signals['Short_MA'][self.signals['Position'] == 1],
                 '^', markersize=10, color='g', lw=0, label='Buy Signal')

        # Plot Sell Signals
        plt.plot(self.signals[self.signals['Position'] == -1].index, 
                 self.signals['Short_MA'][self.signals['Position'] == -1],
                 'v', markersize=10, color='r', lw=0, label='Sell Signal')

        plt.title('Quarterly Sales with Buy/Sell Signals')
        plt.legend()

        # Display the plot
        plt.show(block=True)  # Ensure plot stays open in VS Code

    def calculate_metrics(self):
        returns = self.data['Sales Qtr - Crore'].pct_change().dropna()
        cumulative_return = (1 + returns).cumprod()[-1] - 1
        sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252)

        metrics = {
            'Cumulative Return': cumulative_return,
            'Sharpe Ratio': sharpe_ratio
        }
        return metrics
