import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Cardiovascular Disease Analysis", layout="wide")
sns.set(style='dark')

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/cardio_clean.csv")
    corr = pd.read_csv("dataset/correlation.csv")
    age_grp = pd.read_csv("dataset/age_group.csv")
    lstyle = pd.read_csv("dataset/lifestyle.csv")
    
    chol_map = {1: 'Normal', 2: 'Above Normal', 3: 'Well Above Normal'}
    bp_map = {1: 'Normal', 2: 'Pre-Hypertension', 3: 'Hypertension'} 
    gender_map = {1: 'Perempuan', 2: 'Laki-laki'}
    
    df['cholesterol_label'] = df['cholesterol'].map(chol_map)
    df['bp_label'] = df['bp_category'].map(bp_map)
    df['gender_label'] = df['gender'].map(gender_map)
    
    return df, corr, age_grp, lstyle

df, corr_df, age_group_df, lifestyle_df = load_data()

st.sidebar.header("Filter Analisis")
selected_gender = st.sidebar.multiselect(
    "Pilih Jenis Kelamin:",
    options=df["gender_label"].unique(),
    default=df["gender_label"].unique()
)

main_df = df[df["gender_label"].isin(selected_gender)]

st.title("❤️ CardioCare Analysis Dashboard")

if not main_df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Pasien", value=f"{len(main_df):,}")
    with col2:
        avg_age = round(main_df["age"].mean(), 1)
        st.metric("Rata-rata Usia", value=f"{avg_age} Tahun")
    with col3:
        cardio_rate = round((main_df["cardio"].sum() / len(main_df)) * 100, 1)
        st.metric("Prevalensi Penyakit", value=f"{cardio_rate}%")

    st.divider()

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("1. Fitur Klinis Paling Signifikan")
        cardio_corr = corr_df.set_index(corr_df.columns[0])[['cardio']].sort_values(by='cardio', ascending=False)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cardio_corr, annot=True, cmap='Reds', fmt='.2f', ax=ax)
        st.pyplot(fig)

    with col_b:
        st.subheader("2. Distribusi Kolesterol")
        fig, ax = plt.subplots()
        sns.countplot(x='cholesterol_label', hue='cardio', data=main_df, 
                      palette='magma', order=['Normal', 'Above Normal', 'Well Above Normal'], ax=ax)
        ax.set_xlabel("Tingkat Kolesterol")
        st.pyplot(fig)

    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("3. Risiko Berdasarkan Kelompok Usia")
        fig, ax = plt.subplots()
        sns.barplot(x='age_group', y='cardio', data=age_group_df, palette='viridis', ax=ax)
        plt.xticks(rotation=45)
        ax.set_ylabel("Probabilitas Penyakit")
        st.pyplot(fig)

    with col_d:
        st.subheader("4. Pengaruh Gaya Hidup (Unhealthy Score)")
        fig, ax = plt.subplots()
        sns.lineplot(x='unhealthy_score', y='cardio', data=lifestyle_df, marker='o', ax=ax)
        ax.set_xlabel("Skor Gaya Hidup Tidak Sehat")
        ax.set_ylabel("Probabilitas Penyakit")
        st.pyplot(fig)

    st.subheader("5. Kategori Tekanan Darah vs Penyakit Jantung")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(x='bp_label', hue='cardio', data=main_df, 
                  palette='coolwarm', order=['Normal', 'Pre-Hypertension', 'Hypertension'], ax=ax)
    ax.set_xlabel("Kategori Tekanan Darah")
    st.pyplot(fig)

else:
    st.warning("⚠️ Silakan pilih minimal satu jenis kelamin pada filter di samping.")

st.caption("Copyright (c) Team CC26-PSU324 - Capstone Project 2026")
