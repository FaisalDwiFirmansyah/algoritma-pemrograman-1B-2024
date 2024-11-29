print("===========================")
print("|     SELAMAT DATANG      |")
print("|   DI RUMAH SAKIT FUAD   |")
print("|         HUSADA          |")
print("===========================")

kapasitas_ruangan = {
    "Mawar": 5,
    "Anggrek": 5,
    "Melati": 5,
    "Tulip": 5
}

data_rumah_sakit = {
    "Mawar": [],
    "Anggrek": [],
    "Melati": [],
    "Tulip": []
}

def tambah_pasien():
    print("Pilih ruangan untuk pasien:")
    ruangan_list = list(data_rumah_sakit.keys())
    for i, ruangan in enumerate(ruangan_list, start=1):
        print(f"{i}. {ruangan} (Kapasitas: {len(data_rumah_sakit[ruangan])}/{kapasitas_ruangan[ruangan]})")
    pilihan = input("Pilih nomor ruangan: ")
    if not pilihan.isdigit():
        print("Input harus berupa angka. Silakan coba lagi.")
        return
    pilihan = int(pilihan)
    if 1 <= pilihan <= len(ruangan_list):
        ruangan = ruangan_list[pilihan - 1]
    else:
        print("Nomor ruangan tidak valid. Silakan coba lagi.")
        return
    
    if ruangan:
        if len(data_rumah_sakit[ruangan]) >= kapasitas_ruangan[ruangan]:
            print(f"Ruangan {ruangan} sudah penuh! Silakan pilih ruangan lain.")
            return

    nama = input("Masukkan nama pasien: ")
    umur = input("Masukkan umur pasien: ")
    penyakit = input("Masukkan penyakit pasien: ")
    tingkat_keparahan = input("Masukkan tingkat keparahan (Ringan/Sedang/Berat): ")
    tanggal_kontrol = input("Tanggal masuk rumah sakit (dd-mm-yyyy): ")

    pasien = {
        "Nama": nama,
        "Umur": umur,
        "Penyakit": penyakit,
        "Tingkat Keparahan": tingkat_keparahan,
        "Tanggal Kontrol": tanggal_kontrol
    }
    data_rumah_sakit[ruangan].append(pasien)
    print(f"Pasien berhasil ditambahkan ke ruangan {ruangan}!")

def lihat_semua_pasien():
    for ruangan, pasien_list in data_rumah_sakit.items():
        print(f"\nRuangan: {ruangan} (Kapasitas: {len(pasien_list)}/{kapasitas_ruangan[ruangan]})")
        if not pasien_list:
            print("  Tidak ada pasien.")
        else:
            for i, pasien in enumerate(pasien_list, start=1):
                print(f"  Pasien {i}:")
                for key, value in pasien.items():
                    print(f"    {key}: {value}")

def lihat_pasien_per_ruangan():
    print("Pilih ruangan untuk melihat pasien:")
    ruangan_list = list(data_rumah_sakit.keys())
    for i, ruangan in enumerate(ruangan_list, start=1):
        print(f"{i}. {ruangan}")
    pilihan = input("Pilih nomor ruangan: ")
    if not pilihan.isdigit():
        print("Pilihan harus berupa angka.")
        return
    pilihan = int(pilihan)
    if 1 <= pilihan <= len(ruangan_list):
        ruangan = ruangan_list[pilihan - 1]
    else:
        print("Pilihan ruangan tidak valid.")
        return

    pasien_list = data_rumah_sakit[ruangan]
    print(f"\nPasien di ruangan {ruangan} (Kapasitas: {len(pasien_list)}/{kapasitas_ruangan[ruangan]}):")
    if not pasien_list:
        print("  Tidak ada pasien.")
    else:
        for i, pasien in enumerate(pasien_list, start=1):
            print(f"  Pasien {i}:")
            for key, value in pasien.items():
                print(f"    {key}: {value}")

def update_pasien():
    lihat_semua_pasien()
    ruangan = input("\nMasukkan nama ruangan pasien yang ingin diupdate: ")

    if ruangan not in data_rumah_sakit:
        print("Ruangan tidak valid.")
        return

    pasien_list = data_rumah_sakit[ruangan]
    if not pasien_list:
        print(f"Tidak ada pasien di ruangan {ruangan}.")
        return

    nomor_pasien = input("Masukkan nomor pasien yang ingin diupdate: ")
    if not nomor_pasien.isdigit():
        print("Nomor pasien harus berupa angka.")
        return
    nomor_pasien = int(nomor_pasien)
    if nomor_pasien < 1 or nomor_pasien > len(pasien_list):
        print("Nomor pasien tidak valid.")
        return

    pasien = pasien_list[nomor_pasien - 1]
    print("Masukkan data baru (tekan Enter untuk melewati):")
    pasien["Nama"] = input(f"Nama ({pasien['Nama']}): ") or pasien["Nama"]
    pasien["Umur"] = input(f"Umur ({pasien['Umur']}): ") or pasien["Umur"]
    pasien["Penyakit"] = input(f"Penyakit ({pasien['Penyakit']}): ") or pasien["Penyakit"]
    pasien["Tingkat Keparahan"] = input(f"Tingkat Keparahan ({pasien['Tingkat Keparahan']}): ") or pasien["Tingkat Keparahan"]
    pasien["Tanggal Kontrol"] = input(f"Tanggal Kontrol ({pasien['Tanggal Kontrol']}): ") or pasien["Tanggal Kontrol"]
    print("Data pasien berhasil diperbarui!")

tambah_pasien()
lihat_semua_pasien()
lihat_pasien_per_ruangan()
update_pasien()