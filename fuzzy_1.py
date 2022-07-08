
def down(x, main, xmax):
    return (xmax - x) / (xmax - xmin)

    def up(x, xmin, xmax):
        return (x - xmin) / (xmax - xmin)

        class permintaan():
            minimum = 2500
            maximum = 4000

            def turun(self, x):
            if x >= self .maximum:
            return 0
            elif x<= self .minimum:
            return 0
            else :
            return down(x, self .minimum, self .maximum)

    def naik(self , x):
    if x >= self .maximum:
    return 1
    elif x<= self .minimum:
    return 0
    else :
    return up(x, self .minimum, self .maximum)

class persediaan():
minimum = 200
maximum = 300

def sedikit(self , x):
if x >= self .maximum:
return 0
elif x<= self .minimum:
return 1
else :
return down(x, self .minimum, self .maximum)

def banyak(self , x):
if x >=self .maximum:
return 1
elif x<= self .minimum:
return 0
else :
return up(x, self .minimum, self .maximum)


class produksi():
minimum = 2000
maximum = 6000
permintaan = 0
persediaan = 0

def _berkurang(self, a):
return a*(self.maximum - self.maximum)

def _bertambah(self, a):
return a*(self.maximum - self.minimum) + self.minimum

def _inferensi(self, pmt=permintaan(), psd=persediaan()):
result = []
# [R1] JIKA permintaan TURUN, dan persediaan BANYAK, MAKA
# produksi Barang BERKURANG.
a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
z1 = self._berkurang(a1)
result.append((a1, z1))
# [R2] JIKA permintaan TURUN, dan persediaan SEDIKIT, MAKA
# produksi Barang BERKURANG.
a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
z2 = self._berkurang(a2)
result.append((a2, z2))
# [R3] JIKA permintaan NAIK, dan persediaan BANYAK, MAKA
# produksi Barang BERTAMBAH.
a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
z3 = self._bertambah(a3)
result.append((a3, z3))
# [R4] JIKA permintaan NAIK, dan persediaan SEDIKIT, MAKA
# produksi Barang BERTAMBAH.
a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
z4 = self._bertambah(a4)
result.append((a4, z4))
return result

def defuzifikasi(self, data_inferensi=[]):
# (a1*z1+a2*z2+a3*z3+a4*z4) / (a1+a2+a3+a4)
data_inferensi = data_inferensi if data_inferensi else self._inferensi()
res_a_z = 0
res_a = 0
for data in data_inferensi:
    # data[0] = a
    # data[1] = z
    res_a_z += data[0] * data[1]
    res_a += data[0]
    return res_a_z/res_a