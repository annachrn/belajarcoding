data_nilai_siswa = [
    {"ID Siswa": "001", "Nama Siswa": "Gabriela Anisa", "Matematika" : 85, "Fisika": 90, "Biologi": 100, "Kelas": "X"},
    {"ID Siswa": "002", "Nama Siswa": "Lyla Andalucia", "Matematika" : 80, "Fisika": 100,"Biologi": 85, "Kelas": "X"},
    {"ID Siswa": "003", "Nama Siswa": "Madun Ahmad", "Matematika": 78, "Fisika": 83, "Biologi": 70, "Kelas": "X"},
    {"ID Siswa": "004", "Nama Siswa": "Huda Beauty", "Matematika": 70, "Fisika": 75, "Biologi": 80, "Kelas": "X"},
    {"ID Siswa": "005", "Nama Siswa": "Prima Cinthya", "Matematika": 85, "Fisika": 90, "Biologi": 90, "Kelas": "X"},
    {"ID Siswa": "006", "Nama Siswa": "Ziyad Muhammad", "Matematika" : 80, "Fisika": 70, "Biologi": 60, "Kelas": "XI"},
    {"ID Siswa": "007", "Nama Siswa": "Dayyan Ryuga", "Matematika" : 80, "Fisika": 80,"Biologi": 77, "Kelas": "XI"},
    {"ID Siswa": "008", "Nama Siswa": "Audinna", "Matematika": 100, "Fisika": 95, "Biologi": 100, "Kelas": "XI"},
    {"ID Siswa": "009", "Nama Siswa": "Miskha Aprilidita", "Matematika": 75, "Fisika": 60, "Biologi": 100, "Kelas": "XI"},
    {"ID Siswa": "010", "Nama Siswa": "Prima Wicaksono", "Matematika": 89, "Fisika": 90, "Biologi": 90, "Kelas":"XI"},
    {"ID Siswa": "011", "Nama Siswa": "Gezi Damia", "Matematika" : 80, "Fisika": 70, "Biologi": 60, "Kelas": "XII"},
    {"ID Siswa": "012", "Nama Siswa": "Nowel Ashidqi", "Matematika" : 80, "Fisika": 80,"Biologi": 77, "Kelas": "XII"},
    {"ID Siswa": "013", "Nama Siswa": "Maya Indraini", "Matematika": 100, "Fisika": 95, "Biologi": 100, "Kelas": "XII"},
    {"ID Siswa": "014", "Nama Siswa": "Antariksa", "Matematika": 75, "Fisika": 60, "Biologi": 100, "Kelas": "XII"},
    {"ID Siswa": "015", "Nama Siswa": "Prabowo Widodo", "Matematika": 89, "Fisika": 90, "Biologi": 90, "Kelas":"XII"}
]

from tabulate import tabulate

