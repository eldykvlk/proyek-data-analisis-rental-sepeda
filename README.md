# **Submission Dicoding: Analisis Data dengan Python**

## **Tampilan Dashboard**
![Dashboard Preview](https://raw.githubusercontent.com/eldykvlk/proyek-data-analisis-rental-sepeda/refs/heads/master/Preview_dashboard.PNG)

## **Ringkasan Proyek**
Proyek ini berfokus pada analisis data dari **Bike Sharing Dataset** dengan tujuan menganalisis data dan menginterpretasikan performa yang terkandung di dalamnya. Hasil dari analisis ini divisualisasikan dalam bentuk dashboard interaktif.

## **Struktur Proyek**
- **`/data`**: Folder ini berisi dataset mentah dalam format `.csv` yang digunakan sebagai sumber utama analisis.
- **`/dashboard`**: Berisi file utama `main.py` yang digunakan untuk membangun dashboard berbasis **Streamlit**.
- **`notebook.ipynb`**: Notebook yang digunakan untuk eksplorasi data, pembersihan, dan analisis lebih lanjut.

## **Langkah Instalasi**

1. **Kloning repositori ini ke komputer lokal Anda**
   
   ```sh
   git clone https://github.com/eldykvlk/proyek-data-analisis-rental-sepeda.git
   ```

2. **Pastikan Python dan pustaka yang diperlukan telah terinstal**
   
   Anda dapat menginstalnya dengan menjalankan perintah berikut:
   
   ```sh
   pip install -r requirements.txt
   ```
   Jika pustaka **Streamlit** belum tersedia, instal dengan:
   
   ```sh
   pip install streamlit
   ```

## **Menjalankan Dashboard**

1. **Akses direktori proyek**
   
   ```sh
   cd proyek-data-analisis-rental-sepeda/dashboard/
   ```

2. **Jalankan Streamlit untuk menampilkan dashboard**
   
   ```sh
   streamlit run dashboard.py
   ```
   
Setelah perintah ini dieksekusi, dashboard interaktif akan muncul di browser, menampilkan hasil analisis secara visual.

---

Dengan proyek ini, diharapkan pengguna dapat memahami pola penggunaan layanan penyewaan sepeda berdasarkan berbagai variabel dalam dataset. Selamat mencoba! 🚴‍♂️📊

