#LATIHAN1(7)
TUGAS STRUKTUR KONDISI
#LATIHAN 1
Buat program sederhana dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

#Masukan input 
bil1 = int (input("Masukan bilangan : "))
bil2 = int (input("Masukan bilangan : "))

#Nilai terbesar

if (bil1 > bil2):
   print("Bilangan terbesar :",bil1)

#Nilai terkecil

if (bil1 < bil2):
   print("Bilangan terbesar :",bil2)
   #HASIL PROGRAM
   ![image](https://github.com/vianirmalamahdalena05/latihan7/assets/147572078/4ceb0db5-277c-42e8-897e-18cc8144d03c)


#LATIHAN 2
Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.

#masukan inputan
bil1 = int(input("Bilangan ke-1: "))
bil2 = int(input("Bilangan ke-2: "))
bil3 = int(input("Bilangan ke-3: "))

#Buat variable data
data = [bil1, bil2, bil3]

#Menampilkan data
print("Data sebelum di urutkan :", data)
list.sort(data)
print("Data setelah di urutkan :", data)
#HASIL PROGRAM
![image](https://github.com/vianirmalamahdalena05/latihan7/assets/147572078/efba8d56-aa65-4498-9cf3-aa7eb74985fb)


#LATIHAN 2 (7)
TUGAS PERULANGAN
Buat program dengan perulangan bertingkat (nested) for yang menghasilkan output sebagai berikut:
#LATIHAN 1
baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
    #HASIL PROGRAM
    ![image](https://github.com/vianirmalamahdalena05/latihan7/assets/147572078/6577a228-f694-42d6-a351-83463d61a583)


#LATIHAN 2
TUGAS PERULANGAN
Tampilkan bilangan acak yang lebih kecil dari 0.5. nilai diisi pada saat runtime anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya.
import random

print("===========================================")
print("= Bilangan acak yang lebih kecil dari 0,5 =")
print("===========================================")

jum = int( input("Masukan nilai: "))
i = 0
while i in range(jum):
    i += 1
    angkarandom = random.uniform(0,0.5)
    print("Bilangan ke :", i, " : ", angkarandom)
    #HASIL PROGRAM
    ![image](https://github.com/vianirmalamahdalena05/latihan7/assets/147572078/173bfe5d-1a70-4bca-a116-99679354ed32)
