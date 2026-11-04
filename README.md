Trade Sentiment vs Trader Behavior Analysis
Project Overview

This project analyzes how Bitcoin market sentiment (Fear & Greed Index) influences trader behavior and performance on Hyperliquid.

The objective is to uncover patterns between sentiment regimes and trading activity, profitability, and positioning bias — and propose actionable strategy insights.

📂 Repository Structure
📁 Trading Sentiment Analysis
│
├── Trading_Sentiment_Analysis.ipynb   # Full analysis notebook
├── app.py                             # Streamlit dashboard
├── fear_greed_index.csv               # Sentiment dataset
├── processed_daily_data.csv           # Cleaned & merged dataset
├── Project_Report.pdf                 # Final written report
├── Presentation.pptx                  # Summary presentation
└── README.md


(Note: Historical trade dataset excluded due to size limits.)

Datasets Used
1] Bitcoin Market Sentiment (Fear & Greed Index)

Date

Sentiment value

Sentiment classification (Fear, Greed, Extreme Fear, etc.)

2️] Historical Trader Data (Hyperliquid)

Execution price, Size, Direction, Closed PnL, Fees, Timestamp, Account

Methodology
Part A — Data Preparation

Cleaned and validated datasets (no missing or duplicate values)

Converted timestamps to daily level

Merged sentiment and trading data

Created daily metrics:

Net PnL

Win rate

Number of trades

Bullish vs Bearish ratio

Part B — Analysis
🔹 Performance by Sentiment

Highest profitability observed during Fear regimes

Extreme Greed showed lower overall profitability

🔹 Behavioral Changes

Traders showed bullish bias during Fear

Bearish bias increased during Greed

Indicates contrarian positioning behavior

🔹 Correlation Insights

Moderate positive relationship between trade frequency and profitability (0.35)

Weak direct correlation between sentiment value and net PnL

Volatility and activity play stronger roles than sentiment alone

Bonus — Predictive Modeling

A Logistic Regression model was built to predict next-day profitability using:

Sentiment value

Trade frequency

Win rate

Previous day net PnL

After addressing class imbalance:

Model accuracy: 77%

Strong prediction of profitable days

Limited detection of rare loss days

Bonus — Trader Clustering

KMeans clustering identified 3 behavioral archetypes:

High-frequency aggressive traders

Conservative low-activity traders

Consistent moderate performers

This segmentation highlights distinct behavioral patterns across accounts.

Dashboard

A lightweight Streamlit dashboard was developed to visualize:

Sentiment vs profitability

Win rate trends

Behavioral trade bias

Cluster segmentation

To run locally:

pip install -r requirements.txt
streamlit run app.py

How to Run the Notebook

Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn streamlit


Open:

Trading_Sentiment_Analysis.ipynb


Run all cells sequentially.

Key Insights

Fear regimes create higher volatility and stronger profit opportunities.

Traders increase bullish exposure during panic conditions.

Trade activity is moderately linked to profitability.

Behavioral clustering reveals distinct trader archetypes.

Strategy Recommendations

Increase exposure during Fear regimes.

Reduce leverage and aggression during Extreme Greed.

Adjust position sizing based on activity and volatility levels.

Skills Demonstrated

Data Cleaning & Transformation

Feature Engineering

Time-Series Alignment

Behavioral Analysis

Machine Learning (Logistic Regression)

Unsupervised Learning (KMeans)

Dashboard Development (Streamlit)

Author

Chirag S
Artificial Intelligence & Data Science
