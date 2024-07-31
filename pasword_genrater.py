import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:

            length = int(input("Enter the desired length for your password: "))
            if length < 1:
                print("Password length should be at least 1.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        password = generate_password(length)
        print(f"Generated password: {password}")


        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thanks for using the password generator!")

if __name__ == "__main__":
    main()
