import math

def calculate_sphere_area(radius):
    area = 4 * math.pi * radius**2
    return area

def main():
    print("Choose a language:")
    print("1. English")
    print("2. Indonesian")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("You chose English.")
        radius = float(input("Enter the radius of the sphere: "))
        area = calculate_sphere_area(radius)
        print(f"The surface area of the sphere is: {area:.2f} square units.")

    elif choice == '2':
        print("Anda memilih Bahasa Indonesia.")
        radius = float(input("Masukkan jari-jari bola: "))
        area = calculate_sphere_area(radius)
        print(f"Luas permukaan bola adalah: {area:.2f} satuan persegi.")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()