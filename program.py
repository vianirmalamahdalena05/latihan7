modal_awal = 100_000_000  # Modal awal 100 juta
laba = [0, 0, 0, 0, 0, 0, 0, 0]  # Inisialisasi laba tiap bulan

# Bulan ke-3
laba[2] = modal_awal * 0.01

# Bulan ke-5
laba[4] = modal_awal * 0.05

# Bulan ke-8
laba[7] = modal_awal * 0.03

# Menghitung total laba
total_laba = sum(laba)

# Menampilkan laba tiap bulan dan total laba
for bulan, laba_bulanan in enumerate(laba):
    print(f'laba bulan ke-{bulan + 1} sebesar: {laba_bulanan:.1f}')
print(f'Total Laba adalah: {total_laba:.1f}')