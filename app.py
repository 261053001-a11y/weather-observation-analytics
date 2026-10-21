import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Dashboard Pengamatan Cuaca",
    page_icon="🌤️",
    layout="wide"
)

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_cuaca_1000.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    return df

df = load_data()

# 3. Sidebar Filter
st.sidebar.title("🔍 Filter Pengamatan Cuaca")

kota_list = ["Semua"] + list(df['Kota'].unique())
selected_kota = st.sidebar.selectbox("Pilih Kota", kota_list)

kondisi_list = ["Semua"] + list(df['Kondisi'].unique())
selected_kondisi = st.sidebar.selectbox("Pilih Kondisi Cuaca", kondisi_list)

filtered_df = df.copy()

if selected_kota != "Semua":
    filtered_df = filtered_df[filtered_df['Kota'] == selected_kota]

if selected_kondisi != "Semua":
    filtered_df = filtered_df[filtered_df['Kondisi'] == selected_kondisi]

# 4. Header & Identitas
st.title("🌤️ Dashboard Analisis Pengamatan Cuaca")
st.caption("Bedah Kasus 3: Dataset Pengamatan Cuaca (1.000 Data) | Nama: [HUDZAIFAH AINI] - NIM: [261053001]")
st.markdown("---")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

total_obs = len(filtered_df)
avg_suhu = filtered_df['Suhu (°C)'].mean() if total_obs > 0 else 0
avg_kelembaban = filtered_df['Kelembaban (%)'].mean() if total_obs > 0 else 0
total_kota = filtered_df['Kota'].nunique()

col1.metric("Total Pengamatan", f"{total_obs:,} Data")
col2.metric("Rata-Rata Suhu", f"{avg_suhu:.1f} °C")
col3.metric("Rata-Rata Kelembaban", f"{avg_kelembaban:.1f} %")
col4.metric("Jumlah Kota Dipantau", f"{total_kota}")

st.markdown("---")

# 5. Visualisasi Data (Sesuai Karakteristik Tipe Data)
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("🌡️ Distribusi & Sebaran Suhu (°C)")
    st.caption("Numerik (Interval): Box Plot Sebaran Suhu per Kota")
    fig_suhu = px.box(
        filtered_df, 
        x='Kota', 
        y='Suhu (°C)', 
        color='Kota',
        title='Perbandingan Interval Suhu per Kota'
    )
    fig_suhu.update_layout(template='plotly_white')
    st.plotly_chart(fig_suhu, use_container_width=True)

with row1_col2:
    st.subheader("💧 Distribusi Kelembaban Udara (%)")
    st.caption("Numerik (Rasio): Histogram Kelembaban Udara (Nol Absolut)")
    fig_kelembaban = px.histogram(
        filtered_df, 
        x='Kelembaban (%)', 
        nbins=20, 
        color_discrete_sequence=['#3182bd'],
        title='Distribusi Frekuensi Kelembaban Udara'
    )
    fig_kelembaban.update_layout(template='plotly_white')
    st.plotly_chart(fig_kelembaban, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("☁️ Frekuensi Kondisi Cuaca per Kota")
    st.caption("Kategorik (Nominal): Grouped Bar Chart Kondisi Cuaca")
    fig_kondisi = px.histogram(
        filtered_df, 
        x='Kota', 
        color='Kondisi', 
        barmode='group',
        title='Sebaran Kondisi Cuaca Berdasarkan Kota',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_kondisi.update_layout(template='plotly_white')
    st.plotly_chart(fig_kondisi, use_container_width=True)

with row2_col2:
    st.subheader("📈 Hubungan Suhu vs Kelembaban Udara")
    st.caption("Analisis Bivariat Interval vs Rasio")
    fig_scat = px.scatter(
        filtered_df, 
        x='Suhu (°C)', 
        y='Kelembaban (%)', 
        color='Kondisi',
        hover_data=['Kota', 'Tanggal'],
        title='Korelasi Suhu (°C) dan Kelembaban Udara (%)'
    )
    fig_scat.update_layout(template='plotly_white')
    st.plotly_chart(fig_scat, use_container_width=True)

# 6. Tabel Data Interaktif
st.markdown("---")
st.subheader("📄 Raw Data Pengamatan Cuaca")
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Tanggal": st.column_config.DateColumn("Tanggal", format="YYYY-MM-DD"),
        "Kota": st.column_config.TextColumn("Kota"),
        "Suhu (°C)": st.column_config.NumberColumn("Suhu (°C)", format="%.1f °C"),
        "Kelembaban (%)": st.column_config.NumberColumn("Kelembaban (%)", format="%d %%"),
        "Kondisi": st.column_config.TextColumn("Kondisi Cuaca")
    }
)