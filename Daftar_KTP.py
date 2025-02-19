import time
from datetime import datetime

# Fungsi untuk menghitung umur
def hitung_umur(tanggal_lahir):
    hari_ini = datetime.today()
    umur = hari_ini.year - tanggal_lahir.year

    # Cek apakah ulang tahun sudah lewat atau belum
    if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
        umur -= 1

    return umur

# Fungsi utama
def buat_ktp():
    print("=== Selamat Datang di Layanan Pembuatan KTP Online ===")

    # Input data dari user
    nama = input("Masukkan nama lengkap: ")
    tempat_lahir = input("Masukkan tempat lahir: ")
    tanggal_lahir = input("Masukkan tanggal lahir (format: YYYY-MM-DD): ")

    # Konversi input tanggal lahir ke format datetime
    try:
        tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal salah! Gunakan format YYYY-MM-DD.")
        return

    # Hitung umur
    umur = hitung_umur(tanggal_lahir)

    # Cek apakah user sudah cukup umur
    if umur < 17:
        print("Maaf, kamu belum cukup umur untuk membuat KTP.")
        print("Usia minimal untuk membuat KTP adalah 17 tahun.")
        return
    else:
        print("\nData kamu sedang diproses...")
        time.sleep(5)  # Simulasi proses selama 5 detik

        # Tampilkan data KTP
        print("\n=== Data KTP ===")
        print(f"Nama: {nama}")
        print(f"Tempat, Tanggal Lahir: {tempat_lahir}, {tanggal_lahir.strftime('%Y-%m-%d')}")
        print(f"Umur: {umur} tahun")
        print("Status: KTP berhasil dibuat!")
