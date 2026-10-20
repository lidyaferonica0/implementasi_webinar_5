
# Webinar 5 — Human-Computer Interaction & Data Visualization

## Studi Kasus
**Analisis Keluhan Fasilitas Kampus Menggunakan Visualisasi Data**

## 1. Deskripsi Proyek

Program ini merupakan implementasi studi kasus dari materi Webinar 5 tentang *Human-Computer Interaction (HCI)* dan visualisasi data.

Studi kasus berfokus pada analisis keluhan fasilitas kampus, seperti Wi-Fi, kebersihan, toilet, AC, proyektor, dan kursi atau meja. Data diolah untuk membantu pengelola memahami kategori keluhan, lokasi yang perlu diperhatikan, status penanganan, serta waktu penyelesaian keluhan.

Program dijalankan langsung melalui terminal Python tanpa menggunakan Streamlit atau browser.

**Catatan:** Dataset yang digunakan merupakan data sintetis untuk demonstrasi pembelajaran, bukan data keluhan kampus yang sebenarnya.

## 2. Tujuan Program

- Mengolah dan menganalisis data keluhan fasilitas kampus.
- Menampilkan ringkasan informasi agar lebih mudah dipahami.
- Membuat visualisasi untuk membandingkan kategori keluhan dan melihat tren bulanan.
- Menganalisis status keluhan berdasarkan lokasi dan waktu penyelesaian berdasarkan prioritas.
- Mendemonstrasikan konsep HCI dan visualisasi data dalam mendukung pengambilan keputusan.

## 3. Konsep Materi yang Diterapkan

### a. Human-Computer Interaction (HCI)

Penyajian hasil analisis dirancang agar informasi lebih mudah dibaca dan dipahami oleh pengguna.

### b. User-Centered Design (UCD)

Informasi yang ditampilkan berfokus pada kebutuhan pengelola kampus, seperti kategori keluhan terbanyak dan lokasi yang perlu ditinjau.

### c. Cognitive Load

Ringkasan angka, tabel, dan grafik membantu pengguna memahami pola data tanpa harus membaca seluruh data mentah satu per satu.

### d. Visual Perception

Grafik batang digunakan untuk membandingkan jumlah keluhan, sedangkan grafik garis digunakan untuk melihat perubahan jumlah keluhan dari bulan ke bulan.

### e. Analisis Kebutuhan Pengguna

Informasi yang dianalisis meliputi kategori fasilitas, lokasi, prioritas, status keluhan, waktu penyelesaian, dan kepuasan pelapor.

### f. Dashboard dan Visualisasi Data

Program menerapkan tiga tahapan penyajian informasi yang dikenal sebagai mantra Shneiderman:

1. **Overview:** menampilkan ringkasan keseluruhan data.
2. **Zoom and Filter:** menyaring data berdasarkan kategori dan lokasi tertentu.
3. **Details-on-Demand:** menampilkan contoh rincian keluhan dan menyimpan data hasil penyaringan.

Penerapan ini berupa simulasi analisis dan visualisasi, bukan dashboard grafis interaktif.

## 4. Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **NumPy** — menghasilkan data numerik dan nilai simulasi.
- **Pandas** — mengolah, mengelompokkan, dan menganalisis data.
- **Matplotlib** — membuat grafik visualisasi data.

## 5. Struktur Folder

Struktur folder awal proyek:

```text
webinar_5/
├── webinar_5.py
├── README.md
└── requirements.txt
```

Setelah program dijalankan, folder `output/` akan dibuat secara otomatis:

```text
webinar_5/
├── webinar_5.py
├── README.md
├── requirements.txt
└── output/
    ├── data_keluhan_kampus.csv
    ├── ringkasan_keluhan.csv
    ├── tren_keluhan_bulanan.csv
    ├── detail_filter_keluhan.csv
    ├── 01_keluhan_per_kategori.png
    ├── 02_tren_keluhan_bulanan.png
    ├── 03_status_keluhan_per_lokasi.png
    └── 04_waktu_penyelesaian_prioritas.png
```

## 6. Persyaratan Sistem

- Python 3.9 atau versi yang lebih baru.
- pip untuk menginstal pustaka Python.
- Terminal atau Command Prompt.
- Pustaka NumPy, Pandas, dan Matplotlib.

## 7. Cara Instalasi dan Menjalankan Program

### Langkah 1 — Buka folder proyek

Buka terminal atau Command Prompt pada folder `webinar_5`.

### Langkah 2 — Instal dependensi

Jalankan perintah:

```bash
pip install -r requirements.txt
```

### Langkah 3 — Jalankan program

Jalankan perintah:

```bash
python webinar_5.py
```

Program akan membuat dataset sintetis, melakukan analisis, menyimpan hasil visualisasi, dan menampilkan laporan ringkas langsung di terminal.

Tidak diperlukan perintah `streamlit run` atau akses melalui browser.

## 8. Penjelasan Hasil Program

### a. `data_keluhan_kampus.csv`

Berisi data utama keluhan, meliputi ID keluhan, tanggal, kategori, lokasi, prioritas, status, waktu penyelesaian, dan kepuasan pelapor.

### b. `ringkasan_keluhan.csv`

Berisi indikator utama, seperti total keluhan, jumlah keluhan selesai dan belum selesai, rata-rata waktu penyelesaian, rata-rata kepuasan, serta kategori dan lokasi dengan jumlah keluhan terbanyak.

### c. `tren_keluhan_bulanan.csv`

Berisi jumlah keluhan yang tercatat setiap bulan.

### d. `detail_filter_keluhan.csv`

Berisi rincian keluhan yang sesuai dengan simulasi penyaringan berdasarkan kategori atau lokasi dengan jumlah keluhan terbanyak.

### e. `01_keluhan_per_kategori.png`

Grafik batang untuk membandingkan jumlah keluhan pada setiap kategori fasilitas.

### f. `02_tren_keluhan_bulanan.png`

Grafik garis untuk melihat perubahan jumlah keluhan selama periode pengamatan simulasi.

### g. `03_status_keluhan_per_lokasi.png`

Grafik batang untuk membandingkan status keluhan di berbagai lokasi kampus.

### h. `04_waktu_penyelesaian_prioritas.png`

Grafik untuk membandingkan rata-rata waktu penyelesaian keluhan berdasarkan tingkat prioritas.

## 9. Kesimpulan

Program ini menunjukkan bagaimana konsep HCI dan visualisasi data dapat diterapkan untuk menyajikan informasi secara lebih terstruktur dan mudah dipahami. Ringkasan dan grafik membantu mengidentifikasi pola keluhan, sedangkan penyaringan data memudahkan pemeriksaan informasi tertentu.