# TAMPILAN DATA 
def tampilkan_data_siswa():
    table_data = []
    for siswa in data_nilai_siswa:
        row = [
            siswa["ID Siswa"],
            siswa["Nama Siswa"],
            siswa["Matematika"],
            siswa["Fisika"],
            siswa["Biologi"],
            siswa["Kelas"]
        ]
        table_data.append(row)

    headers = ["ID Siswa", "Nama Siswa", "Matematika", "Fisika", "Biologi", "Kelas"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def validasi_id_siswa(id_siswa):
    return id_siswa.isdigit() and len(id_siswa) == 3

def validasi_kelas(kelas):
    return kelas in ['X','XI','XII']

def validasi_mapel(mapel):
    return mapel in ['Biologi','Matematika','Fisika']

def cek_duplikasi_data(id_siswa):
    for siswa in data_nilai_siswa:
        if siswa["ID Siswa"] == id_siswa:
            return True
    return False

# MENU READ HASIL UJIAN
def lihat_hasil_ujian():
    inputRead = int(input('''
         Menu menampilkan nilai siswa:
            1. Tampilkan nilai siswa
            2. Hasil ujian
            3. Kembali ke menu utama 
        Masukkan angka menu yang dijalankan:'''))
    if inputRead == 1:
        tampilkan_data_siswa()
    elif inputRead == 2:
        id_siswa = input("\tMasukkan ID Siswa: ")
        
        if not validasi_id_siswa(id_siswa):
            print("ID tidak ditemukan dan ID harus berupa 3 digit angka.")
            return
        
        for siswa in data_nilai_siswa:
            if siswa["ID Siswa"] == id_siswa:
                rata_rata = (siswa['Matematika'] + siswa['Fisika'] + siswa['Biologi']) / 3
                status = "Lulus" if rata_rata >= 75 else "Tidak Lulus"
                print("\nHasil Ujian:")
                print("Nama Siswa: {}".format(siswa['Nama Siswa']))
                print("Status: {}".format(status))
                print("Nilai Akhir: {}".format(round(rata_rata, 2)))
                return
        else:
            print("\n\t ID tidak ditemukan")
    elif inputRead == 3:
        Menu()
    else:
        print("Masukan tidak valid. Masukkan angka dari 1 hingga 3.")
    
# CREATE/ADD DATA
def tambah_nilai_siswa():
    inputRead = int(input('''
         Menu menampilkan nilai siswa:
            1. Tambah Nilai Siswa
            2. Kembali ke menu utama 
        Masukkan angka menu yang dijalankan:'''))
    
    if inputRead == 1:
        id_siswa = input("\tMasukkan ID Siswa: ")
        
        if not validasi_id_siswa(id_siswa):
            print("ID tidak ditemukan dan ID harus berupa 3 digit angka.")
            return
            
        kelas = input("\tKelas: ")

        if not validasi_kelas(kelas):
            print("Kelas harus diisi dengan bilangan romawi X, XI, XII")
            return

        if cek_duplikasi_data(id_siswa):
            print("ID siswa {} sudah ada dalam database\n".format(id_siswa))
            return
      
        nama_siswa = input("Masukkan Nama Siswa: ")
        nilai_matematika = int(input("Masukkan Nilai Matematika: "))
        nilai_fisika = int(input("Masukkan Nilai Fisika: "))
        nilai_biologi = int(input("Masukkan Nilai Biologi: "))
        
        if 0 <= nilai_matematika <= 100 and 0 <= nilai_fisika <= 100 and 0 <= nilai_biologi <= 100:
            # Lakukan apa yang perlu dilakukan jika semua nilai kurang dari 100
            print("Data berhasil ditambahkan")
            data_nilai_siswa.append({
                "ID Siswa": id_siswa,
                "Nama Siswa": nama_siswa,
                "Matematika": nilai_matematika,
                "Fisika": nilai_fisika,
                "Biologi": nilai_biologi,
                "Kelas": kelas
            })
        else:
            print("Ada nilai yang lebih dari 100. Harap masukkan nilai yang kurang dari 100 dan input lagi!")
    elif inputRead == 3:
        Menu()
    else:
        print("Masukan tidak valid")

    return 

# UPDATE DATA
def update_data_nilai_siswa():
    id_siswa = input("Masukkan ID siswa yang ingin diubah datanya: ")

    if not validasi_id_siswa(id_siswa):
        print("ID tidak ditemukan dan ID harus berupa 3 digit angka.")
        return
    
    # Membuat fungsi internal untuk menampilkan data siswa berdasarkan ID
    def tampilkan_data_berdasarkan_ID(id_siswa):
        for siswa in data_nilai_siswa:
            if siswa["ID Siswa"] == id_siswa:
                print("Data siswa dengan ID", id_siswa, "adalah:")
                print(f"ID Siswa: {siswa['ID Siswa']}")
                print(f"Nama Siswa: {siswa['Nama Siswa']}")
                print(f"Nilai Matematika: {siswa['Matematika']}")
                print(f"Nilai Fisika: {siswa['Fisika']}")
                print(f"Nilai Biologi: {siswa['Biologi']}")
                print(f"Kelas: {siswa['Kelas']}")
                return siswa

        print("ID siswa tidak ditemukan.")
        return None

    # Menampilkan data siswa berdasarkan ID
    siswa = tampilkan_data_berdasarkan_ID(id_siswa)
    if not siswa:
        return

    # Menampilkan menu kategori pengubahan data
    print("\nPilih kategori data yang ingin diubah:")
    print("1. ID Siswa")
    print("2. Nama Siswa")
    print("3. Nilai Matematika")
    print("4. Nilai Fisika")
    print("5. Nilai Biologi")
    print("6. Kelas")

    kategori = input("\nPilih kategori data yang ingin diubah (1-6): ")

    if kategori == "1":
        nilai_baru = input(f"Masukkan nilai baru untuk kategori {kategori}: ")
        if not validasi_id_siswa(id_siswa):
            print("ID tidak ditemukan dan ID harus berupa 3 digit angka.")
            return
        # Validasi ID siswa jika sudah ada dalam database
        if cek_duplikasi_data(nilai_baru):
            print("ID siswa {} sudah ada dalam database. Gagal memperbarui data.\n".format(nilai_baru))
            return
        siswa["ID Siswa"] = nilai_baru
        print("Data telah diperbarui.")
    elif kategori == "2":
        nilai_baru = input(f"Masukkan nilai baru untuk kategori {kategori}: ")
        # Validasi nama siswa
        if not nilai_baru.isalpha() or len(nilai_baru) <= 100 :
            print("Nama siswa harus berupa huruf dan tidak boleh lebih dari 255 karakter.")
            return
        siswa["Nama Siswa"] = nilai_baru
        print("Data telah diperbarui.")
    elif kategori in ["3", "4", "5"]:
        nilai_baru = input(f"Masukkan nilai baru untuk kategori {kategori}: ")
        # Validasi nilai matematika, fisika, biologi
        if not nilai_baru.isdigit() or int(nilai_baru) < 0 or int(nilai_baru) > 100:
            print("Nilai harus berupa angka antara 0 hingga 100.")
            return
        siswa[list(siswa.keys())[int(kategori) - 1]] = int(nilai_baru)
        print("Data telah diperbarui.")
    elif kategori == "6":
        nilai_baru = input(f"Masukkan nilai baru untuk kategori {kategori}: ")
        # Validasi kelas
        if nilai_baru not in ['X', 'XI', 'XII']:
            print("Kelas harus diisi dengan 'X', 'XI', atau 'XII'.")
            return
        siswa["Kelas"] = nilai_baru
        print("Data telah diperbarui.")
    else:
        print("Kategori tidak valid.")


# DELETE DATA
def hapus_nilai_siswa():
    print("Menu menampilkan nilai siswa:")
    print("1. Hapus Nilai Siswa")
    print("2. Kembali ke menu utama")
    
    inputRead = input("Masukkan angka menu yang dijalankan: ")

    if inputRead == "1":
        id_siswa = input("\tMasukkan ID Siswa: ")
        removed = False
        
        if not validasi_id_siswa(id_siswa):
            print("ID tidak ditemukan dan harus berupa 3 digit angka.")
            return

        for siswa in data_nilai_siswa:
            if siswa["ID Siswa"] == id_siswa:
                print("Detail siswa yang akan dihapus:")
                print(siswa)
                konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (ya/tidak): ")
                if konfirmasi.lower() == "ya":
                    data_nilai_siswa.remove(siswa)
                    removed = True
                    print("Data siswa dengan ID {} telah dihapus.".format(id_siswa))
                    break

        if not removed:
            print("Data siswa dengan ID {} batal dihapus".format(id_siswa))
    elif inputRead == "2":
        print("Kembali ke Menu Utama")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")


# MENU UTAMA
def Menu():
    while True:
        pilihanMenu = input('''
        Selamat Datang di Data Base Nilai Siswa SMA Suka Suka 

        List Menu :
        1. Melihat Data Siswa dan Hasil Ujian
        2. Menambahkan Nilai Ujian 
        3. Menghapus Nilai Ujian
        4. Mengupdate Data Siswa
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            lihat_hasil_ujian()
        elif pilihanMenu == '2':
            tambah_nilai_siswa()
        elif pilihanMenu == '3':
            hapus_nilai_siswa()
        elif pilihanMenu == '4':
            update_data_nilai_siswa()
        elif pilihanMenu == '5':
            break
        else:
            print("Masukan tidak valid. Masukkan angka dari 1 hingga 5.")
Menu()


# # Memanggil fungsi untuk menghapus data siswa
# hapus_nilai_siswa()

# # Menampilkan data siswa setelah penghapusan
# print(data_nilai_siswa)

# # Meminta input dari pengguna
# id_siswa = input("Masukkan ID Siswa yang ingin dilihat nilainya: ")
# kelas = input("Masukkan Kelas siswa (X, XI, atau XII): ")

# # Memanggil fungsi yang sesuai
# lihat_hasil_ujian(id_siswa, kelas)
# # lihat_rincian_nilai_ujian(id_siswa, kelas)

# # Memanggil fungsi untuk menambahkan data siswa baru
# tambah_nilai_siswa()

# # Menampilkan data siswa setelah penambahan
# print(data_nilai_siswa)

# def validasi_id_kelas(id_siswa, kelas):
#     found_id_kelas = False
#     for siswa in data_nilai_siswa:
#         if siswa["ID Siswa"] == id_siswa and siswa["Kelas"] == kelas:
#             found_id_kelas = True
#             return True

#     if not found_id_kelas:
#         print("Data tidak ditemukan untuk ID Siswa tersebut pada kelas yang dimasukkan.")
#         return False

# def lihat_hasil_ujian():
#     id_siswa = input("Masukkan ID siswa: ")
#         # periksa panjang dan apakah ID terdiri dari angka
#     if not validasi_id_siswa(id_siswa):
#             print("ID siswa harus berupa 3 digit angka.")
#             return
#     kelas = input("Masukkan kelas:")   
#         # periksa panjang dan apakah kelas X, XI, XII
#     if not validasi_kelas(kelas):
#             print("Kelas harus diisi dengan bilangan romawi X, XI, XII")
#             return
#     for siswa in data_nilai_siswa:
#         if siswa["ID Siswa"] == id_siswa and siswa["Kelas"] == kelas:
#             rata_rata = (siswa['Matematika'] + siswa['Fisika'] + siswa['Biologi']) / 3
#             status = "Lulus" if rata_rata >= 75 else "Tidak Lulus"
#             print("\nHasil Ujian:")
#             print("Nama Siswa: {}".format(siswa['Nama Siswa']))
#             print("Status: {}".format(status))
#             print("Nilai Akhir: {}".format(round(rata_rata, 2)))
#             return

#     print("Data siswa tidak ditemukan.")

# def tambah_nilai_siswa():
#     id_siswa = input("Masukkan ID siswa: ")
#     # periksa panjang dan apakah ID terdiri dari angka
#     if not validasi_id_siswa(id_siswa):
#             print("ID siswa harus berupa 3 digit angka.")
#             return
#     kelas = input("Masukkan kelas:")   
#     # periksa panjang dan apakah ID terdiri dari angka
#     if not validasi_kelas(kelas):
#            print("Kelas harus diisi dengan bilangan romawi X, XI, XII")
#            return

#     # periksa duplikasi data
#     for siswa in data_nilai_siswa:
#         if siswa["ID Siswa"] == id_siswa:
#             print("ID siswa {} sudah ada dalam database\n".format(id_siswa))
#             return
      
#     nama_siswa = input("Masukkan Nama Siswa: ")
#     nilai_matematika = int(input("Masukkan Nilai Matematika: "))
#     nilai_fisika = int(input("Masukkan Nilai Fisika: "))
#     nilai_biologi = int(input("Masukkan Nilai Biologi: "))
    
#     if 0 <= nilai_matematika <= 100 and 0 <= nilai_fisika <= 100 and 0 <= nilai_biologi <= 100:
#     # Lakukan apa yang perlu dilakukan jika semua nilai kurang dari 100
#         print("Semua nilai valid, data berhasil di tambahkan")
#     else:
#         print("Ada nilai yang lebih dari 100. Harap masukkan nilai yang kurang dari 100 dan Input Lagi!")

#     data_nilai_siswa.append({
#         "ID Siswa": id_siswa,
#         "Nama Siswa": nama_siswa,
#         "Matematika": nilai_matematika,
#         "Fisika": nilai_fisika,
#         "Biologi": nilai_biologi,
#         "Kelas": kelas
#     })
