class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim  = nim
        self.prodi= prodi

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}")

    def get_nim(self):
        return self._nim 
    
    def get_prodi(self):
        return self._prodi 
    
    def set_nim(self, nim_baru):
        self._nim = nim_baru

    def set_prodi(self, prodi_baru):
        self._prodi = prodi_baru

Mahasiswa = Mahasiswa("arial","2224567", "informatika")
Mahasiswa.tampilkan_info()

print("NIM:", Mahasiswa.get_nim)
print("Prodi:",Mahasiswa.get_prodi)

Mahasiswa.set_nim("2224567")
Mahasiswa.set_prodi("Teknologi informasi")

Mahasiswa.tampilkan_info