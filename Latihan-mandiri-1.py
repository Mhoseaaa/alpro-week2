# Meminta pengguna untuk memasukkan bilangan
berat = float(input("Masukkan berat anda dalam Kilogram  : "))
tinggi = float(input("Masukkan berat anda dalam meter    : "))

# Menghitung BMI
bmi = berat / (tinggi ** 2)

# Menampilkan hasil / output
print("BMI anda adalah   : ", bmi)
