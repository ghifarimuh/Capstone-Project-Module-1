import datetime
import re

data_pasien = {
  "P001": {"Nama": "John Doe", "Umur": 35, "Jenis Kelamin": "Laki-laki", "Kondisi": "Tidak Mendesak"},
  "P002": {"Nama": "Jane Smith", "Umur": 28, "Jenis Kelamin": "Perempuan", "Kondisi": "Cukup Mendesak"},
  "P003": {"Nama": "Bob Johnson", "Umur": 62, "Jenis Kelamin": "Laki-laki", "Kondisi": "Mendesak"}
}

nama_kolom = ["ID", "Nama", "Umur", "Jenis Kelamin", "Kondisi"]
recycle_bin = {}

def hitung_umur(tanggal_lahir):
  hari_ini = datetime.date.today()
  return hari_ini.year - tanggal_lahir.year - ((hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
  
def menu_utama():

  print("-"*80)
  
  while True:
    print("Data Pasien Rumah Sakit UGD Sederhana by Akhmad Ghifari Muhammad")
    print("-"*80)
    print("1. Informasi Data Pasien")
    print("2. Tambah Data Pasien Baru")
    print("3. Perbarui Data Pasien")
    print("4. Hapus Data Pasien")
    print("5. Recycle Bin")
    print("6. Keluar")
    print("-"*80)
    
    pilihan = input("Masukkan pilihan: ")
    print("-"*80)

    if pilihan == "1":
      daftar_pasien()
    elif pilihan == "2":
      tambah_pasien_baru()
    elif pilihan == "3":
      perbarui_data_pasien()
    elif pilihan == "4":
      hapus_data_pasien()
    elif pilihan == "5":
      lihat_recycle_bin()
    elif pilihan == "6":
      print("Keluar dari program...")
      exit()
      break
    else:
      print("Pilihan tidak valid")
      print("-"*80)

def daftar_pasien():

  print("-"*80)
  
  while True:
    print("1. Lihat Seluruh Data Pasien")
    print("2. Cari Berdasarkan ID")
    print("3. Cari Berdasarkan Kondisi")
    print("4. Kembali ke Menu Utama")
    print("-"*80)
    
    pilihan = input("Masukkan pilihan: ")
    print("-"*80)

    if pilihan == "1":
      print("\nINFORMASI DATA PASIEN")
      print("-"*80)
      print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
      print("-"*80)
      for id_pasien in sorted(data_pasien.keys()):
        info = data_pasien[id_pasien]
        print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
      print("-"*80)
      break

    elif pilihan == "2":
      
      print("-"*80)
      while True:
        id_pasien = input("Masukkan ID pasien: ").upper()
        print("-"*80)
        if id_pasien in data_pasien:
          break
        print("ID pasien tidak valid")
        print("-"*80)
      
      print("\nINFORMASI DATA PASIEN")
      print("-"*80)
      print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
      print("-"*80)
      info = data_pasien[id_pasien]
      print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
      print("-"*80)
      break

    elif pilihan == "3":
      
      print("-"*80)
      while True:
        kondisi = input("Masukkan kondisi (1. Tidak Mendesak, 2. Cukup Mendesak, 3. Mendesak): ")
        print("-"*80)
        if kondisi in ["1", "2", "3"]:
          break
        print("Pilihan tidak valid")
        print("-"*80)
      
      dict_kondisi = {"1": "Tidak Mendesak", "2": "Cukup Mendesak", "3": "Mendesak"}
      kondisi = dict_kondisi[kondisi]
      
      print("\nINFORMASI DATA PASIEN")
      print("-"*80)
      print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
      print("-"*80)
      for id_pasien, info in data_pasien.items():
        if info["Kondisi"] == kondisi:
          print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
      print("-"*80)
      break

    elif pilihan == "4":
      menu_utama()

    else:
      print("Pilihan tidak valid")
      print("-"*80)

  print("-"*80)
  print("1. Kembali ke Menu Informasi Data Pasien")
  print("2. Kembali ke Menu Utama")
  print("-"*80)
  
  while True:
    pilihan = input("Masukkan pilihan: ")
    print("-"*80)
    if pilihan in ["1", "2"]:
      break
    print("Pilihan tidak valid")
  
  if pilihan == "1":
    daftar_pasien()
  elif pilihan == "2":  
    menu_utama()

def tambah_pasien_baru():

  print("-"*80)
  print("\nTAMBAH DATA PASIEN BARU")
  print("-"*80)

  while True:
    nama = input("Nama: ").title()
    print("-"*80)
    if re.match("^[a-zA-Z ]*$", nama):
      break
    print("\nNama hanya boleh mengandung huruf alfabet dan spasi")
  
  print("-"*80)
  while True:
    try:
      tanggal_lahir = datetime.datetime.strptime(input("Tanggal Lahir (dd/mm/yyyy): "), "%d/%m/%Y").date()
      print("-"*80)
      break
    except ValueError:
      print("\nFormat tanggal tidak valid")

  umur = hitung_umur(tanggal_lahir)

  print("-"*80)
  while True:
    jenis_kelamin = input("Jenis Kelamin (1. Laki-laki, 2. Perempuan): ")
    if jenis_kelamin in ["1", "2"]:
      break
    print("Pilihan tidak valid")

  dict_jenis_kelamin = {"1": "Laki-laki", "2": "Perempuan"}
  jenis_kelamin = dict_jenis_kelamin[jenis_kelamin]

  print("-"*80)
  while True:
    kondisi = input("Kondisi (1. Tidak Mendesak, 2. Cukup Mendesak, 3. Mendesak): ")
    print("-"*80)
    if kondisi in ["1", "2", "3"]:
      break
    print("\nPilihan tidak valid")
  
  dict_kondisi = {"1": "Tidak Mendesak", "2": "Cukup Mendesak", "3": "Mendesak"}
  kondisi = dict_kondisi[kondisi]

  total_pasien = len(data_pasien) + len(recycle_bin) + 1
  id_baru = "P" + str(total_pasien).zfill(3)

  data_pasien[id_baru] = {
    "Nama": nama,
    "Umur": umur, 
    "Jenis Kelamin": jenis_kelamin,
    "Kondisi": kondisi
  }

  print("\nPasien berhasil ditambahkan!")
  print("-"*80)

  print("\nINFORMASI DATA PASIEN")
  print("-"*80)
  print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
  print("-"*80)
  for id_pasien in sorted(data_pasien.keys()):
    info = data_pasien[id_pasien]
    print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
  print("-"*80)
  
  konfirmasi = input("Apakah Anda yakin ingin menyimpan data ini? (Y/N): ")
  print("-"*80)
  while konfirmasi.upper() not in ["Y", "N"]:
    print("-"*80)
    print("Format pilihan tidak valid")
    konfirmasi = input("Apakah Anda yakin ingin menyimpan data ini? (Y/N) ")
    print("-"*80)
  
  if konfirmasi.upper() == "N":
    print("Data tidak disimpan")
    print("-"*80)
    del data_pasien[id_baru]
    return
  
  print("Data pasien baru berhasil disimpan!")

  while True:
    print("1. Kembali ke Menu Tambah Data Pasien")
    print("2. Kembali ke Menu Utama")
    print("-"*80)
    sub_pilihan = input("Masukkan pilihan: ")
    if sub_pilihan in ["1", "2"]:
      break
    print("Pilihan tidak valid!")

  if sub_pilihan == "1":
    tambah_pasien_baru()
  else:
    menu_utama()

def perbarui_data_pasien():

  print("-"*80)
  print("\nPERBARUI DATA PASIEN")
  print("-"*80)

  while True:
    id_pasien = input("Masukkan ID pasien untuk diperbarui: ").upper()
    print("-"*80)
    if id_pasien in data_pasien:
      break
    print("ID pasien tidak valid")

  info_original = data_pasien[id_pasien].copy()
  
  print("-"*80)
  while True:
    print("1. Nama")
    print("2. Umur")
    print("3. Jenis Kelamin")
    print("4. Kondisi")
    print("5. Kembali ke Menu Utama")
    print("-"*80)
    pilihan = input("Apa yang ingin Anda perbarui: ")
    print("-"*80)
    if pilihan in ["1", "2", "3", "4", "5"]:
      break
    print("Pilihan tidak valid")

  if pilihan == "1":
    while True:
      nama = input("Masukkan nama baru: ").title()
      print("-"*80)
      if re.match("^[a-zA-Z ]*$", nama):
        break
      print("Nama hanya boleh mengandung huruf alfabet dan spasi")
    data_pasien[id_pasien]["Nama"] = nama

  elif pilihan == "2":
    while True:
      try:
        tanggal_lahir = datetime.datetime.strptime(input("Masukkan Tanggal Lahir baru (dd/mm/yyyy): "), "%d/%m/%Y").date()
        print("-"*80)
        break
      except ValueError:
        print("Format tanggal tidak valid")

    umur = hitung_umur(tanggal_lahir)
    data_pasien[id_pasien]["Umur"] = umur

  elif pilihan == "3":
    while True:
      jenis_kelamin = input("Masukkan jenis kelamin baru (1. Laki-laki, 2. Perempuan): ")
      print("-"*80)
      if jenis_kelamin in ["1", "2"]:
        break
      print("Pilihan tidak valid")

    dict_jenis_kelamin = {"1": "Laki-laki", "2": "Perempuan"}
    jenis_kelamin = dict_jenis_kelamin[jenis_kelamin]
    data_pasien[id_pasien]["Jenis Kelamin"] = jenis_kelamin

  elif pilihan == "4":
    while True:
      kondisi = input("Masukkan kondisi baru (1. Tidak Mendesak, 2. Cukup Mendesak, 3. Mendesak): ")
      print("-"*80)
      if kondisi in ["1", "2", "3"]:
        break
      print("Pilihan tidak valid")

    dict_kondisi = {"1": "Tidak Mendesak", "2": "Cukup Mendesak", "3": "Mendesak"}
    kondisi = dict_kondisi[kondisi]
    data_pasien[id_pasien]["Kondisi"] = kondisi

  elif pilihan == "5":
    print("-"*80)
    menu_utama()

  print("\nPerubahan Data Sementara:")
  print("-"*80)
  print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
  print("-"*80)
  print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, data_pasien[id_pasien]["Nama"], data_pasien[id_pasien]["Umur"], data_pasien[id_pasien]["Jenis Kelamin"], data_pasien[id_pasien]["Kondisi"]))
  print("-"*80)

  konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan data ini? (Y/N): ")
  print("-"*80)
  while konfirmasi.upper() not in ["Y", "N"]:
    print("-"*80)
    print("Format pilihan tidak valid")
    konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan data ini? (Y/N): ")
    print("-"*80)
  
  if konfirmasi.upper() == "N":
    print("Perubahan data tidak disimpan")
    print("-"*80)
    data_pasien[id_pasien] = info_original
    return

  print("Perubahan data pasien berhasil disimpan!")

