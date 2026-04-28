import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Cardiovascular Dashboard", layout="wide")
sns.set(style='dark')

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/cardio_clean.csv")
    return df

df = load_data()

st.title("Analisis Penyakit Kardiovaskular ❤️")
st.markdown("Dashboard ini menampilkan insight dari dataset kesehatan jantung untuk Project Capstone.")

st.sidebar.header("Filter Data")

gender_options = df["gender"].unique()
selected_gender = st.sidebar.multiselect(
    "Pilih Jenis Kelamin:", 
    options=gender_options, 
    default=gender_options
)

filtered_df = df[df["gender"].isin(selected_gender)]

if not filtered_df.empty:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Pasien", value=len(filtered_df))
    
    with col2:
        avg_age = round(filtered_df["age"].mean() / 365, 1)
        st.metric("Rata-rata Usia", value=f"{avg_age} Tahun")
    
    with col3:
        cardio_rate = round((filtered_df["cardio"].sum() / len(filtered_df)) * 100, 1)
        st.metric("Prevalensi Penyakit", value=f"{cardio_rate}%")

    st.divider()

    st.subheader("Tabel Korelasi Variabel")
    try:
        corr_df = pd.read_csv("dataset/correlation.csv")
        st.dataframe(corr_df)
    except:
        st.error("File dataset/correlation.csv tidak ditemukan.")

    st.subheader("Distribusi Kolesterol terhadap Status Kardiovaskular")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.countplot(x='cholesterol', hue='cardio', data=filtered_df, palette="magma", ax=ax)
    
    # Memberi label
    ax.set_xlabel("Tingkat Kolesterol (1: Normal, 2: Diatas Normal, 3: Jauh Diatas Normal)")
    ax.set_ylabel("Jumlah Pasien")
    
    st.pyplot(fig)

else:
    st.warning("⚠️ Silakan pilih minimal satu jenis kelamin pada filter di samping untuk melihat hasil analisis.")

st.caption("Copyright (c) Team CC26-PSU324 - Capstone Project 2026")