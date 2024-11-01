import math

def calculate_cone_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    lateral_area = math.pi * radius * slant_height
    base_area = math.pi * radius**2
    total_area = lateral_area + base_area
    return total_area

def main():
    print("Choose a language:")
    print("1. English")
    print("2. Indonesian")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("You chose English.")
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        area = calculate_cone_area(radius, height)
        print(f"The total surface area of the cone is: {area:.2f}")

    elif choice == '2':
        print("Anda memilih Bahasa Indonesia.")
        radius = float(input("Masukkan jari-jari kerucut: "))
        height = float(input("Masukkan tinggi kerucut: "))
        area = calculate_cone_area(radius, height)
        print(f"Luas permukaan total kerucut adalah: {area:.2f}")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()