import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk membuat data pertanyaan 1
def create_data_pertanyaan1_df(df):
    df['month_year'] = df['datetime'].dt.to_period('M')
    data_pertanyaan1_df = df.groupby('month_year').agg({
        'PM2.5': 'mean',
        'RAIN': 'mean'
    }).reset_index()
    data_pertanyaan1_df['month_year'] = data_pertanyaan1_df['month_year'].dt.strftime('%B-%Y')
    return data_pertanyaan1_df

# Fungsi untuk membuat data pertanyaan 2
def create_data_pertanyaan2_df(df):
    data_pertanyaan2_df = df.groupby('hour').agg({
        'PM2.5': 'mean',
        'TEMP': 'mean',
        'WSPM': 'mean'
    }).reset_index()
    return data_pertanyaan2_df

# Membaca file CSV
data_clean_df = pd.read_csv("data_clean_df.csv")
data_clean_df['datetime'] = pd.to_datetime(data_clean_df['datetime'])

# Judul dan informasi dashboard
st.title('Proyek Analisis Data - Air Quality Dataset')
st.write("Nama : Muhammad Rakha Almasah")
st.write("Email : muh.rakha.al@gmail.com")
st.write("ID Dicoding : muhrakhaal")

# Membuat data untuk pertanyaan 1 dan 2
data_pertanyaan1_df = create_data_pertanyaan1_df(data_clean_df)
data_pertanyaan2_df = create_data_pertanyaan2_df(data_clean_df)

# Pertanyaan 1
st.subheader('Pertanyaan 1 : Bagaimana pengaruh rata-rata (per bulan) variasi konsentrasi PM 2.5 dengan curah hujan di Kota Wanshouxigong selama periode April 2015 hingga April 2016 ?')

