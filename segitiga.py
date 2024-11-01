# Language selection
print("Please select a language:")
print("Press 1 for Indonesian")
print("Press 2 for English")
language_option = input("Your choice (1 or 2): ")

# Define messages based on selected language
if language_option == '1':
    print("==========================")
    print("=Menghitung Luas Segitiga=")
    print("==========================")
    prompt_base = "Masukkan nilai alas: "
    prompt_height = "Masukkan nilai tinggi: "
    output_message = "Jadi luas segitiga: "
elif language_option == '2':
    print("===========================")
    print("=Calculating Area of Triangle=")
    print("===========================")
    prompt_base = "Enter the value of base: "
    prompt_height = "Enter the value of height: "
    output_message = "So the area of the triangle is: "
else:
    print("Invalid option selected. Exiting.")
    exit()

# Input base and height
a = float(input(prompt_base))
t = float(input(prompt_height))

# Calculate area of the triangle
seg = a * t / 2

# Print output
print(output_message + str(seg))