nama_mahasiswa = input("Masukan Namamu : ")
mata_kuliah = input("Masukan Mata Kuliah : ")
nilai = int(input("Masukan Nilai : "))

print(40*'=')
print("Mahasiswa dengan nama", nama_mahasiswa)
if (nilai >= 81) and (nilai <= 100):
    print("Mendapat predikat : A")
    print("Dinyatakan Lulus Mata Kuliah", mata_kuliah)
elif (nilai >= 71) and (nilai  <= 80):
    print("Mendapat predikat : B")
    print("Dinyatakan Lulus Mata Kuliah", mata_kuliah)
elif (nilai >= 61) and (nilai <= 70):
    print("Mendapat predikat : C")
    print("Dinyatakan Lulus Mata Kuliah", mata_kuliah)
else:
    print("Harus Mengulang Mata Kuliah", mata_kuliah)
