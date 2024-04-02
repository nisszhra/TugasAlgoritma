nama_mahasiswa = input("Masukan Namamu : ")
mata_kuliah = input("Masukan Mata Kuliah : ")
kehadiran = int(input("Masukan kehadiranmu (1-14) : "))
nilai_tugas = int(input("Masukan Nilai Tugas : "))
nilai_uts = int(input("Masukan Nilai UTS : "))
nilai_uas = int(input("Masukan Nilai UAS : "))

minimal_kehadiran = (12,13,14)
nilai_akhir = (nilai_tugas + nilai_uts + nilai_uas)/3

print(40*'=')
print("Mahasiswa dengan nama", nama_mahasiswa)
print("Total Kehadiran : ", kehadiran, " pertemuan")
print("Nilai akhir : ", nilai_akhir)
if kehadiran in minimal_kehadiran and (nilai_akhir >= 90) and (nilai_akhir <= 100):
    print("Predikat : A")
    print("Lulus Mata Kuliah", mata_kuliah)
elif kehadiran in minimal_kehadiran and (nilai_akhir >= 80) and (nilai_akhir <= 89):
    print("Predikat : B")
    print("Lulus Mata Kuliah", mata_kuliah)
elif kehadiran in minimal_kehadiran and (nilai_akhir >= 70) and (nilai_akhir <= 79):
    print("Predikat : C")
    print("Lulus Mata Kuliah", mata_kuliah)
else:
    print("Tidak Lulus Mata Kuliah ", mata_kuliah)
    print("Silahkan hubungi dosen yang bersangkutan untuk perbaikan.")