# Language selection
print("Please select a language:")
print("Press 1 for Indonesian")
print("Press 2 for English")
language_option = input("Your choice (1 or 2): ")

# Define messages based on selected language
if language_option == '1':
    print("======================")
    print("Menghitung Massa Jenis")
    print("======================")
    prompt_mass = "Masukkan nilai massa: "
    prompt_volume = "Masukkan nilai volume: "
    output_message = "Jadi nilai massa jenis: "
elif language_option == '2':
    print("===========================")
    print("Calculating Density")
    print("===========================")
    prompt_mass = "Enter the value of mass: "
    prompt_volume = "Enter the value of volume: "
    output_message = "So the value of density is: "
else:
    print("Invalid option selected. Exiting.")
    exit()

# Input mass and volume
m = float(input(prompt_mass))
v = float(input(prompt_volume))

# Calculate density
p = m / v

# Print output
print(output_message + str(p))