def hapus_data_pasien():

  print("-"*80)
  print("\nHAPUS DATA PASIEN")
  print("-"*80)

  while True:
    id_pasien = input("Masukkan ID pasien untuk dihapus: ").upper()
    print("-"*80)
    if id_pasien in data_pasien:
      break
    print("ID pasien tidak valid")

  konfirmasi = input("Apakah Anda yakin ingin menghapus data pasien ini? (Y/N): ")
  print("-"*80)
  while konfirmasi.upper() not in ["Y", "N"]:
    print("-"*80)
    print("Format pilihan tidak valid")
    konfirmasi = input("Apakah Anda yakin ingin menghapus data pasien ini? (Y/N): ")
    print("-"*80)
  
  if konfirmasi.upper() != "Y":
    print("Data pasien tidak dihapus")
    print("-"*80)
    return

  recycle_bin[id_pasien] = data_pasien[id_pasien]
  del data_pasien[id_pasien]

  print("\nData pasien berhasil dihapus!")
  print("-"*80)

  print("\nINFORMASI DATA PASIEN")
  print("-"*80)
  print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
  print("-"*80)
  for id_pasien in sorted(data_pasien.keys()):
    info = data_pasien[id_pasien]
    print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
  print("-"*80)

  while True:
    print("1. Kembali ke Menu Hapus Data Pasien")
    print("2. Kembali ke Menu Utama")
    print("-"*80)
    sub_pilihan = input("Masukkan pilihan: ")
    if sub_pilihan in ["1", "2"]:
      break
    print("Pilihan tidak valid!")

  if sub_pilihan == "1":
    hapus_data_pasien()
  else:
    menu_utama()


