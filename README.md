# Sales Data Analysis Project

This project analyzes sales data using Python, Pandas, and Matplotlib. It explores total sales by product, region, and date, and presents the insights through visualizations.

## 📁 Files

- `sales_data.csv` : The sample dataset containing sales records.
- `sales_analysis.ipynb` : Jupyter Notebook with code to load, process, and visualize the sales data.

## 📊 Dataset Overview

The CSV file contains the following columns:
- **Date** : Sale date (in DD-MM-YYYY format)
- **Product** : Item sold (e.g., Laptop, Tablet, etc.)
- **Region** : Sales region (e.g., North, South, etc.)
- **Sales** : Amount of sales (in currency units)

## 🧪 Analysis Performed

1. **Load Data**: Using `pandas.read_csv()`
2. **Data Cleaning**: Convert `Date` column to datetime using `pd.to_datetime(..., dayfirst=True)`
3. **Group & Summarize**:
   - Total sales by **Product** using `groupby()` and `sum()`
   - Daily total sales by **Date**
   - Total sales by **Region**
4. **Visualization**: Using `Matplotlib`
   - Bar Chart for Product-wise Sales
   - Line Chart for Daily Sales Trend
   - Pie Chart for Region-wise Sales Distribution

## 📈 Libraries Used

- `pandas`
- `matplotlib.pyplot`

## 🚀 How to Run

1. Open the notebook `sales_analysis.ipynb` in Jupyter.
2. Make sure `sales_data.csv` is in the same folder.
3. Run all cells to see the analysis and charts.

## ✅ Output

- Bar chart of total sales by product
- Line graph of daily sales trend
- Pie chart showing sales distribution by region

## 📌 Notes

- Ensure your system has Python, Jupyter Notebook, Pandas, and Matplotlib installed.
- If date parsing errors occur, verify the date format in your CSV and use `dayfirst=True`.

