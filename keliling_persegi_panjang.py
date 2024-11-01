# Menghitung Keliling Persegi Panjang with Language Support

print("==============================")
print("Menghitung Keliling Persegi Panjang")
print("==============================")

# Pilih bahasa
language = input("Pilih bahasa / Choose language (id/en): ").strip().lower()

# Menentukan pesan berdasarkan pilihan bahasa
if language == 'id':
    # Meminta user untuk memasukkan nilai panjang dan lebar
    panjang = int(input('Masukkan nilai panjang: '))
    lebar = int(input('Masukkan nilai lebar: '))
    
    # Menghitung keliling persegi panjang
    kel = 2 * (panjang + lebar)
    
    # Menampilkan hasil
    print("Hasil = " + str(kel))

elif language == 'en':
    # Asking the user to enter the length and width
    panjang = int(input('Enter the length: '))
    lebar = int(input('Enter the width: '))
    
    # Calculating the perimeter of the rectangle
    kel = 2 * (panjang + lebar)
    
    # Displaying the result
    print("Result = " + str(kel))

else:
    print("Pilihan bahasa tidak valid. Silakan coba lagi. / Invalid language choice. Please try again.")