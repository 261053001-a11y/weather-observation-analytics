# 🌤️ Dashboard Analisis Pengamatan Cuaca
Link Demo : 

> **Bedah Kasus 3: Dataset Pengamatan Cuaca (1.000 Data)**  
> **Nama:** Hudzaifah Aini  
> **NIM:** 261053001  

Aplikasi *Dashboard* interaktif berbasis web yang dibangun menggunakan **Streamlit**, **Pandas**, dan **Plotly** untuk memvisualisasikan serta menganalisis data pengamatan cuaca dari 1.000 data sintetis berbagai kota di Indonesia.

---

## 🚀 Fitur Utama Dashboard
1. **Filter Data Interaktif (Sidebar):**
   - Filter berdasarkan **Kota** (Jakarta, Bandung, Surabaya, Medan, Makassar, Denpasar).
   - Filter berdasarkan **Kondisi Cuaca** (Cerah, Berawan, Hujan Ringan, Hujan Lebat).
2. **Metrik KPI Utama:**
   - Total Pengamatan Data
   - Rata-Rata Suhu (°C)
   - Rata-Rata Kelembaban (%)
   - Jumlah Kota yang Dipantau
3. **Visualisasi Data Interaktif (Plotly):**
   - 🌡️ **Box Plot Suhu (°C)** (*Sebaran interval suhu per kota*).
   - 💧 **Histogram Kelembaban Udara (%)** (*Distribusi rasio kelembaban udara*).
   - ☁️ **Grouped Bar Chart Kondisi Cuaca** (*Frekuensi kondisi cuaca berdasarkan kota*).
   - 📈 **Scatter Plot Korelasi** (*Hubungan bivariat antara Suhu dan Kelembaban Udara*).
4. **Tabel Data Mentah (*Raw Data Table*):** Menampilkan detail data pengamatan cuaca lengkap dengan pemformatan kolom khusus.

---

## 📁 Struktur File Repository
- `app.py`: File utama untuk menjalankan antarmuka dashboard Streamlit.
- `data.py`: Skrip Python untuk menghasilkan data sintesis `dataset_cuaca_1000.csv` secara otomatis.
- `dataset_cuaca_1000.csv`: Berkas data pengamatan cuaca (1.000 baris).
- `requirements.txt`: Daftar dependencies/pustaka Python yang dibutuhkan.

---

## 🛠️ Cara Menjalankan Project

1. **Clone repository ini atau unduh file project.**
2. **Install semua dependencies:**
   ```bash
   pip install -r requirements.txt
