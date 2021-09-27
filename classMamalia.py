class Mamalia:
	def __init__(self, nama, umur, jenis)
		self.nama = nama
		self.umur = umur
		self.jenis = jenis
	
	def printname(self):
		print(self.nama)
		print(self.umur)
		print(self.jenis)
	
class Kucing(Mamalia):
	def __init__(self, nama, umur, jenis):
			mamalia.__init__(self, nama, umur, jenis)
			
class Anjing(Mamalia):
	def __init__(self, nama, umur, jenis):
			mamalia.__init__(self, nama, umur, jenis)
			
	
x = Kucing("Bulu", 2, "Persia")
y = Anjing("Tortila", 4, "Cihuahua")

x.printname()
y.printname()


		