# **Financial Data Analysis and Signal Processing**

## **Overview**
This project focuses on analyzing financial data (such as quarterly sales) to derive **actionable insights** using a variety of financial metrics. Whether you’re a **finance professional** looking for decision-making support or a **data enthusiast** exploring financial data, this project provides a thorough analysis, including **moving averages**, **buy/sell signals**, and momentum indicators like the **Relative Strength Index (RSI)**.

---

## **Features**
- **Moving Averages**: Detect **short-term** and **long-term** trends based on quarterly sales data.
- **Buy/Sell Signals**: Automatically detect **buying** and **selling opportunities** based on moving average crossovers.
- **Relative Strength Index (RSI)**: Assess the **momentum** behind quarterly sales and determine whether they are in "overbought" or "oversold" zones.
- **Financial Metrics**: Calculate the **Cumulative Return** and **Sharpe Ratio** to gauge **performance** and **risk**.

---

## **How It Works**
### **Step-by-Step Walkthrough**

#### 1. **Data Loading**
The CSV file containing financial data is loaded into the script. The dataset includes **company names, market cap, quarterly sales**, and more. The analysis is applied to the column that holds quarterly sales data (`Sales Qtr - Crore`).

---python
data = pd.read_csv('Financial-Analytics-data1.csv')

#### 2. **Calculating Moving Averages**
We calculate short-term (40-period) and long-term (100-period) moving averages. These averages help smooth out sales data to highlight trends. A buy signal is generated when the short-term moving average crosses above the long-term, and a sell signal when it crosses below.

analyzer.calculate_moving_averages(short_window=40, long_window=100)
signals = analyzer.identify_buy_sell_signals()

#### 3. **Relative Strength Index (RSI)**
The RSI is used to identify whether the sales are in an overbought or oversold condition. Typically, an RSI above 70 is considered overbought, while an RSI below 30 is considered oversold.

rsi = analyzer.calculate_rsi(window=14)

#### 4. **Plotting Sales Trends**
The script generates a plot to visualize sales trends along with buy/sell signals, allowing you to easily see when it’s ideal to take action based on the sales performance.
analyzer.plot_data()

#### 5. **Calculating Financial Metrics**
Cumulative Return and Sharpe Ratio are calculated to provide insight into the overall performance of the sales data, with risk adjustments.
metrics = analyzer.calculate_metrics()

# **Installation and Setup**
# 1. Clone the Repository:
git clone https://github.com/ahmedshifathedataengineer/Financial-Data-Analysis.git
cd Financial-Data-Analysis

# 2. Install Dependencies:
Make sure you have Python 3.x installed, then install the required packages:
pip install -r requirements.txt

# 3. Run the Analysis:
Execute the following to perform the analysis:
python main.py

### **Data and Insights**
The dataset used for this project includes:

Name: The company’s name.
Mar Cap - Crore: The market capitalization of the company in crores.
Sales Qtr - Crore: The company’s quarterly sales, also in crores.
Market Cap Category: A classification based on market capitalization (e.g., Large Cap).
Sales Qrt Category: A classification based on quarterly sales performance.
This data is used to perform the analysis and generate the moving averages, RSI, and other indicators.

#### **Example Plot and Output**
Upon running the script, you'll see:

A graph showing the quarterly sales with moving averages and buy/sell signals.
A printed output of the buy/sell signals and RSI values.
Sample Output
Buy/Sell Signals:
                 Signal      Short_MA    Long_MA  Position
Reliance Inds.      1.0    99810.000  99500.000       1.0
TCS                 0.0    65357.000  67000.000       0.0
HDFC Bank           1.0    50431.756  50200.756       1.0
...

### **Visual Output**
The generated plot will show the company's sales data along with the calculated buy and sell signals. You’ll see green triangles for buy signals and red triangles for sell signals.

#### **Financial Metrics**
The project calculates the following key metrics:

**Cumulative Return:** The total return on the company’s sales data over the period analyzed.
**Sharpe Ratio:** A ratio that adjusts return for risk, helping to assess whether the company’s sales growth justifies the risks taken.

#### **Key Takeaways for Finance Professionals**
Identify Trends: Easily track short-term and long-term sales trends to adjust strategies.
Optimize Decisions: Use buy/sell signals to determine the best times to take action based on sales performance.
Manage Risks: By calculating the Sharpe ratio and RSI, you can better understand the risk associated with fluctuating sales.

#### **License**
This project is licensed under the MIT License.


