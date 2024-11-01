# Language selection
print("Please select a language:")
print("Press 1 for Indonesian")
print("Press 2 for English")
language_option = input("Your choice (1 or 2): ")

# Define messages based on selected language
if language_option == '1':
    print('Menghitung luas permukaan Balok')
    print('===============================')    
    prompt_length = 'Masukkan nilai panjang: '
    prompt_width = 'Masukkan nilai lebar: '
    prompt_height = 'Masukkan nilai tinggi: '
    output_message = 'Hasilnya adalah: '
elif language_option == '2':
    print('Calculating Surface Area of Cuboid')
    print('===============================')
    prompt_length = 'Enter the value of length: '
    prompt_width = 'Enter the value of width: '
    prompt_height = 'Enter the value of height: '
    output_message = 'The result is: '
else:
    print("Invalid option selected. Exiting.")
    exit()

# Input dimensions
panjang = float(input(prompt_length))
lebar = float(input(prompt_width))
tinggi = float(input(prompt_height))

# Calculate surface area
lukan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Print output
print(output_message + str(lukan))