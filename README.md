# Capstone-Project-Module-1

# Program Manajemen Data Pasien Rumah Sakit

Ini adalah program sederhana command-line untuk mengelola data pasien di bagian gawat darurat rumah sakit. Program ini memungkinkan pengguna untuk:

- Melihat semua data pasien
- Mencari pasien berdasarkan ID atau kondisi  
- Menambahkan pasien baru
- Memperbarui data pasien yang ada
- Menghapus pasien (dipindahkan ke recycle bin)
- Mengembalikan pasien yang dihapus dari recycle bin
- Keluar dari program

## Fitur

- Sistem menu terorganisir untuk navigasi opsi
- Validasi input untuk entri data
- Pengurutan dan pemformatan data saat melihat
- Recycle bin untuk mengembalikan catatan yang dihapus
- Konfirmasi sebelum menyimpan/menghapus data
- Penyimpanan data persisten (data disimpan di antara sesi)

## Data Pasien  

Setiap catatan pasien berisi data berikut:

- ID (dibuat otomatis)
- Nama  
- Umur
- Jenis kelamin
- Kondisi (Tidak Mendesak, Cukup Mendesak, Mendesak)

## Penggunaan

Program dijalankan melalui command-line. Ikuti prompt menu untuk navigasi opsi.  

Masukkan data saat diminta. Validasi akan menangkap format yang tidak valid.

Catatan pasien disimpan dalam kamus dengan ID sebagai kunci.

Pasien yang dihapus dipindahkan ke kamus recycle bin terpisah.

## Persyaratan

- Python 3
- Modul datetime
- Modul re

## Pengembangan

Pengembangan lebih lanjut bisa mencakup:

- Antarmuka GUI
- Kemampuan mengedit beberapa catatan sekaligus
- Pencarian dengan beberapa kriteria
- Opsi pengurutan saat melihat catatan 
- Ekspor data ke file/database
- Akun pengguna untuk melacak perubahan

## Lisensi

Proyek ini bersifat open source dan bebas digunakan/dimodifikasi.
