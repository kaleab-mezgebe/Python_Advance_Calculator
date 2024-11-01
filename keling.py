# Define constants
Phi = 3.14

# Language selection
print("Please select a language:")
print("Press 1 for Indonesian")
print("Press 2 for English")
language_option = input("Your choice (1 or 2): ")

if language_option == '1':
    prompt_radius = "Masukkan nilai jari-jari: "
    output_message = "Jadi nilai keliling: "
elif language_option == '2':
    prompt_radius = "Enter the value of the radius: "
    output_message = "So the circumference is: "
else:
    print("Invalid option selected. Exiting.")
    exit()

# Input radius
r = float(input(prompt_radius))

# Calculate circumference
keling = 2 * Phi * r

# Print output
print(output_message + str(keling))