# Plot PM2.5 dan curah hujan
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data_pertanyaan1_df['month_year'], data_pertanyaan1_df['PM2.5'], color='blue', marker='o', label='PM2.5')
ax1.set_ylabel('PM2.5 (ug/m3)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax2 = ax1.twinx()
ax2.plot(data_pertanyaan1_df['month_year'], data_pertanyaan1_df['RAIN'], color='red', linestyle='--', marker='o', label='Rainfall')
ax2.set_ylabel('Rainfall (mm/month)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Monthly Average PM2.5 and Rainfall in Wanshouxigong (Apr 2015 - Apr 2016)', fontweight='bold', pad=20)
for tick in ax1.get_xticklabels():
    tick.set_rotation(45)
    tick.set_ha('right')
fig1.tight_layout()

st.pyplot(fig1)

# Jawaban Pertanyaan 1
st.write("")
st.write("### Jawaban Pertanyaan 1")
st.write("Dari hasil visualisasi tersebut, terlihat bahwa variasi konsentrasi PM2.5 dan curah hujan bulanan di Wanshouxigong memiliki hubungan yang cenderung berbanding terbalik. Ketika curah hujan meningkat, seperti yang terjadi pada bulan Juli 2015, konsentrasi PM2.5 justru mengalami penurunan yang signifikan. Hal ini mengindikasikan bahwa curah hujan dapat membantu menurunkan konsentrasi PM2.5 di udara, kemungkinan karena partikel-partikel polutan terbawa turun oleh hujan.")
st.write("Sebaliknya, pada bulan Desember 2015, ketika curah hujan berada pada titik rendah, konsentrasi PM2.5 justru mencapai puncaknya. Ini menunjukkan bahwa ketika curah hujan rendah, tidak ada mekanisme alam yang efektif untuk membersihkan partikel polusi dari udara, sehingga konsentrasi PM2.5 meningkat.")
st.write("Secara keseluruhan, data ini menjawab pertanyaan bahwa ada pengaruh signifikan antara variasi bulanan curah hujan terhadap konsentrasi PM2.5 di kota Wanshouxigong selama periode April 2015 hingga April 2016. Korelasi ini menunjukkan bahwa curah hujan yang lebih tinggi cenderung mengurangi polusi udara, sedangkan pada bulan-bulan dengan curah hujan rendah, polusi udara semakin parah.")

# Pertanyaan 2
st.subheader('Pertanyaan 2 : Bagaimana pengaruh rata-rata (per jam) variasi konsentrasi PM 2.5 dengan kondisi meteorologi (suhu dan kecepatan angin) di Kota Wanshouxigong selama periode April 2015 hingga April 2016 ?')

# Plot PM2.5 dan Suhu
fig2, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data_pertanyaan2_df['hour'], data_pertanyaan2_df['PM2.5'], color='blue', marker='o', label='PM2.5')
ax1.set_xlabel('Hour of the Day', fontsize=12)
ax1.set_ylabel('PM2.5 (ug/m3)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(range(24))
ax1.set_xticklabels(range(24))
ax2 = ax1.twinx()
ax2.plot(data_pertanyaan2_df['hour'], data_pertanyaan2_df['TEMP'], color='red', linestyle='--', marker='o', label='TEMP')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Hourly Average PM2.5 and Temperature in Wanshouxigong (Apr 2015 - Apr 2016)', fontweight='bold')
fig2.tight_layout()

st.pyplot(fig2)

# Jawaban Pertanyaan 2 (PM2.5 dan Suhu)
st.write("")
st.write("### Jawaban Pertanyaan 2 (PM2.5 dan Suhu)")
st.write("Dari hasil visualisasi PM 2.5 dengan temperatur, terlihat adanya hubungan terbalik antara konsentrasi PM2.5 dan temperatur sepanjang hari. Grafik memperlihatkan bahwa konsentrasi PM2.5 cenderung lebih tinggi pada malam hingga dini hari, kemudian menurun pada siang hari ketika suhu meningkat. Tren ini sejalan dengan beberapa penelitian sebelumnya yang menunjukkan bahwa peningkatan konsentrasi PM2.5 sering terjadi pada waktu-waktu dengan suhu rendah dan kelembaban tinggi, serta penurunan konsentrasi PM2.5 ketika suhu naik dan kelembaban menurun.")

# Plot PM2.5 dan kecepatan angin
fig3, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data_pertanyaan2_df['hour'], data_pertanyaan2_df['PM2.5'], color='blue', marker='o', label='PM2.5')
ax1.set_xlabel('Hour of the Day', fontsize=12)
ax1.set_ylabel('PM2.5 (ug/m3)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(range(24))
ax1.set_xticklabels(range(24))
ax2 = ax1.twinx()
ax2.plot(data_pertanyaan2_df['hour'], data_pertanyaan2_df['WSPM'], color='red', linestyle='--', marker='o', label='WSPM')
ax2.set_ylabel('Wind Speed (m/s)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Hourly Average PM2.5 and Wind Speed in Wanshouxigong (Apr 2015 - Apr 2016)', fontweight='bold')
fig3.tight_layout()

st.pyplot(fig3)

# Jawaban Pertanyaan 2 (PM2.5 dan kecepatan angin)
st.write("")
st.write("### Jawaban Pertanyaan 2 (PM2.5 dan Kecepatan Angin)")
st.write("Selain itu, dari hasil visualisasi PM2.5 dengan kecepatan angin menunjukkan hubungan antara rata-rata konsentrasi PM2.5 dan kecepatan angin pada berbagai jam dalam sehari. Ketika kecepatan angin meningkat, konsentrasi PM2.5 cenderung menurun, dan sebaliknya. Pola ini mengindikasikan bahwa kecepatan angin mempengaruhi penyebaran dan pengenceran partikulat PM2.5 di atmosfer.")


# Kesimpulan
st.subheader("Kesimpulan")
st.write("Variasi curah hujan bulanan memiliki pengaruh yang signifikan terhadap konsentrasi PM2.5 di Wanshouxigong selama periode April 2015 hingga April 2016. Ketika curah hujan meningkat, terutama pada bulan-bulan dengan intensitas hujan tinggi seperti Juli 2015, konsentrasi PM2.5 cenderung menurun, kemungkinan karena partikel polutan terbawa turun oleh hujan. Sebaliknya, pada bulan-bulan dengan curah hujan rendah, seperti Desember 2015, konsentrasi PM2.5 meningkat. Ini menunjukkan bahwa curah hujan berperan penting dalam menurunkan polusi udara, dan pada periode dengan curah hujan rendah, risiko peningkatan polusi udara lebih tinggi.")
st.write("Kondisi meteorologi seperti suhu dan kecepatan angin juga mempengaruhi konsentrasi PM2.5 di Wanshouxigong selama periode April 2015 hingga April 2016. Pada malam hari ketika suhu lebih rendah, konsentrasi PM2.5 cenderung tinggi, sedangkan pada siang hari ketika suhu meningkat, konsentrasi PM2.5 menurun. Selain itu, kecepatan angin yang tinggi berkontribusi dalam mengencerkan partikel polutan, sehingga konsentrasi PM2.5 menurun saat angin bertiup lebih kencang. Sebaliknya, saat kecepatan angin rendah, terutama pada malam hingga dini hari, konsentrasi PM2.5 meningkat karena terbatasnya dispersi polutan di atmosfer.")

st.write("")
st.write("© 2024 Muhammad Rakha Almasah. All rights reserved.")