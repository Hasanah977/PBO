class Kosmetik(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def pakai(self):
        print('{} sedang digunakan'.format(self.nama))


class KosmetikWanita(Kosmetik):
    jenis = None
    warna = None

    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def set_warna(self, warna):
        self.warna = warna

    def pakai(self):
        print('{} jenis {} dengan warna {} sedang digunakan'.format(
            self.nama, self.jenis, self.warna))


# Contoh objek
lipstik = KosmetikWanita('Lipstik', 'Matte')
lipstik.set_warna('Merah Muda')
lipstik.pakai()

bedak = KosmetikWanita('Bedak', 'Glow To Glow')
bedak.set_warna('Natural Beige')
bedak.pakai()