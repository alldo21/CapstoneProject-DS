# Cardiovascular Disease Analysis Dashboard ❤️

## Deskripsi Proyek
Proyek ini merupakan **Capstone Project** untuk kelas Data Science. Dashboard ini dikembangkan menggunakan **Streamlit** untuk memvisualisasikan hasil eksplorasi dan analisis data dari dataset kesehatan jantung (*Cardiovascular Disease Dataset*). 

Dashboard ini dirancang untuk menjawab beberapa pertanyaan kunci terkait faktor risiko kesehatan:
1. **Ringkasan Metrik**: Menampilkan total pasien yang dianalisis, rata-rata usia, dan persentase prevalensi penyakit kardiovaskular.
2. **Analisis Korelasi**: Menampilkan hubungan antar variabel kesehatan (seperti tekanan darah, kolesterol, dan usia) terhadap status penyakit.
3. **Distribusi Kolesterol**: Visualisasi perbandingan jumlah pasien sehat vs sakit berdasarkan tingkat kolesterol mereka.

## Struktur Direktori
- `/dataset`: Berisi dataset mentah dan bersih berformat `.csv` (termasuk `cardio_clean.csv` dan `correlation.csv`).
- `dashboard.py`: File utama aplikasi Streamlit yang berisi kode visualisasi.
- `Project_Capstone_Fixed.ipynb`: File Jupyter Notebook yang berisi alur pembersihan data, EDA, hingga teknik *feature engineering*.
- `README.md`: Dokumentasi petunjuk informasi dan penggunaan proyek.
- `requirements.txt`: Daftar *Library* Python yang dibutuhkan (Pandas, Matplotlib, Seaborn, Streamlit).
- `Data Dictionary Cardio.xlsx`: Penjelasan detail mengenai definisi setiap kolom dalam dataset.

## Setup Environment
### Menggunakan Anaconda:
1. **Buat Environment baru:**
   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds
   pip install -r requirements.txt
   cd "C:/DICODING CAMP 2026/Project Capstone_DS"
   streamlit run dashboard.py