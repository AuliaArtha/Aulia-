class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self._nim = nim  
        self._prodi = prodi 

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self._nim}, Prodi: {self._prodi}")

    def get_nim(self):
        return self._nim

    def set_nim(self, nim_baru):
        self._nim = nim_baru

    def get_prodi(self):
        return self._prodi

    def set_prodi(self, prodi_baru):
        self.set_prodi = prodi_baru

Mahasiswa = Mahasiswa ("arial", "2224567", "informatika")
Mahasiswa.tampilkan_info()

print("NIM   :", Mahasiswa.get_nim())
print("Prodi :", Mahasiswa.get_prodi())

Mahasiswa.set_nim("2224567")
Mahasiswa.set_prodi("Teknologi informasi")

Mahasiswa.tampilkan_info()