import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')

def aggregate_hourly_rentals(hourly_data):
    return hourly_data.groupby("hours")["cnt"].sum().reset_index()

def filter_data_by_yearly_range(daily_data, start_year="2011-01-01", end_year="2012-12-31"):
    return daily_data.query(f'dteday >= "{start_year}" and dteday < "{end_year}"')

def calculate_total_registered_users(daily_data):
    return daily_data.groupby("dteday")["registered"].sum().reset_index().rename(columns={"registered": "total_registered"})

def calculate_total_casual_users(daily_data):
    return daily_data.groupby("dteday")["casual"].sum().reset_index().rename(columns={"casual": "total_casual"})

def summarize_rental_by_season(daily_data):
    return daily_data.groupby("season")["cnt"].sum().reset_index()

def summarize_rental_by_hour(hourly_data):
    return hourly_data.groupby("hours")["cnt"].sum().sort_values(ascending=False).reset_index()

daily_data = pd.read_csv("day_cleaned.csv")
hourly_data = pd.read_csv("hour_cleaned.csv")

date_columns = ["dteday"]
for column in date_columns:
    daily_data[column] = pd.to_datetime(daily_data[column])
    hourly_data[column] = pd.to_datetime(hourly_data[column])

min_date = daily_data["dteday"].min()
max_date = daily_data["dteday"].max()

with st.sidebar:
    st.image("gambar.jpg")
    selected_start_date, selected_end_date = st.date_input(
        "Pilih Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

filtered_daily_data = daily_data[(daily_data["dteday"] >= str(selected_start_date)) &
                                 (daily_data["dteday"] <= str(selected_end_date))]
filtered_hourly_data = hourly_data[(hourly_data["dteday"] >= str(selected_start_date)) &
                                   (hourly_data["dteday"] <= str(selected_end_date))]

daily_rentals = filter_data_by_yearly_range(filtered_daily_data)
registered_users = calculate_total_registered_users(filtered_daily_data)
casual_users = calculate_total_casual_users(filtered_daily_data)
hourly_rentals = summarize_rental_by_hour(filtered_hourly_data)
seasonal_rentals = summarize_rental_by_season(filtered_daily_data)

st.header('Bike Rental Dashboard 🚴‍♂️')
st.subheader('Statistik Performa Penyewaan Sepeda')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rental", value=daily_rentals["cnt"].sum())
with col2:
    st.metric("Pengguna Terdaftar", value=registered_users["total_registered"].sum())
with col3:
    st.metric("Pengguna Kasual", value=casual_users["total_casual"].sum())

st.subheader("Jam dengan Sewa Terbanyak dan Terdikit")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(x="hours", y="cnt", data=hourly_rentals.head(5), palette=["#90CAF9" if i == 2 else "#D3D3D3" for i in range(5)], ax=ax[0])
ax[0].set_title("Jam dengan Sewa Terbanyak", fontsize=30)

sns.barplot(x="hours", y="cnt", data=hourly_rentals.sort_values(by="hours").head(5), palette=["#D3D3D3" if i < 4 else "#90CAF9" for i in range(5)], ax=ax[1])
ax[1].set_title("Jam dengan Sewa Terdikit", fontsize=30)
ax[1].invert_xaxis()

st.pyplot(fig)

st.subheader("Performa Penyewaan Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x="season", y="cnt", data=seasonal_rentals.sort_values(by="season", ascending=False), palette=["#90CAF9" if i == 3 else "#D3D3D3" for i in range(4)], ax=ax)
ax.set_title("Penyewaan Berdasarkan Musim", fontsize=50)
st.pyplot(fig)

st.subheader("Performa Penyewaan Dalam Beberapa Tahun Terakhir")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_data["dteday"], daily_data["cnt"], marker='o', linewidth=2, color="#90CAF9")
st.pyplot(fig)