def lihat_recycle_bin():
  
  print("-"*80)
  print("\nRECYCLE BIN")
  print("-"*80)

  if not recycle_bin:
    print("Recycle bin kosong.")
  else:
    print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(nama_kolom[0], nama_kolom[1], nama_kolom[2], nama_kolom[3], nama_kolom[4]))
    print("-"*80)
    for id_pasien, info in recycle_bin.items():
      print("{:<10}|{:<15}|{:^5}|{:^15}|{:^15}".format(id_pasien, info["Nama"], info["Umur"], info["Jenis Kelamin"], info["Kondisi"]))
    print("-"*80)
    
  print("1. Kembalikan Data Pasien")
  print("2. Kembali ke Menu Utama")
  
  print("-"*80)
  while True:
    pilihan = input("Masukkan pilihan: ")
    print("-"*80)
    if pilihan in ["1", "2"]:
      break
    print("Pilihan tidak valid")

  if pilihan == "1":
    kembalikan_data_pasien()
  elif pilihan == "2":
    menu_utama()


def kembalikan_data_pasien():

  print("-"*80)
  if not recycle_bin:
    print("Recycle bin kosong.")
    print("-"*80)
    input("\nTekan Enter untuk kembali ke menu utama...")
    print("-"*80)
    menu_utama()
        
  while True:
    id_pasien = input("Masukkan ID pasien untuk dikembalikan: ").upper()
    print("-"*80)
    if id_pasien in recycle_bin:
      break
    print("ID pasien tidak valid")

  konfirmasi = input("Apakah Anda yakin ingin mengembalikan data pasien ini? (Y/N): ")
  print("-"*80)
  while konfirmasi.upper() not in ["Y", "N"]:
    print("-"*80)
    print("Format pilihan tidak valid")  
    konfirmasi = input("Apakah Anda yakin ingin mengembalikan data pasien ini? (Y/N): ")
    print("-"*80)
  
  if konfirmasi.upper() != "Y":
    print("Data pasien tidak dikembalikan")
    print("-"*80)
    return

  data_pasien[id_pasien] = recycle_bin[id_pasien]
  del recycle_bin[id_pasien]

  print("Data pasien berhasil dikembalikan!")
  print("-"*80)

  print("-"*80)
  input("\nTekan Enter untuk kembali ke menu Recycle Bin...")
  print("-"*80)
  lihat_recycle_bin()

print("-"*80)
menu_utama()
print("-"*80)