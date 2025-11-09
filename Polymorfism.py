# =====================================
# Contoh Polymorphism dalam Python
# =====================================

# Polymorphism artinya "banyak bentuk".
# Dalam OOP, satu method yang sama bisa berperilaku berbeda
# tergantung dari objek (class) yang memanggilnya.

# --- Bagian 1: Superclass ---      
class Animal:
    # Kelas dasar yang mewakili semua hewan
    def speak(self):
        # Method ini akan di-override oleh subclass
        # raise artinya memunculkan error jika subclass tidak menulis ulang method ini
        raise NotImplementedError("Subclass harus mengimplementasikan method speak()")

# --- Bagian 2: Subclass yang meng-override method speak() ---
class Dog(Animal):
    # Kelas Dog mewarisi dari Animal
    def speak(self):
        # Mengoverride method speak() sesuai karakter anjing
        return "Woof!"

class Cat(Animal):
    # Kelas Cat juga mewarisi dari Animal
    def speak(self):
        # Mengoverride method speak() sesuai karakter kucing
        return "Meow!"

class Cow(Animal):
    # Kelas Cow juga mengoverride method speak()
    def speak(self):
        return "Moo!"

# --- Bagian 3: Fungsi yang menunjukkan Polymorphism ---
def make_animal_speak(animal):
    # Fungsi ini bisa menerima semua jenis hewan
    # Tidak peduli objeknya Dog, Cat, atau Cow
    print(f"{animal.__class__.__name__} says: {animal.speak()}")

# --- Bagian 4: Membuat objek dan menjalankan fungsi ---
dog = Dog()
cat = Cat()
cow = Cow()

# Memanggil fungsi yang sama tapi hasilnya berbeda (inilah polymorphism)
make_animal_speak(dog)   # Output: Dog says: Woof!
make_animal_speak(cat)   # Output: Cat says: Meow!
make_animal_speak(cow)   # Output: Cow says: Moo!


# --- Bagian 5: Contoh Polymorphism tanpa pewarisan (Duck Typing) ---
class Human:
    # Tidak mewarisi dari Animal tapi punya method speak()
    def speak(self):
        return "Hello!"

def make_it_speak(obj):
    # Fungsi ini tidak peduli apakah obj turunan Animal atau bukan,
    # asalkan punya method speak(), tetap bisa dipanggil.
    print(f"{obj.__class__.__name__} says: {obj.speak()}")

# Human tetap bisa bicara walau bukan subclass Animal
print("\nDuck Typing Example:")
make_it_speak(Human())  # Output: Human says: Hello!
make_it_speak(Dog())    # Output: Dog says: Woof!
make_it_speak(Cat())    # Output: Cat says: Meow!


# --- Bagian 6: Operator Overloading (Ad-hoc Polymorphism) ---
class Vector:
    # Representasi vektor 2D
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Menggunakan operator + untuk menjumlahkan dua objek Vector
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        # Menampilkan hasilnya dengan format yang mudah dibaca
        return f"Vector({self.x}, {self.y})"

print("\nOperator Overloading Example:")
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2   # Memanggil __add__ secara otomatis
print(v3)      # Output: Vector(6, 8)
