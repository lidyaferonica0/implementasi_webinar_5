from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. KONFIGURASI PROGRAM

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

JUMLAH_DATA = 180
RANDOM_SEED = 42

# 2. MEMBUAT DATA KELUHAN FASILITAS KAMPUS

def buat_dataset():
    """Membuat data sintetis keluhan fasilitas kampus."""

    rng = np.random.default_rng(RANDOM_SEED)

    kategori = [
        "Wi-Fi",
        "Kebersihan",
        "Toilet",
        "AC",
        "Proyektor",
        "Kursi/Meja"
    ]

    lokasi = [
        "Gedung A",
        "Gedung B",
        "Gedung C",
        "Perpustakaan",
        "Laboratorium"
    ]

    prioritas = ["Rendah", "Sedang", "Tinggi"]
    status = ["Selesai", "Diproses", "Menunggu"]

    tanggal_tersedia = pd.date_range(
        start="2026-01-01",
        end="2026-06-30",
        freq="D"
    )

    data = pd.DataFrame({
        "ID_Keluhan": [
            f"KLH-{i:03d}"
            for i in range(1, JUMLAH_DATA + 1)
        ],
        "Tanggal": rng.choice(
            tanggal_tersedia,
            size=JUMLAH_DATA
        ),
        "Kategori": rng.choice(
            kategori,
            size=JUMLAH_DATA,
            p=[0.24, 0.18, 0.17, 0.16, 0.14, 0.11]
        ),
        "Lokasi": rng.choice(
            lokasi,
            size=JUMLAH_DATA
        ),
        "Prioritas": rng.choice(
            prioritas,
            size=JUMLAH_DATA,
            p=[0.28, 0.47, 0.25]
        ),
        "Status": rng.choice(
            status,
            size=JUMLAH_DATA,
            p=[0.62, 0.25, 0.13]
        )
    })

    # Waktu penyelesaian disesuaikan dengan tingkat prioritas.
    waktu_penyelesaian = []

    for tingkat in data["Prioritas"]:
        if tingkat == "Rendah":
            waktu = rng.uniform(1, 18)
        elif tingkat == "Sedang":
            waktu = rng.uniform(4, 36)
        else:
            waktu = rng.uniform(8, 60)

        waktu_penyelesaian.append(round(waktu, 1))

    data["Waktu_Penyelesaian_Jam"] = waktu_penyelesaian

    # Skor kepuasan menggunakan skala 1 sampai 5.
    data["Kepuasan_Pelapor"] = np.clip(
        np.rint(rng.normal(4.0, 0.8, JUMLAH_DATA)),
        1,
        5
    ).astype(int)

    data["Tanggal"] = pd.to_datetime(data["Tanggal"])

    data = data.sort_values("Tanggal").reset_index(drop=True)

    return data

# 3. ANALISIS DAN RINGKASAN DATA

def analisis_data(data):
    """Menghitung indikator utama untuk overview."""

    total_keluhan = len(data)

    jumlah_selesai = int(
        (data["Status"] == "Selesai").sum()
    )

    jumlah_belum_selesai = total_keluhan - jumlah_selesai

    rata_waktu = data["Waktu_Penyelesaian_Jam"].mean()

    rata_kepuasan = data["Kepuasan_Pelapor"].mean()

    kategori_terbanyak = data["Kategori"].value_counts().idxmax()

    lokasi_terbanyak = data["Lokasi"].value_counts().idxmax()

    ringkasan = pd.DataFrame([{
        "Total Keluhan": total_keluhan,
        "Keluhan Selesai": jumlah_selesai,
        "Keluhan Belum Selesai": jumlah_belum_selesai,
        "Rata-rata Waktu Penyelesaian (jam)": round(rata_waktu, 2),
        "Rata-rata Kepuasan (1-5)": round(rata_kepuasan, 2),
        "Kategori Keluhan Terbanyak": kategori_terbanyak,
        "Lokasi Keluhan Terbanyak": lokasi_terbanyak
    }])

    ringkasan.to_csv(
        OUTPUT_DIR / "ringkasan_keluhan.csv",
        index=False
    )

    return ringkasan

# 4. VISUALISASI KELUHAN BERDASARKAN KATEGORI

def grafik_kategori(data):
    """Grafik batang untuk membandingkan kategori keluhan."""

    jumlah = (
        data["Kategori"]
        .value_counts()
        .sort_values(ascending=True)
    )

    plt.figure(figsize=(10, 6))

    jumlah.plot(kind="barh")

    plt.title("Jumlah Keluhan Berdasarkan Kategori")
    plt.xlabel("Jumlah Keluhan")
    plt.ylabel("Kategori Fasilitas")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "01_keluhan_per_kategori.png",
        dpi=160
    )

    plt.close()

# 5. VISUALISASI TREN KELUHAN

def grafik_tren(data):
    """Grafik garis untuk melihat perubahan keluhan setiap bulan."""

    bulanan = (
        data.set_index("Tanggal")
        .resample("MS")
        .size()
        .rename("Jumlah Keluhan")
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        bulanan.index,
        bulanan.values,
        marker="o",
        linewidth=2
    )

    plt.title("Tren Keluhan Fasilitas per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Keluhan")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "02_tren_keluhan_bulanan.png",
        dpi=160
    )

    plt.close()

    bulanan.rename_axis("Bulan").reset_index().to_csv(
        OUTPUT_DIR / "tren_keluhan_bulanan.csv",
        index=False
    )
# 6. VISUALISASI STATUS KELUHAN BERDASARKAN LOKASI

