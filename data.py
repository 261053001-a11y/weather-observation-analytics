import pandas as pd
import numpy as np

# Set seed agar data konsisten
np.random.seed(42)

kotas = ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Makassar', 'Denpasar']
# Format daftar tanggal menjadi string sejak awal
dates = pd.date_range(start='2024-01-01', periods=100, freq='D').strftime('%Y-%m-%d').tolist()

data = []
for i in range(1000):
    kota = np.random.choice(kotas)
    tgl = np.random.choice(dates)
    
    # Suhu (Interval): Bandung lebih sejuk dibanding kota lainnya
    if kota == 'Bandung':
        suhu = round(float(np.random.normal(23.5, 2.5)), 1)
        kelembaban = int(np.clip(np.random.normal(82, 8), 50, 100))
    else:
        suhu = round(float(np.random.normal(31.5, 2.0)), 1)
        kelembaban = int(np.clip(np.random.normal(73, 10), 40, 100))
        
    # Kondisi Cuaca (Nominal) berkorelasi dengan Kelembaban
    if kelembaban > 85:
        kondisi = np.random.choice(['Hujan Ringan', 'Hujan Lebat'], p=[0.6, 0.4])
    elif kelembaban > 70:
        kondisi = np.random.choice(['Berawan', 'Hujan Ringan'], p=[0.7, 0.3])
    else:
        kondisi = np.random.choice(['Cerah', 'Berawan'], p=[0.8, 0.2])
        
    data.append({
        'Tanggal': tgl,
        'Kota': kota,
        'Suhu (°C)': suhu,
        'Kelembaban (%)': kelembaban,
        'Kondisi': kondisi
    })

df = pd.DataFrame(data)
df.to_csv('dataset_cuaca_1000.csv', index=False)
print("Data sintesis 1.000 pengamatan cuaca berhasil dibuat!")