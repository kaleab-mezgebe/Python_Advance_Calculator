# Language selection
print("Please select a language:")
print("Press 1 for Indonesian")
print("Press 2 for English")
language_option = input("Your choice (1 or 2): ")

# Define messages based on selected language
if language_option == '1':
    print("===========================")
    print("=Menghitung Luas Lingkaran=")
    print("===========================")
    prompt_radius = "Masukkan nilai jari-jari: "
    output_message = "Jadi luas lingkaran: "
elif language_option == '2':
    print("===========================")
    print("=Calculating Area of Circle=")
    print("===========================")
    prompt_radius = "Enter the value of the radius: "
    output_message = "So the area of the circle is: "
else:
    print("Invalid option selected. Exiting.")
    exit()

# Define constant
Phi = 3.14

# Input radius
r = float(input(prompt_radius))

# Calculate area
ling = Phi * r * r

# Print output
print(output_message + str(ling))