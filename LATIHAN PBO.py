class Manusia(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print('{} makan nasi.'.format(self.nama))

class ManusiaMilenial(Manusia):
    nama = None
    email = None

    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print('{} makan nasi.'.format(self.nama))

    def set_email(self, email):
        self.email = email

programmer = ManusiaMilenial('Eka')
programmer.set_email('eka@test.com')
programmer.makan()

petani = ManusiaMilenial('Putra')
petani.set_email('putra@test.com')
petani.makan()