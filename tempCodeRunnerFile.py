# Input
gaji_per_jam = float(input("Masukkan gaji per jam yang Anda inginkan: "))
jam_kerja_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

# Hitung pendapatan sebelum pajak
pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja_per_minggu * 5

# Hitung pajak yang harus dibayarkan
pajak = pendapatan_sebelum_pajak * 0.14

# Hitung pendapatan setelah pajak
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak

# Hitung pengeluaran untuk membeli pakaian dan aksesoris
pengeluaran_pakaian_aksesoris = pendapatan_setelah_pajak * 0.1

# Hitung pengeluaran untuk membeli alat tulis
pengeluaran_alat_tulis = pendapatan_setelah_pajak * 0.01

# Hitung jumlah uang yang akan disedekahkan
sedekah = (pendapatan_setelah_pajak - pengeluaran_pakaian_aksesoris - pengeluaran_alat_tulis) * 0.25

# Hitung jumlah uang yang akan diterima anak yatim
uang_anak_yatim = sedekah%1000

modulus = sedekah - uang_anak_yatim

total_uang_yatim = modulus * 0.3

# Hitung jumlah uang yang akan diterima kaum dhuafa
uang_kaum_dhuafa = sedekah - total_uang_yatim

# Output
print(f"1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp{pendapatan_sebelum_pajak:,.2f}")
print(f"2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp{pendapatan_setelah_pajak:,.2f}")
print(f"3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp{pengeluaran_pakaian_aksesoris:,.2f}")
print(f"4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp{pengeluaran_alat_tulis:,.2f}")
print(f"5. Jumlah uang yang akan Budi sedekahkan: Rp{sedekah:,.2f}")
print(f"6. Jumlah uang yang akan diterima anak yatim: Rp{total_uang_yatim:,.2f}")
print(f"7. Jumlah uang yang akan diterima kaum dhuafa: Rp{uang_kaum_dhuafa:,.2f}")