import streamlit as st
from turtle import st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


final_df = pd.read_csv("C:\\Users\\CHIRAG\\Documents\\Github2\\ML Project\\Files\\processed_daily_data.csv", sep=None, engine="python")


sns.set_style("whitegrid")

sentiment_summary = final_df.groupby('classification').agg(
    avg_net_pnl=('net_pnl', 'mean'),
    avg_win_rate=('win_rate', 'mean'),
    avg_trades=('num_trades', 'mean')
).reset_index()

st.subheader("Average Net PnL by Sentiment")

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=sentiment_summary,
    x='classification',
    y='avg_net_pnl',
    palette='viridis',
    ax=ax
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Average Net PnL")
ax.set_title("Performance Across Sentiment Regimes")

plt.xticks(rotation=30)
st.pyplot(fig)


