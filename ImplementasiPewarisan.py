class Pegawai:
	def __init__(self, nama, gaji=0):
		self.nama = nama
		self.gaji = gaji
	def tunjangan(self, persen):
		self.gaji = self.gaji + (self.gaji * persen)
	def kerja(self):
		print(self.nama, "Pekerjaan")
	def __repr__(self):
		return "Pegawai:\n nama = %s, gaji = %s" %(self.nama, self.gaji)
class Guru(Pegawai):
	def __init__(self, nama):
		Pegawai.__init__(self, nama, 100000)
	def kerja(self):
		print(self.nama, "Mengajar Peserta Didik")
class Satpam(Pegawai):
		def __init__(self, nama):
			Pegawai.__init__(self, nama, 40000)
		def kerja(self):
			print(self.nama, "Menjaga Lingkungan Sekolah")
class Honorer(Guru):
	def __init__(Self, nama):
		Guru.__init__(Self, nama)
	def kerja(self):
		print(self.nama, "Mengajar Peserta Didik")
class GuruBK(Satpam):
	def __init__(Self, nama):
		Satpam.__init__(Self, nama)
	def kerja(self):
		print(self.nama, "Mengembangkan Potensi Peserta Didik")	

if __name__ == "__main__":
	andi = Honorer("andi")
	print(andi)
	andi.kerja()
	andi.tunjangan(0.30)
	print(andi)
	print
	
	dewi = GuruBK("dewi")
	print(dewi)
	print
	
	for kelas in Pegawai, Guru, Satpam, Honorer, GuruBK:
		objek = kelas(kelas.__name__)
		objek.kerja()
		
