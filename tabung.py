# Menghitung Volume Tabung with Language Support

print("========================")
print("Menghitung Volume Tabung")
print("========================")

# Pilih bahasa
language = input("Pilih bahasa / Choose language (id/en): ").strip().lower()

# Menentukan pesan berdasarkan pilihan bahasa
if language == 'id':
    # Nilai Phi untuk perhitungan
    Phi = 3.14

    # Meminta user untuk memasukkan nilai jari-jari (radius) dan tinggi (height)
    r = float(input("Masukkan nilai jari-jari: "))
    t = float(input("Masukkan nilai tinggi: "))
    
    # Menghitung volume tabung
    tabung = Phi * r * r * t
    
    # Menampilkan hasil
    print("Jadi volume tabung: " + str(tabung))

elif language == 'en':
    # Value of Pi for computation
    Phi = 3.14

    # Asking the user to enter the radius and height
    r = float(input("Enter the radius: "))
    t = float(input("Enter the height: "))
    
    # Calculating the volume of the cylinder
    tabung = Phi * r * r * t
    
    # Displaying the result
    print("The volume of the cylinder is: " + str(tabung))
else:
    print("Pilihan bahasa tidak valid. Silakan coba lagi. / Invalid language choice. Please try again.")