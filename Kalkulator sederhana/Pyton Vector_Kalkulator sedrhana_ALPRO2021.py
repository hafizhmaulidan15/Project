def jumlah(a,b) : #fungsi penjumlahan
    x = a + b  #operasi hitungan pertambahan
    print('Hasilnya adalah', x) #hasil dari pengoperasian pertambahan
    return x #pengembalian fungsi X ke baris setelah fungsi def

def kurang(a,b) : #fungsi pengurangan
    x = a - b #operasi hitungan pengurangan
    print('Hasilnya adalah', x) #hasil dari pengoperasian pengurangan
    return x #pengembalian fungsi X ke baris setelah fungsi def

def kali(a,b) : #fungsi perkalian
    x = a * b #operasi hitungan perkalian
    print('Hasilnya adalah', x) #hasil dari pengoperasian perkalian
    return x #pengembalian fungsi X ke baris setelah fungsi def

def bagi(a,b) : #fungsi pembagian
    x = a / b #operasi hitungan pembagian
    print('Hasilnya adalah', x) #hasil dari pengoperasian pembagian
    return x #pengembalian fungsi X ke baris setelah fungsi def

def pangkat(a,b): #fungsi perpangkatan
    x = a ** b #operasi hitungan perpangaktan
    print('hasilnya adalah', x) #hasil dari pengoperasian perpangaktan 
    return x #pengembalian fungsi X ke baris setelah fungsi def

def pembulatan(a,b): #fungsi pembagian pembulatan
    x = a // b #operasi hitungan pembagian pembulatan
    print('hasilnya adalah', x) #hasil dari pengoperasian pembulatan pembagian
    return x #pengembalian fungsi X ke baris setelah fungsi def
 
def sisa(a,b): #fungsi penyisaaan pembagian
    x = a % b #operasi hitungan penyisaan pembagian
    print('hasilnya adalah', x) #hasil dari pengoperasian penyiasaan pembagian
    return x #pengembalian fungsi X ke baris setelah fungsi def

print("Kalkulator sederhana") #nama program yang akan di jalankan
print("1. Penjumlahan\n" "2. Pengurangan\n" "3. Perkalian\n" "4. Pembagian\n" "5. Perpangkatan\n" "6. pembualatan pembagian\n" "7. sisa dari hasil pembagian\n") #pilihan variabel yang akan diinputkan
pilihan = int(input('Masukkan pilihan anda : ')) #user diperintahkan untuk menginput  angka 1-7

if pilihan == 1 : #memasukan pilihan 1
    print('Anda memilih operasi penjumlahan') #nama pengoperasian yang dipilih adalah penjumlahan
    b1 = int(input('Masukkan angka pertama : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka kedua : ')) #user di minta memasuakn angkaa kedua
    jumlah(b1,b2) #pemangilan fungsi def penjumlahan

elif pilihan == 2 : #memasukan pilihan 2
    print('Anda memilih operasi pengurangan') #nama pengoperasian yang dipilih adalah pengurangan
    b1 = int(input('Masukkan angka pertama : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka kedua : ')) #user di minta memasuakn angkaa kedua
    kurang(b1,b2) #pemangilan fungsi def pengurangan

elif pilihan == 3 : #memasukan pilihan 3
    print('Anda memilih operasi perkalian') #nama pengoperasian yang dipilih adalah perkalian
    b1 = int(input('Masukkan angka pertama : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka kedua : ')) #user di minta memasuakn angkaa kedua
    kali(b1,b2)   #pemangilan fungsi def perkalian

elif pilihan == 4 : #memasukan pilihan 4
    print('Anda memilih operasi pembagian') #nama pengoperasian yang dipilih adalah pembagian
    b1 = int(input('Masukkan angka pertama : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka kedua : ')) #user di minta memasuakn angkaa kedua
    bagi(b1,b2) #pemangilan fungsi def pembagian

elif pilihan == 5 : #memasukan pilihan 5
    print('Anda memilih operasi perpangkatan') #nama pengoperasian yang dipilih adalah perpangaktan
    b1 = int(input('Masukkan angka yang akan di pangkatkan : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka pangkatnya : ')) #user di minta memasuakn angkaa kedua
    pangkat(b1,b2) #pemangilan fungsi def perpangakatan

elif pilihan == 6 : #memasukan pilihan 6
    print('Anda memilih operasi pembualatan pembagian') #nama pengoperasian yang dipilih adalah pembulatan pembagian
    b1 = int(input('Masukkan angka yang akan di pangkatkan : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka pangkatnya : ')) #user di minta memasuakn angkaa kedua
    pembulatan(b1,b2) #pemangilan fungsi def pembulatan

elif pilihan == 7 : #memasukan pilihan 7
    print('Anda memilih operasi sisa dari hasil pembagian') #nama pengoperasian yang dipilih adalah sisa dari hasil pembagian
    b1 = int(input('Masukkan angka yang akan di bagi : ')) #user di minta memasuakn angkaa pertama
    b2 = int(input('Masukkan angka di bagi nya : ')) #user di minta memasuakn angkaa kedua
    sisa(b1,b2) #pemangilan fungsi def penyisaaan pembagian

else:
    print('maaf yang anda pilih tidak ada di daftar') # tidak memanggil fungsi def dikarekan di luar dari perintah 
    
