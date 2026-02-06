# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, data internal menunjukkan adanya tingkat *dropout* (putus kuliah) yang cukup tinggi. Hal ini menjadi ancaman bagi reputasi institusi dan efisiensi operasional. Oleh karena itu, diperlukan pendekatan berbasis data untuk mendeteksi potensi *dropout* sedini mungkin agar intervensi yang tepat dapat dilakukan.

### Permasalahan Bisnis
Masalah utama yang dihadapi adalah tingginya rasio siswa yang tidak menyelesaikan pendidikan. Secara spesifik, tantangannya adalah:
1.  **Ketidakmampuan mendeteksi dini:** Pihak institusi baru menyadari siswa akan *dropout* ketika siswa tersebut sudah berhenti masuk atau menunggak pembayaran dalam waktu lama, sehingga terlambat untuk diberi bimbingan.
2.  **Kurangnya wawasan faktor penyebab:** Belum adanya pemetaan yang jelas mengenai faktor dominan (apakah finansial, akademik, atau demografis) yang paling mempengaruhi keputusan siswa untuk keluar.

### Cakupan Proyek
Proyek ini mencakup seluruh siklus Data Science (*End-to-End*):
1.  **Data Analysis & Exploration:** Menganalisis dataset historis siswa untuk menemukan pola *churn/dropout*.
2.  **Dashboard Monitoring:** Membuat visualisasi interaktif untuk memantau performa siswa dan faktor risiko.
3.  **Predictive Modeling:** Membangun model Machine Learning untuk memprediksi probabilitas *dropout* siswa.
4.  **Deployment:** Menyediakan aplikasi berbasis web (Streamlit) yang dapat digunakan oleh dosen/staf akademik untuk memeriksa risiko siswa secara *real-time*.

### Persiapan

Sumber data: [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup environment:**

**Untuk Windows:**

```
# Membuat venv
python -m venv venv

# Mengaktifkan venv
venv\Scripts\activate
```

**Untuk macOS / Linux:**

```
# Membuat venv
python3 -m venv venv

# Mengaktifkan venv
source venv/bin/activate
```
**Instalasi Dependensi**
```
pip install -r requirements.txt
```

## Business Dashboard
Dashboard bisnis telah dibuat untuk memudahkan manajemen Jaya Jaya Institut memantau kondisi makro mahasiswa. Dashboard ini memvisualisasikan korelasi antara status kelulusan dengan faktor kunci seperti keterlambatan pembayaran SPP, distribusi nilai akademik, dan usia pendaftar.

**Link Dashboard:** (Akses melalui localhost setelah menjalankan container Docker)

Gambar Preview:  ![Dashboard Preview](Reditya-Dashboard.png)

**Cara Menjalankan Dashboard (Docker):** Untuk mengakses dashboard beserta database yang telah dikonfigurasi, jalankan perintah berikut di terminal:
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

Kredensial Akses Metabase:

URL: http://localhost:3000

Username: root@mail.com

Password: root123

Insight utama dari Dashboard:

- Mahasiswa yang menunggak pembayaran SPP memiliki kecenderungan dropout yang sangat tinggi.

- Efektivitas Beasiswa untuk mahasiswa yang tidak mendapatkannya cenderung tinggi.

- Nilai semester 2 yang dropout hanya mendapatkan di angka 6.

## Menjalankan Sistem Machine Learning
Sistem prediksi risiko dropout telah dikembangkan menggunakan algoritma Random Forest Classifier yang mencapai akurasi ~90%. Sistem ini dikemas dalam bentuk aplikasi web interaktif menggunakan Streamlit.

**Cara Menjalankan Prototype (Lokal)**
Pastikan seluruh dependensi sudah terinstal.

Jalankan perintah berikut di terminal:
```
streamlit run app.py
```

**Akses Prototype (Cloud)**

Aplikasi ini telah di-deploy dan dapat diakses secara online melalui tautan berikut:

**Link Streamlit App:** [MASUKKAN LINK APP STREAMLIT CLOUD ANDA DI SINI]

## Conclusion
Berdasarkan analisis data dan pemodelan yang dilakukan, dapat disimpulkan bahwa:

**Faktor Akademik adalah Indikator Utama:** Variabel ``Curricular units 2nd sem (approved)`` (SKS yang lulus di Semester 2) dan ``Curricular units 2nd sem (grade)`` (Nilai rata-rata Semester 2) adalah fitur yang paling berpengaruh (Top Feature Importance). Mahasiswa yang gagal mengamankan SKS di tahun pertama kuliah memiliki risiko dropout tertinggi.

**Faktor Finansial Sangat Kritis:** Status pembayaran uang kuliah (``Tuition fees up to date``) menjadi penentu kedua. Hampir seluruh mahasiswa yang tidak membayar SPP tepat waktu berakhir dengan status dropout.

**Efektivitas Model:** Model Machine Learning mampu memprediksi status siswa (Lulus/Dropout) dengan akurasi 90%, sehingga layak digunakan sebagai alat bantu pengambilan keputusan.

### Rekomendasi Action Items
Untuk menurunkan angka dropout, direkomendasikan agar Jaya Jaya Institut melakukan langkah-langkah berikut:

1. **Sistem Peringatan Dini Akademik (Academic Early Warning System):** Jangan menunggu hingga akhir tahun ajaran. Gunakan data Semester 1. Jika mahasiswa gagal lulus >50% dari SKS yang diambil, segera jadwalkan sesi konseling wajib/bimbingan akademik intensif.

2. **Program Intervensi Finansial:** Mengingat korelasi kuat antara tunggakan SPP dan dropout, institusi sebaiknya menawarkan skema cicilan pembayaran yang lebih fleksibel atau beasiswa darurat bagi mahasiswa berprestasi yang mengalami kendala ekonomi, sebelum mereka memutuskan untuk berhenti.

3. **Pemanfaatan Aplikasi Prediksi saat Perwalian:** Wajibkan dosen wali untuk menggunakan aplikasi prediksi (prototype yang dibuat) setiap awal semester untuk mengecek profil risiko mahasiswa bimbingannya. Mahasiswa yang terdeteksi "High Risk" harus mendapatkan prioritas pemantauan.
