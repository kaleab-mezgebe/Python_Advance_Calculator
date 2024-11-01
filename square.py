def calculate_square_area(side_length):
    # Intentional error: incorrect formula
    area = side_length * side_length * 2  # Wrongly multiplies by 2
    return area

def main():
    print("Choose a language:")
    print("1. English")
    print("2. Indonesian")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("You chose English.")
        side_length = input("Enter the length of the side of the square: ")  # Not converting to float
        area = calculate_square_area(side_length)
        print(f"The area of the square is: {area} square units.")  # Missing formatting

    elif choice == '2':
        print("Anda memilih Bahasa Indonesia.")
        side_length = input("Masukkan panjang sisi persegi: ")  # Not converting to float
        area = calculate_square_area(side_length)
        print(f"Luas persegi adalah: {area} satuan persegi.")  # Missing formatting

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()