def grafik_status_lokasi(data):
    """Membandingkan status keluhan di setiap lokasi."""

    tabel = pd.crosstab(
        data["Lokasi"],
        data["Status"]
    )

    tabel.plot(
        kind="bar",
        figsize=(10, 6)
    )

    plt.title("Status Keluhan Berdasarkan Lokasi")
    plt.xlabel("Lokasi")
    plt.ylabel("Jumlah Keluhan")
    plt.xticks(rotation=20, ha="right")
    plt.legend(title="Status")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "03_status_keluhan_per_lokasi.png",
        dpi=160
    )

    plt.close()

# 7. VISUALISASI WAKTU PENYELESAIAN BERDASARKAN PRIORITAS

def grafik_prioritas(data):
    """Menganalisis rata-rata waktu penyelesaian tiap prioritas."""

    urutan = ["Rendah", "Sedang", "Tinggi"]

    rata_waktu = (
        data.groupby("Prioritas")["Waktu_Penyelesaian_Jam"]
        .mean()
        .reindex(urutan)
    )

    plt.figure(figsize=(8, 5))

    rata_waktu.plot(kind="bar")

    plt.title(
        "Rata-rata Waktu Penyelesaian Berdasarkan Prioritas"
    )
    plt.xlabel("Prioritas Keluhan")
    plt.ylabel("Waktu Rata-rata (jam)")
    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "04_waktu_penyelesaian_prioritas.png",
        dpi=160
    )

    plt.close()

# 8. ZOOM, FILTER, DAN DETAILS-ON-DEMAND

def filter_detail(data):
    """
    Menyaring data berdasarkan kategori atau lokasi
    dengan jumlah keluhan terbanyak.
    """

    kategori_terbanyak = data["Kategori"].value_counts().idxmax()

    lokasi_terbanyak = data["Lokasi"].value_counts().idxmax()

    hasil_filter = data[
        (data["Kategori"] == kategori_terbanyak)
        | (data["Lokasi"] == lokasi_terbanyak)
    ].copy()

    hasil_filter.to_csv(
        OUTPUT_DIR / "detail_filter_keluhan.csv",
        index=False
    )

    return kategori_terbanyak, lokasi_terbanyak, hasil_filter

# 9. MENAMPILKAN HASIL ANALISIS DI TERMINAL

def tampilkan_laporan(
    data,
    ringkasan,
    kategori_terbanyak,
    lokasi_terbanyak,
    hasil_filter
):
    """Menampilkan overview dan contoh detail data."""

    print("\n" + "=" * 65)
    print(" ANALISIS KELUHAN FASILITAS KAMPUS")
    print(" HCI DAN VISUALISASI DATA - WEBINAR 5")
    print("=" * 65)

    print("\n1. OVERVIEW - RINGKASAN DATA")

    for kolom, nilai in ringkasan.iloc[0].items():
        print(f"   {kolom}: {nilai}")

    print("\n2. ZOOM AND FILTER - HASIL PENYARINGAN")

    print(
        f"   Kategori keluhan terbanyak: {kategori_terbanyak}"
    )

    print(
        f"   Lokasi dengan keluhan terbanyak: {lokasi_terbanyak}"
    )

    print(
        f"   Jumlah baris hasil filter: {len(hasil_filter)}"
    )

    print("\n3. DETAILS-ON-DEMAND - CONTOH DATA KELUHAN")

    kolom_detail = [
        "ID_Keluhan",
        "Tanggal",
        "Kategori",
        "Lokasi",
        "Prioritas",
        "Status",
        "Waktu_Penyelesaian_Jam"
    ]

    print(
        data[kolom_detail]
        .head(10)
        .to_string(index=False)
    )

    print("\n4. INTERPRETASI HASIL")

    print(
        f"   - Kategori '{kategori_terbanyak}' "
        "menjadi fokus awal pemeriksaan."
    )

    print(
        f"   - Lokasi '{lokasi_terbanyak}' "
        "perlu ditinjau lebih lanjut."
    )

    print(
        "   - Grafik mempermudah perbandingan tanpa "
        "membaca seluruh tabel mentah."
    )

    print(
        "   - Prioritas tindakan tetap perlu mempertimbangkan "
        "urgensi dan kondisi lapangan."
    )

    print("\n5. FILE OUTPUT")

    print(f"   Folder: {OUTPUT_DIR}")

    print("   - data_keluhan_kampus.csv")
    print("   - ringkasan_keluhan.csv")
    print("   - tren_keluhan_bulanan.csv")
    print("   - detail_filter_keluhan.csv")
    print("   - 01_keluhan_per_kategori.png")
    print("   - 02_tren_keluhan_bulanan.png")
    print("   - 03_status_keluhan_per_lokasi.png")
    print("   - 04_waktu_penyelesaian_prioritas.png")

    print("\nProgram selesai dijalankan.")
    print("=" * 65)

# 10. FUNGSI UTAMA

def main():
    print("Menyiapkan data keluhan fasilitas kampus...")

    data = buat_dataset()

    data.to_csv(
        OUTPUT_DIR / "data_keluhan_kampus.csv",
        index=False
    )

    print("Menganalisis data...")

    ringkasan = analisis_data(data)

    print("Membuat visualisasi...")

    grafik_kategori(data)
    grafik_tren(data)
    grafik_status_lokasi(data)
    grafik_prioritas(data)

    kategori, lokasi, hasil_filter = filter_detail(data)

    tampilkan_laporan(
        data,
        ringkasan,
        kategori,
        lokasi,
        hasil_filter
    )


if __name__ == "__main__":
    main()
