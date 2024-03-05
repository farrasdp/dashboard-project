import streamlit as st
import numpy as np # for linear algebra
import pandas as pd # for data wrangling
import matplotlib.pyplot as plt #for plotting charts
import seaborn as sns #for visualization and plotting

import warnings
warnings.filterwarnings('ignore')

# Input Data
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/farrasdp/dashboard-project/main/data/bikeSharing.csv")
bikeSharing_df = load_data()

#Processing
datetime_columns = ["dteday"]
for column in datetime_columns:
    bikeSharing_df[column] = pd.to_datetime(bikeSharing_df[column])

category_columns = ["season", "yr", "mnth", "hr", "holiday", "weekday", "workingday"]
for column in category_columns:
    bikeSharing_df[column] = bikeSharing_df[column].astype('category')

min_date = bikeSharing_df["dteday"].min()
max_date = bikeSharing_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

#Buat Judul Dashboard
st.title('Demonstrasi Pengguna Bike Sharing🚲')
st.write("Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic")
st.write("\n")

# Plot Jumlah Pengguna Berdasarkan Bulan
st.subheader('Jumlah Pengguna Berdasarkan Bulan')
by_month_df = bikeSharing_df.groupby(by="mnth").cnt.sum().reset_index()
by_month_df.rename(columns={"cnt": "cnt_sum"}, inplace=True)

colors = ["#72BCD4"]
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="cnt_sum",
    x="mnth",
    data=by_month_df.sort_values(by="cnt_sum", ascending=False),
    palette=colors,
    ax=ax
)
plt.title("Jumlah Pengguna Berdasarkan Bulan", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Plot Jumlah Pengguna Berdasarkan Musim
st.subheader('Jumlah Pengguna Berdasarkan Musim')
by_weathersit_df = bikeSharing_df.groupby(by="weathersit").cnt.sum().reset_index()
by_weathersit_df.rename(columns={"cnt": "cnt_sum"}, inplace=True)

colors = ["#72BCD4"]
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="cnt_sum",
    x="weathersit",
    data=by_weathersit_df.sort_values(by="cnt_sum", ascending=False),
    palette=colors,
    ax=ax
)
plt.title("Jumlah Pengguna Berdasarkan Musim", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)
