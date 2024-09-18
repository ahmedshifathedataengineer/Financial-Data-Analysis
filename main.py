from financial_analyzer_module import FinancialAnalyzer
import pandas as pd

# Main script
if __name__ == "__main__":
    # Load your actual data from the provided file path
    data_path = r'C:\Users\hurri\OneDrive\Desktop\Financial Data Analysis and Signal Processing\Financial-Analytics-data1.csv'
    
    try:
        # Read the CSV into a DataFrame
        data = pd.read_csv(data_path)
        print(f"Data loaded successfully from {data_path}")
        print("Columns in the data:", data.columns)
    except FileNotFoundError:
        print(f"Error: File not found at {data_path}")
        data = None

    # Ensure column names have no leading/trailing spaces
    if data is not None:
        data.columns = data.columns.str.strip()

    # Check if the column exists and proceed
    if data is not None and 'Sales Qtr - Crore' in data.columns:
        analyzer = FinancialAnalyzer(data)
        
        # Step 1: Calculate moving averages
        analyzer.calculate_moving_averages(short_window=40, long_window=100)
        
        # Step 2: Identify buy/sell signals
        signals = analyzer.identify_buy_sell_signals()
        print("Buy/Sell Signals:")
        print(signals)
        
        # Step 3: Calculate RSI
        rsi = analyzer.calculate_rsi(window=14)
        print("\nRSI Values:")
        print(rsi)
        
        # Step 4: Plot the data
        print("\nPlotting data...")
        analyzer.plot_data(short_window=40, long_window=100)
        
        # Step 5: Calculate financial metrics
        metrics = analyzer.calculate_metrics()
        print("\nFinancial Metrics:")
        print(metrics)

    else:
        print("The 'Sales Qtr - Crore' column is missing. Please check the dataset.")
